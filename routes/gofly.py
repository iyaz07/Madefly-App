from flask import Flask, Blueprint, render_template
from models import db, ActivityPlan, MealPlan, User

gofly = Blueprint('gofly', __name__)

@gofly.route('/gofly/<name>')
def go_fly(name):
    # Retrieve the user based on the provided name
    user = User.query.filter_by(username=name).first()
    meal_plans = user.meal_plans
    
    # If user not found, return an error message
    if not user:
        return "User not found", 404
    
    # Query the ActivityPlan and MealPlan based on user's age category and BMI category
    activity_plan = user.activity_plans
    meal_plan = MealPlan.query.filter_by(bmi_category=user.bmi_category, region=user.region).limit(7).all()
    
    # Render the template with the retrieved data
    return render_template('gofly.html', activity_plan=activity_plan, meal_plan=meal_plan)
