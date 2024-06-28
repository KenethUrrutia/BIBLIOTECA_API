from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column

class EstadoModel(db.Model):
    __tablename__ = 'ESTADO'
    IDESTADO: Mapped[int] = mapped_column( primary_key=True)
    NOMBRE: Mapped[str] = mapped_column(nullable=False)