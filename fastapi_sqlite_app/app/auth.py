from datetime import datetime, timedelta, timezone
from typing import Dict, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

# Clave secreta para firmar el JWT (en un proyecto real, pon esto en variables de entorno)
SECRET_KEY = "cambia_esta_clave_por_una_muy_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# URL del endpoint que emite el token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Para simplificar, usamos un "usuario" en memoria
fake_user_db: Dict[str, Dict[str, str]] = {
    "admin": {
        "username": "admin",
        # En un proyecto real deberías guardar un password hasheado
        "password": "admin123",
    }
}


def authenticate_user(username: str, password: str) -> Optional[Dict[str, str]]:
    user = fake_user_db.get(username)
    if not user or user["password"] != password:
        return None
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> Dict[str, str]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = fake_user_db.get(username)
    if user is None:
        raise credentials_exception
    return user
