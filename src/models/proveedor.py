from typing import TYPE_CHECKING, Optional, List
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .libro import Libro

class Proveedor(SQLModel, table=True):
    __tablename__ = "proveedor"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre_proveedor: str = Field(index=True, max_length=100)
    telefono_proveedor: str = Field(max_length=50)

    # Relación 1 a N con Libro
    libros: List["Libro"] = Relationship(back_populates="proveedor")
