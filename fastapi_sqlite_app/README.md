# FastAPI + SQLite + SQLAlchemy (Starter)

API CRUD básica con persistencia en SQLite usando SQLAlchemy 2.x y Pydantic 2.

## Requisitos
- Python 3.10+
- VS Code + extensión *Python*

## Instalación (Windows)
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
# Crear tablas
python -m app.init_db
# Ejecutar servidor
uvicorn app.app:app --reload
```
Abrir: <http://127.0.0.1:8000/docs>

## Endpoints
- `GET    /items` — lista paginada
- `GET    /items/{id}` — detalle
- `POST   /items` — crear
- `PUT    /items/{id}` — actualizar
- `DELETE /items/{id}` — eliminar

## Estructura
```
fastapi_sqlite_app/
  app/
    app.py
    database.py
    models.py
    schemas.py
    crud.py
    init_db.py
  .vscode/
    launch.json
  requirements.txt
  README.md
```

## Pruebas rápidas con `curl`
```bash
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d "{"name":"Mouse","price":299.99,"description":"Gamer"}"
curl http://127.0.0.1:8000/items
```
