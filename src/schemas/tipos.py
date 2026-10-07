# Aduana de tipos de datos para los modelos de Pydantic que se usan en los endpoints de FastAPI
from typing import Annotated
from pydantic import Field

# Reglas de validacion (reutilizables) para los modelos de Pydantic que se usan en los endpoints de FastAPI
IdPositivo = Annotated[int, Field(gt=0, description="ID mayor a cero")]
TextoCorto = Annotated[str, Field(min_length=1, max_length=80, description="Texto de maximo 80 caracteres")]
PrecioValid = Annotated[float, Field(gt=0, lt=1000000,description="Precio en pesos hasta $1.000.000")]
BoolDisponible = Annotated[bool,Field(default=True,description="El libro esta disponile?")]