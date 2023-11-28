#!/usr/bin/env python3

# Importing required modules
from random import choice as rc  # Importing the 'choice' function from the 'random' module with an alias 'rc'
from faker import Faker  # Importing the 'Faker' class from the 'faker' module

# Importing Flask application and database models
from app import app
from models import db, Owner, Pet

# Initializing the database with the Flask application

# Creating a Faker instance for generating fake data
fake = Faker()

# Using the Flask application context
with app.app_context():

    # Deleting existing Pet and Owner records in the database
    Pet.query.delete()
    Owner.query.delete()

    # Generating fake Owner records and adding them to the database
    owners = []
    for n in range(50):
        owner = Owner(name=fake.name())  # Creating a fake Owner with a name using Faker
        owners.append(owner)
    db.session.add_all(owners)  # Adding all generated owners to the database

    # Generating fake Pet records and adding them to the database
    pets = []
    species = ['dog', 'cat', 'parrot', 'snake', 'bird']  # List of possible pet species
    for n in range(50):
        # Creating a fake Pet with a name, species (randomly chosen), and owner (randomly chosen from the generated owners)
        pet = Pet(name=fake.first_name(), species=rc(species), owner=rc(owners))
        pets.append(pet)
    db.session.add_all(pets)  # Adding all generated pets to the database

    # Committing the changes to the database
    db.session.commit()
