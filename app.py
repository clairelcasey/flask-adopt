"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/')
def list_pets():
    """ List all pets. """

    pets = Pet.query.all()
    return render_template("pet-list.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """ Render add pet form template or
    handle adding pet if form has been filled out
    and it is a POST request"""

    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data
            )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} was added to the system!")
        return redirect("/")
    else:
        return render_template("add-pet-form.html", form=form)
