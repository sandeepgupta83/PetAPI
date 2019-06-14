from app import db, ma
from marshmallow import Schema, fields, pprint
# from api.models.person import PersonSchema

# A pet has only one owner
class Pet(db.Model):
    __tablename__ = 'pet'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(30), unique=True, nullable=True)
    owner_id = db.Column('owner_id', db.Integer, db.ForeignKey('person.id'))

    # def __str__(self):
    #     return "Pet(id<{}>, name<{}>)".format(self.id, self.name)


# class PetSchema(ma.ModelSchema):
#     class Meta:
#         # owner = fields.Nested(PersonSchema())
#         # fields = ('id', 'name', 'owner_id')
#         model = Pet

class PetSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    owner_id = fields.Int()
    # owner = fields.Nested(PersonSchema(), many=True)

# if __name__ == '__main__':
# #     print('PET Class')