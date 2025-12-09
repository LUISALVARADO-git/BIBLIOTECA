from fastapi import FastAPI, Depends, HTTPException, Query, Security
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, crud, models


API_KEY_NAME = "X-API-Token"
API_KEY = "MI_TOKEN_SUPER_SECRETO"  # cámbialo por un valor fuerte y guarda solo en entorno

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def get_api_key(api_key: str | None = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    raise HTTPException(status_code=403, detail="No autorizado: API Key inválida o ausente")


app = FastAPI(
    title="Biblioteca Virtual",
    version="1.0.0",
    description="API de Biblioteca protegida con API Key simple en header X-API-Token",
    dependencies=[Depends(get_api_key)],
)


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
# CRUD completo para Biblioteca
# -------------------------


@app.get("/usuarios", response_model=list[schemas.UsuarioOut], tags=["usuarios"])
def list_usuarios(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    return crud.list_usuarios(db, skip=skip, limit=limit)


@app.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioOut, tags=["usuarios"])
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@app.post("/usuarios", response_model=schemas.UsuarioOut, status_code=201, tags=["usuarios"])
def create_usuario(body: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    usuario = crud.create_usuario(db, body)
    return usuario


@app.put("/usuarios/{usuario_id}", response_model=schemas.UsuarioOut, tags=["usuarios"])
def update_usuario(usuario_id: int, body: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return crud.update_usuario(db, usuario, body)


@app.delete("/usuarios/{usuario_id}", status_code=204, tags=["usuarios"])
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    crud.delete_usuario(db, usuario)
    return None


@app.get("/autores", response_model=list[schemas.AutorOut], tags=["autores"])
def list_autores(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    return crud.list_autores(db, skip=skip, limit=limit)


@app.get("/autores/{autor_id}", response_model=schemas.AutorOut, tags=["autores"])
def get_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = crud.get_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor


@app.post("/autores", response_model=schemas.AutorOut, status_code=201, tags=["autores"])
def create_autor(body: schemas.AutorCreate, db: Session = Depends(get_db)):
    autor = crud.create_autor(db, body)
    return autor


@app.put("/autores/{autor_id}", response_model=schemas.AutorOut, tags=["autores"])
def update_autor(autor_id: int, body: schemas.AutorUpdate, db: Session = Depends(get_db)):
    autor = crud.get_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return crud.update_autor(db, autor, body)


@app.delete("/autores/{autor_id}", status_code=204, tags=["autores"])
def delete_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = crud.get_autor(db, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    crud.delete_autor(db, autor)
    return None


@app.get("/categorias", response_model=list[schemas.CategoriaOut], tags=["categorias"])
def list_categorias(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    return crud.list_categorias(db, skip=skip, limit=limit)


@app.get("/categorias/{categoria_id}", response_model=schemas.CategoriaOut, tags=["categorias"])
def get_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.get_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria


@app.post("/categorias", response_model=schemas.CategoriaOut, status_code=201, tags=["categorias"])
def create_categoria(body: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    categoria = crud.create_categoria(db, body)
    return categoria


@app.put("/categorias/{categoria_id}", response_model=schemas.CategoriaOut, tags=["categorias"])
def update_categoria(categoria_id: int, body: schemas.CategoriaUpdate, db: Session = Depends(get_db)):
    categoria = crud.get_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return crud.update_categoria(db, categoria, body)


@app.delete("/categorias/{categoria_id}", status_code=204, tags=["categorias"])
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.get_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    crud.delete_categoria(db, categoria)
    return None


@app.get("/lenguajes", response_model=list[schemas.LenguajeOut], tags=["lenguajes"])
def list_lenguajes(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    return crud.list_lenguajes(db, skip=skip, limit=limit)


@app.get("/lenguajes/{lenguaje_id}", response_model=schemas.LenguajeOut, tags=["lenguajes"])
def get_lenguaje(lenguaje_id: int, db: Session = Depends(get_db)):
    lenguaje = crud.get_lenguaje(db, lenguaje_id)
    if not lenguaje:
        raise HTTPException(status_code=404, detail="Lenguaje no encontrado")
    return lenguaje


@app.post("/lenguajes", response_model=schemas.LenguajeOut, status_code=201, tags=["lenguajes"])
def create_lenguaje(body: schemas.LenguajeCreate, db: Session = Depends(get_db)):
    lenguaje = crud.create_lenguaje(db, body)
    return lenguaje


@app.put("/lenguajes/{lenguaje_id}", response_model=schemas.LenguajeOut, tags=["lenguajes"])
def update_lenguaje(lenguaje_id: int, body: schemas.LenguajeUpdate, db: Session = Depends(get_db)):
    lenguaje = crud.get_lenguaje(db, lenguaje_id)
    if not lenguaje:
        raise HTTPException(status_code=404, detail="Lenguaje no encontrado")
    return crud.update_lenguaje(db, lenguaje, body)


@app.delete("/lenguajes/{lenguaje_id}", status_code=204, tags=["lenguajes"])
def delete_lenguaje(lenguaje_id: int, db: Session = Depends(get_db)):
    lenguaje = crud.get_lenguaje(db, lenguaje_id)
    if not lenguaje:
        raise HTTPException(status_code=404, detail="Lenguaje no encontrado")
    crud.delete_lenguaje(db, lenguaje)
    return None


@app.get("/libros", response_model=list[schemas.LibroOut], tags=["libros"])
def list_libros(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    return crud.list_libros(db, skip=skip, limit=limit)


@app.get("/libros/{libro_id}", response_model=schemas.LibroOut, tags=["libros"])
def get_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = crud.get_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


@app.post("/libros", response_model=schemas.LibroOut, status_code=201, tags=["libros"])
def create_libro(body: schemas.LibroCreate, db: Session = Depends(get_db)):
    libro = crud.create_libro(db, body)
    return libro


@app.put("/libros/{libro_id}", response_model=schemas.LibroOut, tags=["libros"])
def update_libro(libro_id: int, body: schemas.LibroUpdate, db: Session = Depends(get_db)):
    libro = crud.get_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return crud.update_libro(db, libro, body)


@app.delete("/libros/{libro_id}", status_code=204, tags=["libros"])
def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = crud.get_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    crud.delete_libro(db, libro)
    return None


@app.get("/temas", response_model=list[schemas.TemaOut], tags=["temas"])
def list_temas(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    return crud.list_temas(db, skip=skip, limit=limit)


@app.get("/temas/{tema_id}", response_model=schemas.TemaOut, tags=["temas"])
def get_tema(tema_id: int, db: Session = Depends(get_db)):
    tema = crud.get_tema(db, tema_id)
    if not tema:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    return tema


@app.post("/temas", response_model=schemas.TemaOut, status_code=201, tags=["temas"])
def create_tema(body: schemas.TemaCreate, db: Session = Depends(get_db)):
    tema = crud.create_tema(db, body)
    return tema


@app.put("/temas/{tema_id}", response_model=schemas.TemaOut, tags=["temas"])
def update_tema(tema_id: int, body: schemas.TemaUpdate, db: Session = Depends(get_db)):
    tema = crud.get_tema(db, tema_id)
    if not tema:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    return crud.update_tema(db, tema, body)


@app.delete("/temas/{tema_id}", status_code=204, tags=["temas"])
def delete_tema(tema_id: int, db: Session = Depends(get_db)):
    tema = crud.get_tema(db, tema_id)
    if not tema:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    crud.delete_tema(db, tema)
    return None


@app.get("/descripciones", response_model=list[schemas.DescripcionOut], tags=["descripciones"])
def list_descripciones(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    return crud.list_descripciones(db, skip=skip, limit=limit)


@app.get("/descripciones/{descripcion_id}", response_model=schemas.DescripcionOut, tags=["descripciones"])
def get_descripcion(descripcion_id: int, db: Session = Depends(get_db)):
    descripcion = crud.get_descripcion(db, descripcion_id)
    if not descripcion:
        raise HTTPException(status_code=404, detail="Descripción no encontrada")
    return descripcion


@app.post("/descripciones", response_model=schemas.DescripcionOut, status_code=201, tags=["descripciones"])
def create_descripcion(body: schemas.DescripcionCreate, db: Session = Depends(get_db)):
    descripcion = crud.create_descripcion(db, body)
    return descripcion


@app.put("/descripciones/{descripcion_id}", response_model=schemas.DescripcionOut, tags=["descripciones"])
def update_descripcion(descripcion_id: int, body: schemas.DescripcionUpdate, db: Session = Depends(get_db)):
    descripcion = crud.get_descripcion(db, descripcion_id)
    if not descripcion:
        raise HTTPException(status_code=404, detail="Descripción no encontrada")
    return crud.update_descripcion(db, descripcion, body)


@app.delete("/descripciones/{descripcion_id}", status_code=204, tags=["descripciones"])
def delete_descripcion(descripcion_id: int, db: Session = Depends(get_db)):
    descripcion = crud.get_descripcion(db, descripcion_id)
    if not descripcion:
        raise HTTPException(status_code=404, detail="Descripción no encontrada")
    crud.delete_descripcion(db, descripcion)
    return None


@app.get("/inventario", response_model=list[schemas.InventarioOut], tags=["inventario"])
def list_inventario(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    return crud.list_inventario(db, skip=skip, limit=limit)


@app.get("/inventario/{inventario_id}", response_model=schemas.InventarioOut, tags=["inventario"])
def get_inventario(inventario_id: int, db: Session = Depends(get_db)):
    inv = crud.get_inventario(db, inventario_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")
    return inv


@app.post("/inventario", response_model=schemas.InventarioOut, status_code=201, tags=["inventario"])
def create_inventario(body: schemas.InventarioCreate, db: Session = Depends(get_db)):
    inv = crud.create_inventario(db, body)
    return inv


@app.put("/inventario/{inventario_id}", response_model=schemas.InventarioOut, tags=["inventario"])
def update_inventario(inventario_id: int, body: schemas.InventarioUpdate, db: Session = Depends(get_db)):
    inv = crud.get_inventario(db, inventario_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")
    return crud.update_inventario(db, inv, body)


@app.delete("/inventario/{inventario_id}", status_code=204, tags=["inventario"])
def delete_inventario(inventario_id: int, db: Session = Depends(get_db)):
    inv = crud.get_inventario(db, inventario_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")
    crud.delete_inventario(db, inv)
    return None
