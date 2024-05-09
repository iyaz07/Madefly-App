from flask import Flask, Blueprint, render_template

about = Blueprint('aboutus', __name__)


@about.route('/aboutus',  methods=['GET', 'POST'])
def aboutus(): 
    return render_template('about.html')