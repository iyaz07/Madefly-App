from . import db
from datetime import datetime

class MealPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breakfast = db.Column(db.String(200))
    lunch = db.Column(db.String(200))
    dinner = db.Column(db.String(200))
    region = db.Column(db.String(20))
    bmi_category = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    