from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
#from src.models.libro_model import LibroModel

class GeneroModel(db.Model):
    __tablename__ = 'GENERO'
    IDGENERO: Mapped[int] = mapped_column( primary_key=True)
    NOMBRE: Mapped[str] = mapped_column(nullable=False)

    LIBROS: Mapped[List["LibroModel"]] = relationship(back_populates='GENERO')

