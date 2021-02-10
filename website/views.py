#routes except for authentication
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")