"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, Optional


class AddPetForm(FlaskForm):
    """ Form to add a new pet """

    name = StringField(
        "Pet Name", 
        validators=[InputRequired()])
    species = SelectField(
        "Species", 
        choices=[
            ('cat', 'Cat'),
            ('dog', 'Dog'),
            ('porcupine', 'Porcupine')
            ],
        validators=[InputRequired()])
    photo_url = StringField(
        "Photo URL", 
        validators=[Optional(), URL()])
    age = SelectField(
        "Age",
        validators=[InputRequired()],
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Senior'),
            ('senior', 'Senior')
            ])
    notes = StringField(
        'Notes', 
        validators=[Optional()])
    available = BooleanField(
        "Available",
        validators=[Optional()],
        default=True
    )

class EditPetForm(FlaskForm):
    """ Form to edit an existing pet """

    photo_url = StringField(
        "Photo URL", 
        validators=[Optional(), URL()])
    notes = StringField(
        'Notes', 
        validators=[Optional()])
    available = SelectField(
    "Available",
    choices=[
        ("True", 'yes'),
        ("", 'no')],
        coerce=bool
    )