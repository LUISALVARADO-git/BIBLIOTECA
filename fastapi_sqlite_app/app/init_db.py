"""Crea las tablas en SQLite si no existen."""
from .database import engine, Base
from . import models

def main():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas/actualizadas en app.db")

if __name__ == "__main__":
    main()
