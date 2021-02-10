from . import db
from flask_login import UserMixin

class Note(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Interger, db.ForeignKey("user.id"))

class User(db.Model, userMixin)
    id = db.Colmn(db.Interger, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.column(db.String(150))
    name = db.Column(db.String(150))