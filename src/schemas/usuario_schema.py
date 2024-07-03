from src.common.utils import ma
from src.models.usuario_model import UsuarioModel
from marshmallow import fields, validate

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel
        ordered = True
        load_instance = True
        include_relationships = True
        #foreign_keys = True
        exclude = ('PASSWORD', 'PRESTAMO')
    PRESTAMO = fields.Nested('PrestamoSchema', many=True) 

class UsuarioSchemaValidar(ma.SQLAlchemyAutoSchema):
    IDUSUARIO = fields.Integer(required=True)
    NOMBRE = fields.String(required=True)
    APELLIDO = fields.String(allow_none=True)
    EDAD = fields.Integer(required=True, validate=validate.Range(min=18, max=100))
    CORREO = fields.String(required=True, validate=validate.Email())
    PASSWORD = fields.String(required=True, validate=validate.Length(min=1, max=20)) 

class UsuarioSchemaLogin(ma.SQLAlchemyAutoSchema):
    CORREO = fields.String(required=True, validate=validate.Email())
    PASSWORD = fields.String(required=True, validate=validate.Length(min=1, max=20))