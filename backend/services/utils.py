from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from config import settings
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def handle_integrity_error(e: IntegrityError, entity: str = "Registro"):
    """
    Maneja errores de integridad de SQLAlchemy y los convierte en HTTPException más claros.
    """
    if "unique constraint" in str(e.orig).lower():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"{entity} ya existe (violación de UNIQUE)"
        )
    elif "foreign key" in str(e.orig).lower():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{entity} con clave foránea inválida"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error de integridad en {entity}: {str(e.orig)}"
        )