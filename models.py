"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy  #, CheckConstraint
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ Ped model. """

    __tablename__ = "pets"
    # __table_args__ = (42,)
        # db.CheckConstraint("age in ('baby', 'young', 'adult', 'senior')"),)

    id = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True)
    name = db.Column(
        db.String(30),
        nullable=False)
    species = db.Column(
        db.Text,
        nullable=False)
    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=''
    )
    age = db.Column(
        db.Text,
        nullable=False
        # db.CheckConstraint("age in ['baby', 'young', 'adult', 'senior']")
    )
    notes = db.Column(
        db.Text,
        default='',
        nullable=False
    )
    available = db.Column(
        db.Boolean, 
        nullable=False,
        default=True
    )
