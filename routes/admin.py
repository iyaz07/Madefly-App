from flask import Flask, render_template, Blueprint

admin=Blueprint('admin', __name__)

@admin.route('/admin')
def admin_page():
    return render_template('admin.html')