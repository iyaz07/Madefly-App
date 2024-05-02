from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)


class Users(db.Model):
   










@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/comefly',  methods=['GET', 'POST'])
def come_fly(): 
    return render_template('comefly.html')


@app.route('/status', methods=["POST"])
def fly_status():
    try:
        name = request.form['name']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        region = request.form['region']

        if not name or not age or not height or not weight:
            error_statement = 'All Form Fields Required'
            return render_template('comefly.html',
                                    error_statement=error_statement,
                                    name=name,
                                    age=age,
                                    height=height,
                                    weight=weight,
                                    region=region)
    except KeyError:
        # Handle the case where the 'region' key is missing from the form data
        name = request.form.get('name', '')
        age = request.form.get('age', '')
        height = request.form.get('height', '')
        weight = request.form.get('weight', '')
        region = request.form.get('region', '')
        error_statement = 'All Form Fields Required'
        return render_template('comefly.html',
                                error_statement=error_statement,
                                name=name,
                                age=age,
                                height=height,
                                weight=weight,
                                region=region)


    bmi = calculate_bmi(convert_feet_to_inches(height), kg_to_lbs(weight))
    bmi_category = get_bmi_category(bmi)      
    return render_template('status.html', name=name, bmi=bmi, category=bmi_category)

def calculate_bmi(inches, pounds):
    weigh = pounds * 703 
    bmi = weigh / inches 
    return (bmi / inches)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

def convert_feet_to_inches(height):
    feet, sub = map(int, height.split("'"))
    inches = feet * 12 + sub
    return inches
def kg_to_lbs(weight):
    pounds = float(weight) * 2.20462
    return pounds


@app.route('/gofly/<name>')
def go_fly(name):
    items = [
        {'id': 1, 'Day': 'Monday', 'Breakfast': 'Eba', 'Lunch': 'Semo', 'Dinner': 'EBA'},
        {'id': 2, 'Day': 'Tuesday', 'Breakfast': 'fish', 'Lunch': 'dog', 'Dinner': 'Obe'},
        {'id': 3, 'Day': 'Wednesday', 'Breakfast': 'tea', 'Lunch': 'bread', 'Dinner': 'garri'},
        {'id': 4, 'Day': 'Thursday', 'Breakfast': 'egusi', 'Lunch': 'yam', 'Dinner': 'Iyan'},
        {'id': 5, 'Day': 'Friday', 'Breakfast': 'noodles', 'Lunch': 'spag', 'Dinner': 'pasta'},
        {'id': 6, 'Day': 'Saturday', 'Breakfast': 'leaf', 'Lunch': 'tame', 'Dinner': 'soko'},
        {'id': 7, 'Day': 'Sunday', 'Breakfast': 'paper', 'Lunch': 'money', 'Dinner': 'money'},
    ]
    return render_template('gofly.html', items=items)

   

if __name__ == "__main__":
    app.run(debug=True)
