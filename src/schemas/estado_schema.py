from src.common.utils import ma
from src.models.estado_model import EstadoModel
from marshmallow import fields

class EstadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EstadoModel
        ordered = True
        load_instance = True
        include_relationships = True
        #foreign_keys = True
        exclude = ('PRESTAMO',)
        
    PRESTAMO = fields.Nested('PrestamoSchema', many=True)    

class EstadoSchemaValidar(ma.SQLAlchemyAutoSchema):
    IDESTADO = fields.Integer(required=True)
    NOMBRE = fields.String(required=True)
    