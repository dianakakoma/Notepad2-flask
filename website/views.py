#routes except for authentication
from flask import Blueprint, render_template
from flask_login import login_required,  current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("index.html")
#post request

@views.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

#post request
@views.route('/login')
def login():
    return render_template("login.html")