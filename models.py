from datetime import datetime
from config import db, ma
from sqlalchemy import true


# Define db model to allow working with SQL Alchemy
class Person(db.Model):
    __table_name__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(100), index=True)
    fname = db.Column(db.String(100))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


# Marshmallow Schema 
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Set SQLAlchemy model into model
        model = Person
        # Set SQLAlchemy db session into marshmallow
        sqla_session = db.session
        load_instance = true

