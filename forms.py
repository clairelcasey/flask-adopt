"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, URL, Optional


class AddPetForm(FlaskForm):
    """ Form to add a new pet """

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField(
        "Age",
        validators=[InputRequired()],
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Senior'),
            ('senior', 'Senior')
            ])
    notes = StringField('Notes', validators=[Optional()])