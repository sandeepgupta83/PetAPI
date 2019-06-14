from api.models.person import PersonSchema
from api.models.pet import PetSchema


class Utils:

    @staticmethod
    def serialize_person(person_obj):
        return {
            'Person ID': person_obj.id,
            'First Name': person_obj.name,
            'Pets': Utils.serialize_pet_list(person_obj.pets)
        }

    @staticmethod
    def serialize_pet(pet_obj):
        return {
            'Pet Id': pet_obj.id,
            'Pet Name': pet_obj.name,
            'Owner ID': pet_obj.owner_id,
            'Owner': {
                'Owner ID': pet_obj.owner.id,
                'Owner Name': pet_obj.owner.name,
            }
        }

    @staticmethod
    def serialize_pet_list(pet_obj_list):
        return list(map(Utils.serialize_pet, pet_obj_list))

    @staticmethod
    def serialize_person_list(person_obj_list):
        return list(map(Utils.serialize_person, person_obj_list))


    # ------ Marshmallo -----
    @staticmethod
    def serialize_person_marsh(person_obj):
        schema = PersonSchema()
        return schema.dump(person_obj).data

    @staticmethod
    def serialize_pet_marsh(pet_obj):
        schema = PetSchema()
        return schema.dump(pet_obj)

    @staticmethod
    def serialize_person_list_marsh(person_obj_list):
        return list(map(Utils.serialize_person, person_obj_list))




