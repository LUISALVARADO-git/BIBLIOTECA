from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas


# -------------------------
# CRUD para Item (ya existente)
# -------------------------

def get_item(db: Session, item_id: int) -> models.Item | None:
    return db.get(models.Item, item_id)


def list_items(db: Session, skip: int = 0, limit: int = 100) -> list[models.Item]:
    stmt = select(models.Item).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_item(db: Session, data: schemas.ItemCreate) -> models.Item:
    item = models.Item(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item: models.Item, data: schemas.ItemUpdate) -> models.Item:
    for k, v in data.model_dump().items():
        setattr(item, k, v)
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item: models.Item) -> None:
    db.delete(item)
    db.commit()


# -------------------------
# CRUD para Alumnos
# -------------------------

def get_alumno(db: Session, alumno_id: int) -> models.Alumno | None:
    return db.get(models.Alumno, alumno_id)


def list_alumnos(db: Session, skip: int = 0, limit: int = 100) -> list[models.Alumno]:
    stmt = select(models.Alumno).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_alumno(db: Session, data: schemas.AlumnoCreate) -> models.Alumno:
    alumno = models.Alumno(**data.model_dump())
    db.add(alumno)
    db.commit()
    db.refresh(alumno)
    return alumno


def update_alumno(db: Session, alumno: models.Alumno, data: schemas.AlumnoUpdate) -> models.Alumno:
    for k, v in data.model_dump().items():
        setattr(alumno, k, v)
    db.commit()
    db.refresh(alumno)
    return alumno


def delete_alumno(db: Session, alumno: models.Alumno) -> None:
    db.delete(alumno)
    db.commit()


# -------------------------
# CRUD para Clase
# -------------------------

def get_clase(db: Session, clase_id: int) -> models.Clase | None:
    return db.get(models.Clase, clase_id)


def list_clases(db: Session, skip: int = 0, limit: int = 100) -> list[models.Clase]:
    stmt = select(models.Clase).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_clase(db: Session, data: schemas.ClaseCreate) -> models.Clase:
    clase = models.Clase(**data.model_dump())
    db.add(clase)
    db.commit()
    db.refresh(clase)
    return clase


def update_clase(db: Session, clase: models.Clase, data: schemas.ClaseUpdate) -> models.Clase:
    for k, v in data.model_dump().items():
        setattr(clase, k, v)
    db.commit()
    db.refresh(clase)
    return clase


def delete_clase(db: Session, clase: models.Clase) -> None:
    db.delete(clase)
    db.commit()


# -------------------------
# CRUD para Notas
# -------------------------

def get_nota(db: Session, nota_id: int) -> models.Nota | None:
    return db.get(models.Nota, nota_id)


def list_notas(db: Session, skip: int = 0, limit: int = 100) -> list[models.Nota]:
    stmt = select(models.Nota).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_nota(db: Session, data: schemas.NotaCreate) -> models.Nota:
    nota = models.Nota(**data.model_dump())
    db.add(nota)
    db.commit()
    db.refresh(nota)
    return nota


def update_nota(db: Session, nota: models.Nota, data: schemas.NotaUpdate) -> models.Nota:
    for k, v in data.model_dump().items():
        setattr(nota, k, v)
    db.commit()
    db.refresh(nota)
    return nota


def delete_nota(db: Session, nota: models.Nota) -> None:
    db.delete(nota)
    db.commit()
