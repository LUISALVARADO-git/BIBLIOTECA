from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLite en archivo local
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# check_same_thread=False para SQLite en hilos con FastAPI (solo demo)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={ "check_same_thread": False }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# Dependencia para inyección de sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
