# practico-fastapi5_SQLmodel_Alembric

Proyecto base con **FastAPI + SQLModel** y **Alembic** para migraciones de base de datos.

## Requisitos

- Python 3.10+

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar migraciones

```bash
alembic upgrade head
```

## Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

## Endpoint de prueba

- `GET /health` → `{"ok": true}`
