from flask_restplus import Resource
from api.handlers.pet import PetHandler
from api.handlers.utils import Utils


class Pet(Resource):
    def get(self, owner_id):
        print('Calling Pet with owner_id')
        return Utils.serialize_pet(PetHandler.getpets_by_ownerid(owner_id))

class PetList(Resource):
    def get(self):
        print('Calling PetList')
        return Utils.serialize_pet_list(PetHandler.get_all_pets())

