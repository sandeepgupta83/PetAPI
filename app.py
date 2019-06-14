import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_restplus import Api

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
ma = Marshmallow(app)
api = Api(app, version='1.0', title='Person and Pet', description='Person and Pet Example')

from api.endpoints.person import Person
from api.endpoints.pet import Pet, PetList
api.add_resource(Person, '/person/<int:person_id>')
api.add_resource(Person, '/person/<string:person_name>')

api.add_resource(Person, '/person')
api.add_resource(PetList, '/pets')

api.add_resource(Pet, '/owner/<int:owner_id>')
api.add_resource(Pet, '/owner')

