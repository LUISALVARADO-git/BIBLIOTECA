from pydantic import BaseModel, Field
from typing import Optional


# -------------------------
# Esquemas de autenticación (Token)
# -------------------------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


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
