from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
import datetime

class LibroModel(db.Model):
    __tablename__ = 'LIBRO'
    IDLIBRO: Mapped[int] = mapped_column( primary_key=True)
    TITULO: Mapped[str] = mapped_column(nullable=False)
    AUTOR: Mapped[str] = mapped_column(nullable=True)
    ANIO_PUBLICACION: Mapped[datetime.date] = mapped_column(nullable=True)
    IDGENERO: Mapped[int] = mapped_column(nullable=False)
