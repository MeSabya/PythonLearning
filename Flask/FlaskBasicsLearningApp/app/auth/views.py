from . import auth_blueprint
from flask import render_template, request

@auth_blueprint.route('/')
def index():
    return render_template('auth/register.html')
