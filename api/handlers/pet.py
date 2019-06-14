from api.models.pet import Pet


class PetHandler:
    @staticmethod
    def getpets_by_ownerid(owner_id):
        pet_data = Pet.query.filter_by(owner_id=owner_id).first()
        return pet_data

    @staticmethod
    def get_all_pets():
        return Pet.query.all()
