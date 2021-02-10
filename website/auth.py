from flask import Blueprint, request

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


    return "<p>Sign Up</p>"

