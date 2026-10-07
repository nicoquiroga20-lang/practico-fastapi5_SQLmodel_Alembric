from .libros import (
    LibroBase,
    LibroCreate,
    LibroRead,
    LibroUpdate,
    LibroSchema,
    LibroReadWithProveedor,
)
from .proveedor import (
    ProveedorBase,
    ProveedorCreate,
    ProveedorRead,
    ProveedorUpdate,
    ProveedorReadWithLibros,
)

__all__ = [
    "LibroBase",
    "LibroCreate",
    "LibroRead",
    "LibroUpdate",
    "LibroSchema",
    "LibroReadWithProveedor",
    "ProveedorBase",
    "ProveedorCreate",
    "ProveedorRead",
    "ProveedorUpdate",
    "ProveedorReadWithLibros",
]
