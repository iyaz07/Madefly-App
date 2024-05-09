from . import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at =db.Column(db.DateTime, default=datetime.utcnow)
    age = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    bmi = db.Column(db.Integer, nullable=False)
    bmi_category = db.Column(db.String(50), nullable=True)
    activity_plans = db.relationship('ActivityPlan', backref='user', lazy=True)
    meal_plans = db.relationship('MealPlan', backref='user', lazy=True)

    def __repr__(self):
        return f'{self.name}, {self.age}'