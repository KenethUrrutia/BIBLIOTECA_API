from src.common.utils import ma
from src.models.libro_model import LibroModel
from marshmallow import fields, validate

class LibroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LibroModel
        ordered = True
        load_instance = True
        # include_fk = True
        # include_relationships = True

class LibroSchemaValidar(ma.SQLAlchemyAutoSchema):
    IDLIBRO = fields.Integer(required=True)
    TITULO = fields.String(required=True)
    AUTOR = fields.String(allow_none=True)
    ANIO_PUBLICACION = fields.Date(allow_none=True)
    IDGENERO = fields.Integer(required=True)
