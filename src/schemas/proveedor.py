from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field

if TYPE_CHECKING:
    from .libros import LibroRead

class ProveedorBase(SQLModel):
    nombre_proveedor: str = Field(min_length=1, max_length=100, description="Nombre del proveedor")
    telefono_proveedor: str = Field(min_length=3, max_length=50, description="Telefono del proveedor")

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorRead(ProveedorBase):
    id: int

class ProveedorUpdate(SQLModel):
    nombre_proveedor: Optional[str] = Field(default=None, min_length=1, max_length=100)
    telefono_proveedor: Optional[str] = Field(default=None, min_length=3, max_length=50)

# Schema anidado: Proveedor con la lista de libros asociados
class ProveedorReadWithLibros(ProveedorRead):
    libros: List["LibroRead"] = []
