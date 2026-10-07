from typing import Optional
from sqlmodel import SQLModel, Field
from .tipos import IdPositivo
from .proveedor import ProveedorRead, ProveedorReadWithLibros

class LibroBase(SQLModel):
    titulo: str = Field(min_length=1, max_length=150, description="Título del libro")
    autor: str = Field(min_length=1, max_length=100, description="Autor del libro")
    precio: float = Field(gt=0, lt=1000000, description="Precio en pesos hasta $1.000.000")
    disponible: bool = Field(default=True, description="El libro está disponible?")
    proveedor_id: Optional[int] = Field(default=None, description="ID del proveedor asociado")

class LibroCreate(LibroBase):
    pass

class LibroRead(LibroBase):
    id: int

class LibroUpdate(SQLModel):
    titulo: Optional[str] = Field(default=None, min_length=1, max_length=150)
    autor: Optional[str] = Field(default=None, min_length=1, max_length=100)
    precio: Optional[float] = Field(default=None, gt=0, lt=1000000)
    disponible: Optional[bool] = Field(default=None)
    proveedor_id: Optional[int] = Field(default=None)

# Alias para compatibilidad con código previo
LibroSchema = LibroRead

# Schema anidado: Libro con datos de su Proveedor
class LibroReadWithProveedor(LibroRead):
    proveedor: Optional[ProveedorRead] = None

# Reconstruir schemas anidados para resolver referencias forward
ProveedorReadWithLibros.model_rebuild()
LibroReadWithProveedor.model_rebuild()