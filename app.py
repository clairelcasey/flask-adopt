"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

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
def add_pet(): # pet_add_form -- both shows and process the form
    """ Render add pet form template.
    Handle adding pet."""

    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
            available=form.available.data
            )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} was added to the system!")
        return redirect("/")
    else:
        return render_template("add-pet-form.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_edit_pet_form(pet_id): # pet_edit_form
    """ Show pet information and pet edit form.
    Handle editing a pet.  """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet) #pass any object, it checks the form attribute names on that object. If form already has a new value, it will not use the one from the obj. Called polymorphism

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name} was updated!")
        return redirect(f"/{pet_id}")
    else:
        # show current info for first request, show changed info on failed POST
        # if not form.photo_url.data:
        #     form.photo_url.data = pet.photo_url
        # if not form.notes.data:
        #     form.notes.data = pet.notes
        # form.available.data = pet.available

        return render_template("edit-pet-form.html", form=form, pet=pet)
