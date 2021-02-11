from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash,check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    data = request.form
    print(data)
    return "<p>Login</p>"

@auth.route("/logout")
def logout():

    return "<p>Logout</p>"

@auth.route("/sign-up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        new_user = User(email=email, name=name, password= generate_password_hash(password1, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template("sign_up.html")

