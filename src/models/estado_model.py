from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
# from src.models.prestamo_model import PrestamoModel

class EstadoModel(db.Model):
    __tablename__ = 'ESTADO'
    IDESTADO: Mapped[int] = mapped_column( primary_key=True)
    NOMBRE: Mapped[str] = mapped_column(nullable=False)

    PRESTAMO: Mapped[List["PrestamoModel"]] = relationship(back_populates='ESTADO_PRESTAMO')