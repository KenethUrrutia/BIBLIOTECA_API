from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
from src.models.libro_model import LibroModel
from src.models.estado_model import EstadoModel
import datetime

class PrestamoModel(db.Model):
    __tablename__ = 'PRESTAMO'
    IDUSUARIO: Mapped[int] = mapped_column(ForeignKey("USUARIO.IDUSUARIO"), nullable=False)
    IDLIBRO: Mapped[int] = mapped_column(ForeignKey("LIBRO.IDLIBRO"), nullable=False)
    IDPRESTAMO: Mapped[int] = mapped_column(primary_key=True)
    FECHA_PRESTAMO: Mapped[datetime.datetime] = mapped_column(nullable=False)
    FECHA_DEVOLUCION: Mapped[datetime.datetime] = mapped_column(nullable=True)
    ESTADO: Mapped[str] = mapped_column(nullable=True)
    IDESTADO: Mapped[int] = mapped_column(ForeignKey("ESTADO.IDESTADO"),nullable=False)

    USUARIO: Mapped[List["UsuarioModel"]] = relationship(back_populates='PRESTAMO')
    LIBROS: Mapped[List[LibroModel]] = relationship(back_populates='PRESTAMO')
    ESTADO_LIBRO: Mapped[EstadoModel] = relationship(back_populates='PRESTAMO')

