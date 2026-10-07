# Conexion a la base de datos con SQLModel
from pathlib import Path
from sqlmodel import SQLModel, create_engine, Session

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "base_de_datos.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

def get_db():
    """Dependencia para inyectar la sesion de la db a los endpoints de FastAPI."""
    with Session(engine) as db:
        yield db

