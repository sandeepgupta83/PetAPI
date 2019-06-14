from flask_restplus import Resource
from flask import request
from api.handlers.person import PersonHandler
from api.handlers.utils import Utils


class Person(Resource):

    def get(self, person_id=None):
        if person_id is not None:
            # return Utils.serialize_person(PersonHandler.read_by_id(person_id)), 200
            return Utils.serialize_person_marsh(PersonHandler.read_by_id(person_id)), 200
        else:
            return Utils.serialize_person_list(PersonHandler.get_all_persons()), 200

    # Example with JSON
    def post(self):
        if request.is_json:
            data = request.get_json()
            print(data)
            person = PersonHandler.add_person(data['person_name'])
            return {"message": "Person created {} {}".format(person.id, person.name)}, 201

    def put(self):
        if request.is_json:
            data = request.get_json()
            print(data)
            person = PersonHandler.update_person(data['person_id'], data['person_name'])
            return {"message": "Person updated {} {}".format(person.id, person.name)}, 201

    def delete(self):
        if request.is_json:
            data = request.get_json()
            person_id = data['person_id']
            print(person_id)
            get_person = PersonHandler.read_by_id(int(person_id))
            delete_id = get_person.id
            person_name = get_person.name
            print(delete_id, person_name)

            result = PersonHandler.delete_person(person_id)
            return {"message": " person deleted from db {} {}".format(delete_id, person_name)}, 200


# class PersonList(Resource):
#     def get(self):
#         return Utils.serialize_person_list(PersonHandler.get_all_persons()), 200


