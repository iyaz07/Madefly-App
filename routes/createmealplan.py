from flask import Flask, Blueprint, render_template

meal_plan = Blueprint('mealplan', __name__)
@meal_plan.route(/add_meal_plan', methods=['POST'])
    def mealplan():
        return render_template('addmealplan.html')


