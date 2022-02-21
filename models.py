# """Models for pet adoption app"""
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# GENERAL_IMAGE = "https://www.supermarketnews.com/sites/supermarketnews.com/files/pet-care-coronavirus-happy-dog-and-cat_0.png"

# class Pet(db.Model):
#     """Available pets for adoption"""

#     __tablename__ = 'pets'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.Text, nullable=False)
#     species = db.Column(db.Text, nullable=False)
#     photo_url = db.Column(db.Text)
#     age = db.Column(db.Integer)
#     notes = db.Column(db.Text)
#     available = db.Column(db.Boolean, nullable=False, default=True) 

#     def image_url(self):
#         """Returns default image for pet if no image is given"""
#         return self.photo_url or GENERAL_IMAGE


# def connect_db(app):
#   db.app = app
#   db.init_app(app)


"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()


class Pet(db.Model):
    """Adoptable pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or GENERIC_IMAGE


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
