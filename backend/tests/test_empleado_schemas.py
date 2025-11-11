import pytest
from datetime import date
from typing import Optional
from pydantic import BaseModel, ValidationError, ConfigDict

# --- Definición de los Esquemas (para autoejecución) ---

class EmpleadoBase(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: int
    documento: str
    fecha_nacimiento:date

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoUpdate(BaseModel):
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    tipo_documento: Optional[int] = None
    documento: Optional[str]  = None
    fecha_nacimiento: Optional[date] = None

class EmpleadoOut(BaseModel):
    id_empleado: int
    nombres: str
    apellidos: str
    tipo_documento: int
    documento: str
    fecha_nacimiento:date

    # Configuración Pydantic V2
    model_config = ConfigDict(from_attributes=True)
    # Nota: Tu esquema original usaba 'class Config: from_attributes = True'.
    # Lo he actualizado a la sintaxis de Pydantic V2 para evitar warnings.

# --- Fixtures de Datos de Prueba ---

@pytest.fixture
def base_data():
    """Datos mínimos requeridos para EmpleadoBase."""
    return {
        "nombres": "Ana María",
        "apellidos": "Pérez López",
        "tipo_documento": 1,
        "documento": "1020304050",
        "fecha_nacimiento": date(1990, 5, 20)
    }

@pytest.fixture
def out_data(base_data):
    """Datos para EmpleadoOut, incluyendo el ID."""
    return {**base_data, "id_empleado": 5}

# --- Pruebas Unitarias ---

## EmpleadoBase y EmpleadoCreate

def test_empleado_base_creacion_exitosa(base_data):
    """Verifica la creación exitosa y la correcta tipificación de fecha."""
    empleado = EmpleadoBase(**base_data)
    assert empleado.nombres == "Ana María"
    assert empleado.documento == "1020304050"
    assert empleado.fecha_nacimiento == date(1990, 5, 20)
    assert isinstance(empleado.fecha_nacimiento, date)

def test_empleado_base_convierte_string_a_date():
    """Verifica que Pydantic puede convertir un string de fecha a objeto date."""
    data = {
        "nombres": "Carlos",
        "apellidos": "Rodríguez",
        "tipo_documento": 2,
        "documento": "987654321",
        "fecha_nacimiento": "1985-11-10" # String
    }
    empleado = EmpleadoBase(**data)
    assert empleado.fecha_nacimiento == date(1985, 11, 10)

def test_empleado_base_validacion_fallida_campo_faltante():
    """Verifica que falla si falta un campo requerido (e.g., apellidos)."""
    data_invalida = {
        "nombres": "Luis",
        "tipo_documento": 1,
        "documento": "123",
        "fecha_nacimiento": date(2000, 1, 1)
    }
    with pytest.raises(ValidationError):
        EmpleadoBase(**data_invalida)

def test_empleado_create_es_identico_a_base(base_data):
    """Verifica que EmpleadoCreate hereda correctamente de EmpleadoBase."""
    empleado_base = EmpleadoBase(**base_data)
    empleado_create = EmpleadoCreate(**base_data)
    assert empleado_base.model_dump() == empleado_create.model_dump()
    assert EmpleadoCreate.model_fields.keys() == EmpleadoBase.model_fields.keys()

## EmpleadoUpdate

def test_empleado_update_creacion_vacio_exitosa():
    """Verifica que EmpleadoUpdate se crea exitosamente sin campos (todos son opcionales)."""
    update = EmpleadoUpdate()
    assert update.nombres is None
    assert update.documento is None
    assert update.fecha_nacimiento is None

def test_empleado_update_creacion_parcial_exitosa():
    """Verifica que EmpleadoUpdate se crea con un subconjunto de campos, incluyendo una fecha."""
    data = {
        "documento": "123456789",
        "fecha_nacimiento": "1999-03-25"
    }
    update = EmpleadoUpdate(**data)
    assert update.documento == "123456789"
    assert update.fecha_nacimiento == date(1999, 3, 25)
    assert update.apellidos is None

def test_empleado_update_validacion_fallida_tipos():
    """Verifica que falla si se intenta asignar un tipo incorrecto (e.g., int a nombres)."""
    data_invalida = {"nombres": 12345}
    with pytest.raises(ValidationError):
        EmpleadoUpdate(**data_invalida)

## EmpleadoOut

def test_empleado_out_creacion_exitosa(out_data):
    """Verifica la creación de EmpleadoOut con el campo id_empleado requerido."""
    empleado_out = EmpleadoOut(**out_data)
    assert empleado_out.id_empleado == 5
    assert empleado_out.nombres == "Ana María"

def test_empleado_out_validacion_fallida_id_empleado(base_data):
    """Verifica que falla si falta id_empleado (requerido)."""
    with pytest.raises(ValidationError):
        EmpleadoOut(**base_data)

def test_empleado_out_config_from_attributes():
    """Verifica que from_attributes está habilitado."""
    assert EmpleadoOut.model_config.get('from_attributes') is True