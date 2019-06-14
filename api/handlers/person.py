from api.models.person import Person
from app import db


class PersonHandler:

    @staticmethod
    def read_by_id(person_id):
        person_data = Person.query.filter_by(id=person_id).first()
        # print(person_data.id, person_data.name)
        return person_data

    @staticmethod
    def get_all_persons():
        all_persons = Person.query.all()
        return all_persons

    @staticmethod
    def add_person(person_name):
        person = Person(name=person_name)
        db.session.add(person)
        db.session.commit()
        return person

    @staticmethod
    def update_person(person_id, person_name):
        person_data = Person.query.filter_by(id=person_id).first()
        person_data.name = person_name
        db.session.commit()
        return person_data

    @staticmethod
    def delete_person(person_id):
        db.session.delete(Person.query.filter_by(id=person_id).first())
        db.session.commit()
        return True
