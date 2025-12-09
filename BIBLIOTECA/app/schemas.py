from pydantic import BaseModel, Field
from typing import Optional


# -------------------------
# Esquemas para Item (ya existente)
# -------------------------
class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=60)
    price: float = Field(..., ge=0)
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemOut(ItemBase):
    id: int

    model_config = {
        "from_attributes": True  # Permite convertir desde ORM
    }


# -------------------------
# Esquemas para Alumnos
# -------------------------
class AlumnoBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=60)
    apellido: str = Field(..., min_length=1, max_length=60)


class AlumnoCreate(AlumnoBase):
    pass


class AlumnoUpdate(AlumnoBase):
    pass


class AlumnoOut(AlumnoBase):
    id: int

    model_config = {
        "from_attributes": True
    }


# -------------------------
# Esquemas para Clase
# -------------------------
class ClaseBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=60)
    descripcion: Optional[str] = None


class ClaseCreate(ClaseBase):
    pass


class ClaseUpdate(ClaseBase):
    pass


class ClaseOut(ClaseBase):
    id: int

    model_config = {
        "from_attributes": True
    }


# -------------------------
# Esquemas para Notas
# -------------------------
class NotaBase(BaseModel):
    alumno_id: int
    clase_id: int
    nota: float


class NotaCreate(NotaBase):
    pass


class NotaUpdate(NotaBase):
    pass


class NotaOut(NotaBase):
    id: int

    model_config = {
        "from_attributes": True
    }


# -------------------------
# Esquemas para Biblioteca
# -------------------------


class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    correo: str = Field(..., min_length=5, max_length=120)
    contrasena: str = Field(..., min_length=4, max_length=255)


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(UsuarioBase):
    pass


class UsuarioOut(UsuarioBase):
    id_usuario: int

    model_config = {
        "from_attributes": True
    }


class AutorBase(BaseModel):
    nombre_autor: str = Field(..., min_length=1, max_length=120)


class AutorCreate(AutorBase):
    pass


class AutorUpdate(AutorBase):
    pass


class AutorOut(AutorBase):
    id_autor: int

    model_config = {
        "from_attributes": True
    }


class CategoriaBase(BaseModel):
    nombre_categoria: str = Field(..., min_length=1, max_length=120)


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(CategoriaBase):
    pass


class CategoriaOut(CategoriaBase):
    id_categoria: int

    model_config = {
        "from_attributes": True
    }


class LenguajeBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=80)


class LenguajeCreate(LenguajeBase):
    pass


class LenguajeUpdate(LenguajeBase):
    pass


class LenguajeOut(LenguajeBase):
    id_lenguaje: int

    model_config = {
        "from_attributes": True
    }


class LibroBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)
    categoria: int
    lenguaje: int
    descripcion: Optional[str] = None


class LibroCreate(LibroBase):
    pass


class LibroUpdate(LibroBase):
    pass


class LibroOut(LibroBase):
    id_libro: int

    model_config = {
        "from_attributes": True
    }


class TemaBase(BaseModel):
    titulo_tema: str = Field(..., min_length=1, max_length=200)
    autor: int
    lenguaje: int


class TemaCreate(TemaBase):
    pass


class TemaUpdate(TemaBase):
    pass


class TemaOut(TemaBase):
    id_tema: int

    model_config = {
        "from_attributes": True
    }


class DescripcionBase(BaseModel):
    libro_id: Optional[int] = None
    tema_id: Optional[int] = None
    texto: str


class DescripcionCreate(DescripcionBase):
    pass


class DescripcionUpdate(DescripcionBase):
    pass


class DescripcionOut(DescripcionBase):
    id_descripcion: int

    model_config = {
        "from_attributes": True
    }


class InventarioBase(BaseModel):
    usuario_id: int
    libro_id: int
    autor_id: int
    categoria_id: int
    tema_id: int
    lenguaje_id: int
    descripcion_id: int


class InventarioCreate(InventarioBase):
    pass


class InventarioUpdate(InventarioBase):
    pass


class InventarioOut(InventarioBase):
    id_inventario: int

    model_config = {
        "from_attributes": True
    }
