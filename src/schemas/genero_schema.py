from src.common.utils import ma
from src.models.genero_model import GeneroModel
from marshmallow import fields

class GeneroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GeneroModel
        ordered = True
        load_instance = True
        include_relationships = True
        #foreign_keys = True
        exclude = ('LIBROS',)
    LIBROS = fields.Nested('LibroSchema', many=True)

class GeneroSchemaValidar(ma.SQLAlchemyAutoSchema):
    IDGENERO = fields.Integer(required=True)
    NOMBRE = fields.String(required=True)
    