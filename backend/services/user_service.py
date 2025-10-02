from sqlalchemy.orm import Session
from models.users import User
from models.empleado import Empleado
from schemas.user_schema import UserCreate, TokenResponse
from services.empleado_service import create_empleado
from services.utils import hash_password, verify_password, create_access_token

def create_user(db: Session, user: UserCreate) -> User:
    try:
        if db.query(User).filter(User.username == user.username).first():
            raise ValueError("El usuario ya existe")

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

    except Exception as e:
        db.rollback()
        raise e
    
def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None, "Usuario no encontrado"
    
    if not verify_password(password, user.password):
        return None, "Contraseña incorrecta"

    token = create_access_token({"sub": user.email})
    data_response = TokenResponse(access_token=token, token_type="bearer", username=user.username, email=user.email)
    
    return data_response, None
    

