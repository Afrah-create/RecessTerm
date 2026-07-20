"""
Run this once to create your first login user.
Usage: python seed_user.py
"""
import os
from dotenv import load_dotenv
from flask import Flask
from models import db, User

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    username = input("Username: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    existing = User.query.filter_by(username=username).first()
    if existing:
        print(f"User '{username}' already exists. Aborting.")
    else:
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print(f"User '{username}' created successfully.")