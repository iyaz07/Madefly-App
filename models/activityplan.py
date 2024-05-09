from . import db
from datetime import datetime


class ActivityPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    morning_activity = db.Column(db.String(100))
    afternoon_activity = db.Column(db.String(100))
    evening_activity = db.Column(db.String(100))
    age_category = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))