# Endpoints de FastAPI para el manejo de Libros con SQLModel
from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select

from database import get_db
from models.libro import Libro
from models.proveedor import Proveedor
from schemas.libros import (
    LibroCreate,
    LibroRead,
    LibroUpdate,
    LibroReadWithProveedor,
)
from schemas.tipos import IdPositivo

libros_router = APIRouter(prefix="/libros", tags=["Libros"])

@libros_router.get("/", response_model=List[LibroRead], status_code=status.HTTP_200_OK)
async def get_libros(db: Session = Depends(get_db)):
    """Listar todos los libros."""
    libros = db.exec(select(Libro)).all()
    return libros

@libros_router.get("/{id}", response_model=LibroReadWithProveedor, status_code=status.HTTP_200_OK)
async def get_by_id_libro(id: IdPositivo, db: Session = Depends(get_db)):
    """Obtener un libro por ID, incluyendo la información de su Proveedor (datos anidados)."""
    libro = db.get(Libro, id)
    if libro is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")
    return libro

@libros_router.post("/", response_model=LibroRead, status_code=status.HTTP_201_CREATED)
async def post_libro(libro_nuevo: LibroCreate, db: Session = Depends(get_db)):
    """Crear un nuevo libro, opcionalmente asignando un proveedor_id."""
    if libro_nuevo.proveedor_id is not None:
        proveedor = db.get(Proveedor, libro_nuevo.proveedor_id)
        if not proveedor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El proveedor con ID {libro_nuevo.proveedor_id} no existe",
            )

    libro_db = Libro.model_validate(libro_nuevo)
    db.add(libro_db)
    db.commit()
    db.refresh(libro_db)
    return libro_db

@libros_router.put("/{id}", response_model=LibroRead, status_code=status.HTTP_200_OK)
async def update_libro(id: IdPositivo, libro_actualizado: LibroUpdate, db: Session = Depends(get_db)):
    """Actualizar datos de un libro existente."""
    libro_db = db.get(Libro, id)
    if libro_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")

    update_data = libro_actualizado.model_dump(exclude_unset=True)
    if "proveedor_id" in update_data and update_data["proveedor_id"] is not None:
        proveedor = db.get(Proveedor, update_data["proveedor_id"])
        if not proveedor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El proveedor con ID {update_data['proveedor_id']} no existe",
            )

    for key, value in update_data.items():
        setattr(libro_db, key, value)

    db.add(libro_db)
    db.commit()
    db.refresh(libro_db)
    return libro_db

@libros_router.delete("/{id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_libro(
    id: IdPositivo,
    db: Session = Depends(get_db),
    logico: Annotated[
        bool,
        Query(description="Si es True solo marca como no disponible, si es False elimina de forma permanente"),
    ] = False,
):
    """Eliminar un libro (físico o lógico)."""
    libro_db = db.get(Libro, id)
    if libro_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Libro no encontrado")

    if logico:
        libro_db.disponible = False
        db.add(libro_db)
        db.commit()
        return {"Mensaje": f"Libro {libro_db.titulo} se ha eliminado momentáneamente de forma exitosa"}
    else:
        db.delete(libro_db)
        db.commit()
        return {"Alerta": f"Libro {libro_db.titulo} se ha eliminado permanentemente de la base de datos de forma exitosa"}