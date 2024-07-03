from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer
from .prestamo_model import PrestamoModel
from typing import List

class UsuarioModel(db.Model):
    __tablename__ = 'USUARIO'
    IDUSUARIO: Mapped[int] = mapped_column( primary_key=True)
    NOMBRE: Mapped[str] = mapped_column(nullable=False)
    APELLIDO: Mapped[str] = mapped_column(nullable=True)
    EDAD: Mapped[int] = mapped_column(nullable=False)
    CORREO: Mapped[str] = mapped_column(nullable=False)
    PASSWORD: Mapped[str] = mapped_column(nullable=False)

    PRESTAMO: Mapped[List[PrestamoModel]] = relationship(back_populates='USUARIO')
