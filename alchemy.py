import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restplus import Resource, Api


# SQLite Database path
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "practice.db"))

# Flask application
app = Flask(__name__)
# Allow CORS to make requests across the domains
CORS(app)

# Create the DB object
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
api = Api(app, version='1.0', title='Person and Pet', description='Person and Pet Example')

# ns = api.namespace('personspet', description='Person and Pet operations')

from api.endpoints.person import Person
api.add_resource(Person, '/person/<int:id>')

# # Person can have many pets
# class Person(db.Model):
#     __tablename__ = 'person'
#     id = db.Column('id', db.Integer, primary_key=True)
#     name = db.Column('name', db.Unicode, unique=True, nullable=True)
#     pets = db.relationship('Pet', backref='owner')
#
#     # def __init__(self, id, name):
#     #     self.id = id
#     #     self.name = name
#
#     def __str__(self):
#         return "Person(id<{}>, name<{}>)".format(self.id, self.name)

# A pet has only one owner
# class Pet(db.Model):
#     __tablename__ = 'pet'
#     id = db.Column('id', db.Integer, primary_key=True)
#     name = db.Column('name', db.String(30), unique=True, nullable=True)
#     owner_id = db.Column('owner_id', db.Integer, db.ForeignKey('person.id'))
#     #
#     # def __init__(self, id, name):
#     #     self.id = id
#     #     self.name = name
#
#     def __str__(self):
#         return "Pet(id<{}>, name<{}>)".format(self.id, self.name)

# @api.route('/person/<int:person_id>')
# class Persondata(Resource):
#     def get(self, person_id):
#         from models.person import Person
#         data = Person.query.filter_by(id=person_id).first()
#         retval = {
#             'id': data.id,
#             'name': data.name
#         }
#         print(retval)
#         return retval, 200


if __name__ == '__main__':
    # Sample Data
    # from models.person import Person
    # from models.pet import Pet
    # person1 = Person(name='Holly')
    # person2 = Person(name='Polly')
    # person3 = Person(name='Solly')
    # db.session.add(person1)
    # db.session.add(person2)
    # db.session.add(person3)
    # pet1 = Pet(name='Dog', owner_id=1)
    # pet2 = Pet(name='Tortoise', owner_id=1)
    # pet3 = Pet(name='Parrot', owner_id=2)
    # pet4 = Pet(name='Pigeon', owner_id=2)
    # pet5 = Pet(name='Fish', owner_id=3)
    # db.session.add(pet1)
    # db.session.add(pet2)
    # db.session.add(pet3)
    # db.session.add(pet4)
    # db.session.add(pet5)
    # db.session.commit()
    app.run(debug=True)
