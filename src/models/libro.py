from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .proveedor import Proveedor

class Libro(SQLModel, table=True):
    __tablename__ = "libro"

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str = Field(max_length=150)
    autor: str = Field(max_length=100)
    precio: float = Field(gt=0)
    disponible: bool = Field(default=True)

    # Clave foránea referenciando a la tabla proveedor
    proveedor_id: Optional[int] = Field(default=None, foreign_key="proveedor.id")

    # Relación N a 1 con Proveedor
    proveedor: Optional["Proveedor"] = Relationship(back_populates="libros")
