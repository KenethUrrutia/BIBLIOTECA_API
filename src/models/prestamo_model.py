from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
import datetime

class PrestamoModel(db.Model):
    __tablename__ = 'PRESTAMO'
    IDUSUARIO: Mapped[int] = mapped_column(nullable=False)
    IDLIBRO: Mapped[int] = mapped_column(nullable=False)
    IDPRESTAMO: Mapped[int] = mapped_column(primary_key=True)
    FECHA_PRESTAMO: Mapped[datetime.datetime] = mapped_column(nullable=False)
    FECHA_DEVOLUCION: Mapped[datetime.datetime] = mapped_column(nullable=True)
    ESTADO: Mapped[str] = mapped_column(nullable=True)
    IDESTADO: Mapped[int] = mapped_column(nullable=False)
