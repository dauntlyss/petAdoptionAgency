"""Models for pet adoption app"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERAL_IMAGE = https://images.unsplash.com/photo-1600352712371-15fd49ca42b5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=736&q=80

class Pet(db.Model):
    """Available pets for adoption"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True) 


def connect_db(app):
  db.app = app
  db.init_app(app)