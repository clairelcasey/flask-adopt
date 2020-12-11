from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

test_pet = Pet(name="TestPet", species="TestSpecies", age="baby")
test_pet_with_image = Pet(name="TestPet2", species="TestSpecies2", photo_url="https://i1.wp.com/www.dailycal.org/assets/uploads/2019/10/animals_wikimedia_cc-900x580.jpg", age="young")
db.session.add(test_pet)
db.session.add(test_pet_with_image)
db.session.commit()
