from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
import datetime

from src.models.genero_model import GeneroModel

class LibroModel(db.Model):
    __tablename__ = 'LIBRO'
    IDLIBRO: Mapped[int] = mapped_column( primary_key=True)
    TITULO: Mapped[str] = mapped_column(nullable=False)
    AUTOR: Mapped[str] = mapped_column(nullable=True)
    ANIO_PUBLICACION: Mapped[datetime.date] = mapped_column(nullable=True)
    IDGENERO: Mapped[int] = mapped_column(ForeignKey("GENERO.IDGENERO"), nullable=False)

    GENERO: Mapped[GeneroModel] = relationship(back_populates='LIBROS')
    PRESTAMO: Mapped[List["PrestamoModel"]] = relationship(back_populates='LIBROS')


    
