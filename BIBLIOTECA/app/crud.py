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


# -------------------------
# CRUD para Biblioteca
# -------------------------


def get_usuario(db: Session, usuario_id: int) -> models.Usuario | None:
    return db.get(models.Usuario, usuario_id)


def list_usuarios(db: Session, skip: int = 0, limit: int = 100) -> list[models.Usuario]:
    stmt = select(models.Usuario).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_usuario(db: Session, data: schemas.UsuarioCreate) -> models.Usuario:
    usuario = models.Usuario(**data.model_dump())
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def update_usuario(db: Session, usuario: models.Usuario, data: schemas.UsuarioUpdate) -> models.Usuario:
    for k, v in data.model_dump().items():
        setattr(usuario, k, v)
    db.commit()
    db.refresh(usuario)
    return usuario


def delete_usuario(db: Session, usuario: models.Usuario) -> None:
    db.delete(usuario)
    db.commit()


def get_autor(db: Session, autor_id: int) -> models.Autor | None:
    return db.get(models.Autor, autor_id)


def list_autores(db: Session, skip: int = 0, limit: int = 100) -> list[models.Autor]:
    stmt = select(models.Autor).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_autor(db: Session, data: schemas.AutorCreate) -> models.Autor:
    autor = models.Autor(**data.model_dump())
    db.add(autor)
    db.commit()
    db.refresh(autor)
    return autor


def update_autor(db: Session, autor: models.Autor, data: schemas.AutorUpdate) -> models.Autor:
    for k, v in data.model_dump().items():
        setattr(autor, k, v)
    db.commit()
    db.refresh(autor)
    return autor


def delete_autor(db: Session, autor: models.Autor) -> None:
    db.delete(autor)
    db.commit()


def get_categoria(db: Session, categoria_id: int) -> models.Categoria | None:
    return db.get(models.Categoria, categoria_id)


def list_categorias(db: Session, skip: int = 0, limit: int = 100) -> list[models.Categoria]:
    stmt = select(models.Categoria).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_categoria(db: Session, data: schemas.CategoriaCreate) -> models.Categoria:
    categoria = models.Categoria(**data.model_dump())
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria


def update_categoria(db: Session, categoria: models.Categoria, data: schemas.CategoriaUpdate) -> models.Categoria:
    for k, v in data.model_dump().items():
        setattr(categoria, k, v)
    db.commit()
    db.refresh(categoria)
    return categoria


def delete_categoria(db: Session, categoria: models.Categoria) -> None:
    db.delete(categoria)
    db.commit()


def get_lenguaje(db: Session, lenguaje_id: int) -> models.Lenguaje | None:
    return db.get(models.Lenguaje, lenguaje_id)


def list_lenguajes(db: Session, skip: int = 0, limit: int = 100) -> list[models.Lenguaje]:
    stmt = select(models.Lenguaje).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_lenguaje(db: Session, data: schemas.LenguajeCreate) -> models.Lenguaje:
    lenguaje = models.Lenguaje(**data.model_dump())
    db.add(lenguaje)
    db.commit()
    db.refresh(lenguaje)
    return lenguaje


def update_lenguaje(db: Session, lenguaje: models.Lenguaje, data: schemas.LenguajeUpdate) -> models.Lenguaje:
    for k, v in data.model_dump().items():
        setattr(lenguaje, k, v)
    db.commit()
    db.refresh(lenguaje)
    return lenguaje


def delete_lenguaje(db: Session, lenguaje: models.Lenguaje) -> None:
    db.delete(lenguaje)
    db.commit()


def get_libro(db: Session, libro_id: int) -> models.Libro | None:
    return db.get(models.Libro, libro_id)


def list_libros(db: Session, skip: int = 0, limit: int = 100) -> list[models.Libro]:
    stmt = select(models.Libro).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_libro(db: Session, data: schemas.LibroCreate) -> models.Libro:
    libro = models.Libro(**data.model_dump())
    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro


def update_libro(db: Session, libro: models.Libro, data: schemas.LibroUpdate) -> models.Libro:
    for k, v in data.model_dump().items():
        setattr(libro, k, v)
    db.commit()
    db.refresh(libro)
    return libro


def delete_libro(db: Session, libro: models.Libro) -> None:
    db.delete(libro)
    db.commit()


def get_tema(db: Session, tema_id: int) -> models.Tema | None:
    return db.get(models.Tema, tema_id)


def list_temas(db: Session, skip: int = 0, limit: int = 100) -> list[models.Tema]:
    stmt = select(models.Tema).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_tema(db: Session, data: schemas.TemaCreate) -> models.Tema:
    tema = models.Tema(**data.model_dump())
    db.add(tema)
    db.commit()
    db.refresh(tema)
    return tema


def update_tema(db: Session, tema: models.Tema, data: schemas.TemaUpdate) -> models.Tema:
    for k, v in data.model_dump().items():
        setattr(tema, k, v)
    db.commit()
    db.refresh(tema)
    return tema


def delete_tema(db: Session, tema: models.Tema) -> None:
    db.delete(tema)
    db.commit()


def get_descripcion(db: Session, descripcion_id: int) -> models.Descripcion | None:
    return db.get(models.Descripcion, descripcion_id)


def list_descripciones(db: Session, skip: int = 0, limit: int = 100) -> list[models.Descripcion]:
    stmt = select(models.Descripcion).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_descripcion(db: Session, data: schemas.DescripcionCreate) -> models.Descripcion:
    descripcion = models.Descripcion(**data.model_dump())
    db.add(descripcion)
    db.commit()
    db.refresh(descripcion)
    return descripcion


def update_descripcion(db: Session, descripcion: models.Descripcion, data: schemas.DescripcionUpdate) -> models.Descripcion:
    for k, v in data.model_dump().items():
        setattr(descripcion, k, v)
    db.commit()
    db.refresh(descripcion)
    return descripcion


def delete_descripcion(db: Session, descripcion: models.Descripcion) -> None:
    db.delete(descripcion)
    db.commit()


def get_inventario(db: Session, inventario_id: int) -> models.Inventario | None:
    return db.get(models.Inventario, inventario_id)


def list_inventario(db: Session, skip: int = 0, limit: int = 100) -> list[models.Inventario]:
    stmt = select(models.Inventario).offset(skip).limit(limit)
    return list(db.execute(stmt).scalars())


def create_inventario(db: Session, data: schemas.InventarioCreate) -> models.Inventario:
    inv = models.Inventario(**data.model_dump())
    db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv


def update_inventario(db: Session, inv: models.Inventario, data: schemas.InventarioUpdate) -> models.Inventario:
    for k, v in data.model_dump().items():
        setattr(inv, k, v)
    db.commit()
    db.refresh(inv)
    return inv


def delete_inventario(db: Session, inv: models.Inventario) -> None:
    db.delete(inv)
    db.commit()
