from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from database import get_db
from models.proveedor import Proveedor
from schemas.proveedor import (
    ProveedorCreate,
    ProveedorRead,
    ProveedorUpdate,
    ProveedorReadWithLibros,
)
from schemas.tipos import IdPositivo

proveedores_router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

@proveedores_router.get("/", response_model=List[ProveedorRead], status_code=status.HTTP_200_OK)
async def get_proveedores(db: Session = Depends(get_db)):
    """Listar todos los proveedores registrados."""
    proveedores = db.exec(select(Proveedor)).all()
    return proveedores

@proveedores_router.get("/{id}", response_model=ProveedorReadWithLibros, status_code=status.HTTP_200_OK)
async def get_proveedor_by_id(id: IdPositivo, db: Session = Depends(get_db)):
    """Obtener un proveedor por su ID, incluyendo la lista de libros asociados (datos anidados)."""
    proveedor = db.get(Proveedor, id)
    if proveedor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")
    return proveedor

@proveedores_router.post("/", response_model=ProveedorRead, status_code=status.HTTP_201_CREATED)
async def create_proveedor(proveedor_in: ProveedorCreate, db: Session = Depends(get_db)):
    """Registrar un nuevo proveedor."""
    proveedor = Proveedor.model_validate(proveedor_in)
    db.add(proveedor)
    db.commit()
    db.refresh(proveedor)
    return proveedor

@proveedores_router.put("/{id}", response_model=ProveedorRead, status_code=status.HTTP_200_OK)
async def update_proveedor(id: IdPositivo, proveedor_in: ProveedorUpdate, db: Session = Depends(get_db)):
    """Actualizar datos de un proveedor existente."""
    proveedor = db.get(Proveedor, id)
    if proveedor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")

    update_data = proveedor_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(proveedor, key, value)

    db.add(proveedor)
    db.commit()
    db.refresh(proveedor)
    return proveedor

@proveedores_router.delete("/{id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_proveedor(id: IdPositivo, db: Session = Depends(get_db)):
    """Eliminar un proveedor."""
    proveedor = db.get(Proveedor, id)
    if proveedor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor no encontrado")

    db.delete(proveedor)
    db.commit()
    return {"mensaje": f"Proveedor '{proveedor.nombre_proveedor}' eliminado exitosamente"}
