from flask import Flask, Blueprint, render_template

comefly = Blueprint('comefly', __name__)


@comefly.route('/comefly',  methods=['GET', 'POST'])
def come_fly(): 
    return render_template('comefly.html')