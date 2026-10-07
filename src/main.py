from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.libros import libros_router
from routers.proveedores import proveedores_router

app = FastAPI(
    title="Gestion de Libros y Proveedores",
    description="API con SQLModel y Alembic para Libros y Proveedores",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(libros_router)
app.include_router(proveedores_router)
