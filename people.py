from datetime import datetime
from flask import make_response, abort
from config import db
from models import Person, PersonSchema


def create(person):
    """
    Creates a person in the people structure based on passed in person data
    """
    fname = person.get("fname")
    lname = person.get("lname")

    existing_person = (
        Person.query.filter(Person.fname == fname)
        .filter(Person.lname == lname)
        .one_or_none()
    )

    if existing_person is None:
        # Create a person instance using schema and passed-in person
        schema = PersonSchema()
        new_person = schema.load(person, session=db.session)

        # Add person to db
        db.session.add(new_person)
        db.session.commit()
    else:
        abort(409, f"Person with {fname} {lname} already exists")


def read_all():
    """
    :return: list of person in people db
    """

    # Create a list of people from our data
    # Uses SQLAlchemy model to write a SQL like query
    people = Person.query.order_by(Person.lname).all()

    # Serialize data for the response
    # Note: many=True tells PersonSchema to expect an iterable to serialize
    person_schema = PersonSchema(many=True)
    return person_schema.dump(people)


def read_one(person_id):
    """
    Read a person by person_id
    """
    # Find person with required person_id
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person:
        # Note: We don't pass many=True because a single object is passed in to
        # serialize
        person_schema = PersonSchema()
        return person_schema.dump(person)
    else:
        abort(404, f"Person with person_id {person_id} not found")
    return {}


def update(person_id, person):
    """
    Updates person with person_id with passed in person 
    """
    # Get the person requested for update from the db into session
    update_person = Person.query.filter(Person.person_id == person_id).one_or_none()

    # Exit if person to update is not present in db
    if update_person is None:
        abort(404, f"Person with id: {person_id} not found")

    # Try to find after updating existing record, would we get a person that
    # already exists in the db
    fname = person.get("fname")
    lname = person.get("lname")

    existing_person = (
        Person.query
        .filter(Person.fname == fname)
        .filter(Person.lname == lname)
        .one_or_none()
    )

    if existing_person is not None and existing_person.person_id != person_id:
        abort(409, f"Person with {fname} {lname} already exists")

    # Go ahead and update person
    # Turn passed-in person into a db object
    schema = PersonSchema()
    update = schema.load(person, session=db.session)

    update.person_id = update_person.person_id
    # Use .merge() to update record
    db.session.merge(update)
    db.session.commit()

    data = schema.dump(update_person)
    return data, 200


def delete(person_id):
    """
    Deletes person with id
    """
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person:
        db.session.delete(person)
        db.session.commit()
        return make_response(f"Person with id {person_id} successfully deleted", 200)
    else:
        abort(404, f"Person not found for id {person_id}")
