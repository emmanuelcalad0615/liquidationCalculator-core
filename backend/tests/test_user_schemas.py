import pytest
from datetime import date
from pydantic import BaseModel, EmailStr, ValidationError, ConfigDict
from typing import Optional, List

# --- Definición de Esquemas de Empleado (Requeridos para la prueba) ---
# Se copian las clases de Empleado que se necesitan para que este archivo sea ejecutable
class EmpleadoBase(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: int
    documento: str
    fecha_nacimiento: date

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoOut(EmpleadoBase):
    id_empleado: int
    model_config = ConfigDict(from_attributes=True)
# --- Fin de Esquemas de Empleado ---


# --- Definición de los Esquemas de Usuario (Actualizados para V2) ---

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    empleado: EmpleadoCreate

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    empleado: EmpleadoOut

    # Configuración Pydantic V2
    model_config = ConfigDict(from_attributes=True)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserDelete(BaseModel):
    email: EmailStr

class TokenResponse(BaseModel):
    id: int
    access_token: str
    token_type: str
    username: str
    email: str

# --- Fixtures de Datos de Prueba ---

@pytest.fixture
def empleado_create_data():
    """Datos para EmpleadoCreate."""
    return {
        "nombres": "Ana",
        "apellidos": "García",
        "tipo_documento": 1,
        "documento": "1020000001",
        "fecha_nacimiento": date(1995, 8, 10)
    }

@pytest.fixture
def empleado_out_data(empleado_create_data):
    """Datos para EmpleadoOut."""
    return {**empleado_create_data, "id_empleado": 50}

@pytest.fixture
def user_create_data(empleado_create_data):
    """Datos para UserCreate, incluyendo el empleado anidado."""
    return {
        "username": "anagarcia",
        "email": "ana.garcia@dominio.com",
        "password": "PasswordSeguro123",
        "empleado": empleado_create_data
    }

@pytest.fixture
def user_out_data(empleado_out_data):
    """Datos para UserOut, incluyendo el empleado anidado."""
    return {
        "id": 1,
        "username": "anagarcia",
        "email": "ana.garcia@dominio.com",
        "empleado": empleado_out_data
    }

# --- Pruebas Unitarias ---

## UserCreate

def test_user_create_creacion_exitosa(user_create_data):
    """Verifica la creación exitosa con EmailStr y esquema anidado."""
    user = UserCreate(**user_create_data)
    assert user.username == "anagarcia"
    assert user.email == "ana.garcia@dominio.com"
    assert isinstance(user.empleado, EmpleadoCreate)
    assert user.empleado.nombres == "Ana"

def test_user_create_validacion_fallida_email_invalido(user_create_data):
    """Verifica que falla si el email no es válido (EmailStr)."""
    invalid_data = {**user_create_data, "email": "email_invalido"}
    with pytest.raises(ValidationError):
        UserCreate(**invalid_data)

def test_user_create_validacion_fallida_empleado_incompleto(user_create_data):
    """Verifica que falla si los datos anidados de Empleado están incompletos."""
    empleado_invalido = {"nombres": "Juan"} # Faltan campos requeridos en EmpleadoCreate
    invalid_data = {**user_create_data, "empleado": empleado_invalido}
    with pytest.raises(ValidationError):
        UserCreate(**invalid_data)

## UserOut

def test_user_out_creacion_exitosa(user_out_data):
    """Verifica la creación exitosa con ID y EmpleadoOut anidado."""
    user_out = UserOut(**user_out_data)
    assert user_out.id == 1
    assert user_out.email == "ana.garcia@dominio.com"
    assert isinstance(user_out.empleado, EmpleadoOut)
    assert user_out.empleado.id_empleado == 50

def test_user_out_validacion_fallida_id_faltante(user_create_data):
    """Verifica que falla si falta el campo id (requerido)."""
    # Usar user_create_data ya que no tiene 'id'
    with pytest.raises(ValidationError):
        UserOut(**user_create_data)

def test_user_out_config_from_attributes():
    """Verifica que from_attributes está habilitado."""
    assert UserOut.model_config.get('from_attributes') is True

## LoginRequest

def test_login_request_creacion_exitosa():
    """Verifica la creación exitosa de la solicitud de login."""
    login_data = {"email": "test@dominio.com", "password": "securepassword"}
    login = LoginRequest(**login_data)
    assert login.email == "test@dominio.com"

def test_login_request_validacion_fallida_password_faltante():
    """Verifica que falla si falta la contraseña."""
    invalid_data = {"email": "test@dominio.com"}
    with pytest.raises(ValidationError):
        LoginRequest(**invalid_data)

## UserDelete

def test_user_delete_creacion_exitosa():
    """Verifica la creación exitosa de la solicitud de borrado."""
    delete_data = {"email": "user_to_delete@dominio.com"}
    delete = UserDelete(**delete_data)
    assert delete.email == "user_to_delete@dominio.com"

## TokenResponse

def test_token_response_creacion_exitosa():
    """Verifica que TokenResponse se crea correctamente."""
    token_data = {
        "id": 10,
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "token_type": "bearer",
        "username": "tokenuser",
        "email": "token@example.com"
    }
    token = TokenResponse(**token_data)
    assert token.id == 10
    assert token.token_type == "bearer"
    assert token.email == "token@example.com"

def test_token_response_validacion_fallida_access_token_faltante():
    """Verifica que falla si falta el access_token."""
    invalid_data = {
        "id": 10,
        "token_type": "bearer",
        "username": "tokenuser",
        "email": "token@example.com"
    }
    with pytest.raises(ValidationError):
        TokenResponse(**invalid_data)