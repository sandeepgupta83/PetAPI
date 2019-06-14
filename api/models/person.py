from app import db, ma
from marshmallow import Schema, fields, pprint
from api.models.pet import PetSchema

# Person can have many pets


class Person(db.Model):

    __tablename__ = 'person'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode, unique=True, nullable=True)
    pets = db.relationship('Pet', backref='owner')
    #

    def __repr__(self):
        return "Person(id<{}>, name<{}>)".format(self.id, self.name)


class PersonSchema(ma.ModelSchema):
    # id = fields.Int()
    # name = fields.Str()
    pets = fields.Nested(PetSchema(), many=True)
    class Meta:
        # fields = ('id', 'name', 'pets')
#         # table = Person.__tablename__
        model = Person
#         # pets = ma.Nested(PetSchema())


# class PersonSchema(Schema):
#     id = fields.Int()
#     name = fields.Str()
#     pets = fields.Nested(PetSchema(), many=True)

# if __name__ == '__main__':
#     print('Person Class')
