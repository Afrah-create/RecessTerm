from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Prediction(db.Model):
    __tablename__ = "predictions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    age = db.Column(db.Integer, nullable=False)
    monthly_income = db.Column(db.Float, nullable=False)
    dependents = db.Column(db.Integer, nullable=False)
    debt_ratio = db.Column(db.Float, nullable=False)
    late_30_59 = db.Column(db.Integer, nullable=False)
    late_60_89 = db.Column(db.Integer, nullable=False)
    late_90 = db.Column(db.Integer, nullable=False)

    prediction = db.Column(db.Integer, nullable=False)
    probability = db.Column(db.Float, nullable=False)
    risk_level = db.Column(db.String(10), nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "age": self.age,
            "monthly_income": self.monthly_income,
            "dependents": self.dependents,
            "debt_ratio": self.debt_ratio,
            "late_30_59": self.late_30_59,
            "late_60_89": self.late_60_89,
            "late_90": self.late_90,
            "prediction": self.prediction,
            "probability": self.probability,
            "risk_level": self.risk_level,
        }