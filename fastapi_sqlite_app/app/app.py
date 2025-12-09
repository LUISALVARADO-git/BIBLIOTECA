from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, crud, models
from .auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user

app = FastAPI(title="Demo FastAPI + SQLite", version="1.0.0")


@app.post("/token", response_model=schemas.Token, tags=["auth"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nombre de usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/", tags=["root"])
def root():
    return {"message": "API lista. Visita /docs para probar."}


# -------------------------
# Endpoints para Items (ya existentes)
# -------------------------

@app.get("/items", response_model=list[schemas.ItemOut], tags=["items"])
def list_items(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    return crud.list_items(db, skip=skip, limit=limit)


@app.get("/items/{item_id}", response_model=schemas.ItemOut, tags=["items"])
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item


@app.post("/items", response_model=schemas.ItemOut, status_code=201, tags=["items"])
def create_item(body: schemas.ItemCreate, db: Session = Depends(get_db)):
    item = crud.create_item(db, body)
    return item


@app.put("/items/{item_id}", response_model=schemas.ItemOut, tags=["items"])
def update_item(item_id: int, body: schemas.ItemUpdate, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return crud.update_item(db, item, body)


@app.delete("/items/{item_id}", status_code=204, tags=["items"])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    crud.delete_item(db, item)
    return None


# -------------------------
# CRUD completo para Alumnos
# -------------------------

@app.get("/alumnos", response_model=list[schemas.AlumnoOut], tags=["alumnos"])
def list_alumnos(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return crud.list_alumnos(db, skip=skip, limit=limit)


@app.get("/alumnos/{alumno_id}", response_model=schemas.AlumnoOut, tags=["alumnos"])
def get_alumno(alumno_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    alumno = crud.get_alumno(db, alumno_id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno


@app.post("/alumnos", response_model=schemas.AlumnoOut, status_code=201, tags=["alumnos"])
def create_alumno(body: schemas.AlumnoCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    alumno = crud.create_alumno(db, body)
    return alumno


@app.put("/alumnos/{alumno_id}", response_model=schemas.AlumnoOut, tags=["alumnos"])
def update_alumno(alumno_id: int, body: schemas.AlumnoUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    alumno = crud.get_alumno(db, alumno_id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return crud.update_alumno(db, alumno, body)


@app.delete("/alumnos/{alumno_id}", status_code=204, tags=["alumnos"])
def delete_alumno(alumno_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    alumno = crud.get_alumno(db, alumno_id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    crud.delete_alumno(db, alumno)
    return None


# -------------------------
# CRUD completo para Clase
# -------------------------

@app.get("/clases", response_model=list[schemas.ClaseOut], tags=["clases"])
def list_clases(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return crud.list_clases(db, skip=skip, limit=limit)


@app.get("/clases/{clase_id}", response_model=schemas.ClaseOut, tags=["clases"])
def get_clase(clase_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    clase = crud.get_clase(db, clase_id)
    if not clase:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
    return clase


@app.post("/clases", response_model=schemas.ClaseOut, status_code=201, tags=["clases"])
def create_clase(body: schemas.ClaseCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    clase = crud.create_clase(db, body)
    return clase


@app.put("/clases/{clase_id}", response_model=schemas.ClaseOut, tags=["clases"])
def update_clase(clase_id: int, body: schemas.ClaseUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    clase = crud.get_clase(db, clase_id)
    if not clase:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
    return crud.update_clase(db, clase, body)


@app.delete("/clases/{clase_id}", status_code=204, tags=["clases"])
def delete_clase(clase_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    clase = crud.get_clase(db, clase_id)
    if not clase:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
    crud.delete_clase(db, clase)
    return None


# -------------------------
# CRUD completo para Notas
# -------------------------

@app.get("/notas", response_model=list[schemas.NotaOut], tags=["notas"])
def list_notas(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return crud.list_notas(db, skip=skip, limit=limit)


@app.get("/notas/{nota_id}", response_model=schemas.NotaOut, tags=["notas"])
def get_nota(nota_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    nota = crud.get_nota(db, nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota


@app.post("/notas", response_model=schemas.NotaOut, status_code=201, tags=["notas"])
def create_nota(body: schemas.NotaCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Aquí podrías validar que alumno_id y clase_id existan antes de crear
    nota = crud.create_nota(db, body)
    return nota


@app.put("/notas/{nota_id}", response_model=schemas.NotaOut, tags=["notas"])
def update_nota(nota_id: int, body: schemas.NotaUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    nota = crud.get_nota(db, nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return crud.update_nota(db, nota, body)


@app.delete("/notas/{nota_id}", status_code=204, tags=["notas"])
def delete_nota(nota_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    nota = crud.get_nota(db, nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    crud.delete_nota(db, nota)
    return None
