from flask import Flask, Blueprint, render_template, request
from sqlalchemy.exc import IntegrityError
from models import db, User, ActivityPlan, MealPlan


from middleware.utils import *

flystatus = Blueprint('flystatus', __name__)

@flystatus.route('/status', methods=['POST'],)
def fly_status():
    try:
        name = request.form['name']
        age = age_group(request.form['age'])
        height = request.form['height']
        weight = request.form['weight']
        region = request.form['region']
        bmi = calculate_bmi(convert_feet_to_inches(height), kg_to_lbs(weight))
        bmi_category = get_bmi_category(bmi)
        user = User(username=name, age=age, region=region, bmi=bmi, bmi_category=bmi_category)

        # Add user to the database session and commit changes
        db.session.add(user)
        db.session.commit()    

        return render_template('status.html', name=name, bmi=bmi, category=bmi_category)  
    except IntegrityError as e:
        # Rollback the session to prevent partially inserted data
        db.session.rollback()
        error_message = f"Username '{name}' already exists. Please choose a different username."
        
        # Return the error message to the client
        return render_template('comefly.html', error_statement=error_message,
                                name=name, age=age, height=height, weight=weight, region=region)
        
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