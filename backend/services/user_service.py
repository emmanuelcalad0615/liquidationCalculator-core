from sqlalchemy.orm import Session
from models.users import User
from models.empleado import Empleado
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from schemas.user_schema import UserCreate, TokenResponse
from services.empleado_service import create_empleado
from services.utils import hash_password, verify_password, create_access_token

def create_user(db: Session, user: UserCreate) -> User:
    try:
        if db.query(User).filter(User.username == user.username).first():
            raise HTTPException(status_code=409, detail="El usuario ya existe")
        
 

        empleado = db.query(Empleado).filter(Empleado.documento == user.empleado.documento).first()
        if not empleado:
            empleado = create_empleado(db, user.empleado)

        password_hash = hash_password(user.password)

        db_usuario = User(
            username=user.username,
            email=user.email,
            password=password_hash,
            id_empleado=empleado.id_empleado
            )

        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario

    except IntegrityError as e:
        db.rollback()
        if "users_email_key" in str(e.orig):
            raise HTTPException(status_code=409, detail="El email de usuario ya está registrado")
        elif "users_username_key" in str(e.orig):
            raise HTTPException(status_code=409, detail="El username ya está registrado")
        elif "empleado_documento_key" in str(e.orig):
            raise HTTPException(status_code=409, detail="El documento del empleado ya existe")
        else:
            raise HTTPException(status_code=409, detail="Violación de restricción única")
    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear usuario: {str(e)}")


def login_user(db: Session, email: str, password: str):
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        if not user.activo:
            raise HTTPException(status_code = 403, detail = "Usuario inactivo")
        
        if not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Contraseña incorrecta")

        token = create_access_token({"sub": user.email})
        data_response = TokenResponse(
            access_token=token, 
            token_type="bearer", 
            username=user.username, 
            email=user.email
        )
        return data_response

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en login: {str(e)}")
    
def delete_user(db: Session, email:str):
    user = db.query(User).filter(User.email == email).first()
    empleado = db.query(Empleado).filter(Empleado.id_empleado == user.id_empleado).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "Usuario no encontrado")
    if not user.activo:
        return user
    user.activo = False
    empleado.activo = False
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


