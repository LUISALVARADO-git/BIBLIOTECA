from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, Text, ForeignKey
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False, index=True)
    price: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)


class Alumno(Base):
    __tablename__ = "alumnos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(60), nullable=False, index=True)
    apellido: Mapped[str] = mapped_column(String(60), nullable=False, index=True)

    notas: Mapped[list["Nota"]] = relationship(back_populates="alumno", cascade="all, delete-orphan")


class Clase(Base):
    __tablename__ = "clases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(60), nullable=False, index=True)
    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)

    notas: Mapped[list["Nota"]] = relationship(back_populates="clase", cascade="all, delete-orphan")


class Nota(Base):
    __tablename__ = "notas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    alumno_id: Mapped[int] = mapped_column(ForeignKey("alumnos.id"), nullable=False, index=True)
    clase_id: Mapped[int] = mapped_column(ForeignKey("clases.id"), nullable=False, index=True)
    nota: Mapped[float] = mapped_column(Float, nullable=False)

    alumno: Mapped[Alumno] = relationship(back_populates="notas")
    clase: Mapped[Clase] = relationship(back_populates="notas")


# -------------------------
# Modelos de Biblioteca
# -------------------------


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(120), nullable=False, index=True, unique=True)
    contrasena: Mapped[str] = mapped_column(String(255), nullable=False)


class Autor(Base):
    __tablename__ = "autores"

    id_autor: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_autor: Mapped[str] = mapped_column(String(120), nullable=False)


class Categoria(Base):
    __tablename__ = "categorias"

    id_categoria: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_categoria: Mapped[str] = mapped_column(String(120), nullable=False)


class Lenguaje(Base):
    __tablename__ = "lenguajes"

    id_lenguaje: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)


class Libro(Base):
    __tablename__ = "libros"

    id_libro: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(200), nullable=False)
    # Relación lógica con categorias y lenguajes (por id)
    categoria: Mapped[int] = mapped_column(ForeignKey("categorias.id_categoria"), nullable=False)
    lenguaje: Mapped[int] = mapped_column(ForeignKey("lenguajes.id_lenguaje"), nullable=False)
    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)


class Tema(Base):
    __tablename__ = "temas"

    id_tema: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo_tema: Mapped[str] = mapped_column(String(200), nullable=False)
    autor: Mapped[int] = mapped_column(ForeignKey("autores.id_autor"), nullable=False)
    lenguaje: Mapped[int] = mapped_column(ForeignKey("lenguajes.id_lenguaje"), nullable=False)


class Descripcion(Base):
    __tablename__ = "descripciones"

    id_descripcion: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    libro_id: Mapped[int | None] = mapped_column(ForeignKey("libros.id_libro"), nullable=True)
    tema_id: Mapped[int | None] = mapped_column(ForeignKey("temas.id_tema"), nullable=True)
    texto: Mapped[str] = mapped_column(Text, nullable=False)


class Inventario(Base):
    __tablename__ = "inventario"

    id_inventario: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id_usuario"), nullable=False)
    libro_id: Mapped[int] = mapped_column(ForeignKey("libros.id_libro"), nullable=False)
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id_autor"), nullable=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id_categoria"), nullable=False)
    tema_id: Mapped[int] = mapped_column(ForeignKey("temas.id_tema"), nullable=False)
    lenguaje_id: Mapped[int] = mapped_column(ForeignKey("lenguajes.id_lenguaje"), nullable=False)
    descripcion_id: Mapped[int] = mapped_column(ForeignKey("descripciones.id_descripcion"), nullable=False)
