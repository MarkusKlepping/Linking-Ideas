from cgitb import text
from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin

class User (db.Model, CRUDMixin, UserMixin):
    id= db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(40), index = True , unique = True)
    password = db.Column(db.String(120))
    username = db.Column(db.String(80))
    uploads = db.relationship("Upload", backref = "user", lazy = True)

class Upload (db.Model, CRUDMixin, UserMixin):
    id= db.Column(db.Integer, primary_key = True)
    idea = db.Column(db.String(400))
    team = db.Column(db.String(400))
    contact = db.Column(db.String(400))
    title = db.Column(db.String(80), index = True, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))