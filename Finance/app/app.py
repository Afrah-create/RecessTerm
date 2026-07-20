from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import joblib
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from models import db, User, Prediction

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model", "random_forest_model.pkl"))
feature_columns = joblib.load(os.path.join(BASE_DIR, "model", "feature_columns.pkl"))
debt_ratio_median = joblib.load(os.path.join(BASE_DIR, "model", "debt_ratio_median.pkl"))


def build_features(form):
    age = int(form["age"])
    debt_ratio = float(form["debt_ratio"])
    monthly_income = float(form["monthly_income"])
    dependents = int(form["dependents"])
    late_30_59 = int(form["late_30_59"])
    late_60_89 = int(form["late_60_89"])
    late_90 = int(form["late_90"])

    total_past_due = late_30_59 + late_60_89 + late_90
    income_per_dependent = monthly_income / (dependents + 1)
    debt_ratio_flag = 1 if debt_ratio > 10 else 0
    debt_ratio_log = np.log1p(debt_ratio)
    has_any_late_payment = 1 if total_past_due > 0 else 0
    high_debt_ratio = 1 if debt_ratio > debt_ratio_median else 0

    age_groups = {
        "AgeGroup_25-34": 0, "AgeGroup_35-44": 0,
        "AgeGroup_45-54": 0, "AgeGroup_55-64": 0, "AgeGroup_65+": 0
    }
    if 25 <= age < 35:
        age_groups["AgeGroup_25-34"] = 1
    elif 35 <= age < 45:
        age_groups["AgeGroup_35-44"] = 1
    elif 45 <= age < 55:
        age_groups["AgeGroup_45-54"] = 1
    elif 55 <= age < 65:
        age_groups["AgeGroup_55-64"] = 1
    elif age >= 65:
        age_groups["AgeGroup_65+"] = 1

    row = {
        "age": age,
        "NumberOfTime30-59DaysPastDueNotWorse": late_30_59,
        "DebtRatio": debt_ratio,
        "NumberOfTimes90DaysLate": late_90,
        "NumberOfTime60-89DaysPastDueNotWorse": late_60_89,
        "MonthlyIncome": monthly_income,
        "NumberOfDependents": dependents,
        "DebtRatio_Flag": debt_ratio_flag,
        "DebtRatio_log": debt_ratio_log,
        "TotalPastDue": total_past_due,
        "IncomePerDependent": income_per_dependent,
        "HighDebtRatio": high_debt_ratio,
        "HasAnyLatePayment": has_any_late_payment,
        **age_groups
    }

    raw_inputs = {
        "age": age, "monthly_income": monthly_income, "dependents": dependents,
        "debt_ratio": debt_ratio, "late_30_59": late_30_59,
        "late_60_89": late_60_89, "late_90": late_90
    }

    input_df = pd.DataFrame([row]).reindex(columns=feature_columns, fill_value=0)
    return input_df, raw_inputs


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("home"))
        else:
            flash("Invalid username or password", "error")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/", methods=["GET"])
@login_required
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
@login_required
def predict():
    input_df, raw_inputs = build_features(request.form)
    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1])
    risk_level = "high" if probability >= 0.5 else "low"

    record = Prediction(
        age=raw_inputs["age"],
        monthly_income=raw_inputs["monthly_income"],
        dependents=raw_inputs["dependents"],
        debt_ratio=raw_inputs["debt_ratio"],
        late_30_59=raw_inputs["late_30_59"],
        late_60_89=raw_inputs["late_60_89"],
        late_90=raw_inputs["late_90"],
        prediction=prediction,
        probability=probability,
        risk_level=risk_level,
        created_by=current_user.id,
    )
    db.session.add(record)
    db.session.commit()

    result = {
        "prediction": "High Risk (Likely Delinquent)" if prediction == 1 else "Low Risk",
        "probability": f"{probability:.2%}",
        "risk_level": risk_level
    }
    return render_template("result.html", result=result)


@app.route("/dashboard")
@login_required
def dashboard():
    records = Prediction.query.order_by(Prediction.created_at.desc()).all()
    return render_template("dashboard.html", records=[r.to_dict() for r in records])


@app.route("/api/predictions")
@login_required
def api_predictions():
    records = Prediction.query.order_by(Prediction.created_at.desc()).all()
    return jsonify([r.to_dict() for r in records])


if __name__ == "__main__":
    app.run(debug=True)