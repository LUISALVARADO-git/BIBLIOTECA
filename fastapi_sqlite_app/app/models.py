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
