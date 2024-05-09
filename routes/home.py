from flask import Flask, Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    return render_template('home.html')