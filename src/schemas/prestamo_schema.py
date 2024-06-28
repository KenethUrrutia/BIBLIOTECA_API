from src.common.utils import ma
from src.models.prestamo_model import PrestamoModel
from marshmallow import fields, validate

class PrestamoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PrestamoModel
        ordered = True
        load_instance = True
        # include_fk = True
        # include_relationships = True

class PrestamoSchemaValidar(ma.SQLAlchemyAutoSchema):
    IDUSUARIO = fields.Integer(required=True, validate=validate.Range(min=1))
    IDLIBRO = fields.Integer(required=True, validate=validate.Range(min=1))
    IDPRESTAMO = fields.Integer(required=True, validate=validate.Range(min=1))
    FECHA_PRESTAMO = fields.DateTime(required=True)
    FECHA_DEVOLUCION = fields.DateTime(allow_none=True)
    ESTADO = fields.String(allow_none=True)
    IDESTADO = fields.Integer(required=True, validate=validate.Range(min=1))
