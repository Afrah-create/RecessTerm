from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model", "random_forest_model.pkl"))
feature_columns = joblib.load(os.path.join(BASE_DIR, "model", "feature_columns.pkl"))


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

    # Age group one-hot (must match training exactly)
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
    # <25 stays all zeros (drop_first=True baseline)

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
        "HighDebtRatio": debt_ratio_flag,  # or recompute vs median if you saved it
        "HasAnyLatePayment": has_any_late_payment,
        **age_groups
    }

    input_df = pd.DataFrame([row])
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)
    return input_df


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    input_df = build_features(request.form)
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    result = {
        "prediction": "High Risk (Likely Delinquent)" if prediction == 1 else "Low Risk",
        "probability": f"{probability:.2%}",
        "risk_level": "high" if probability >= 0.5 else "low"
    }
    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)