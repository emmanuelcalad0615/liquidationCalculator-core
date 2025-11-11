import pytest
from typing import Optional
from pydantic import BaseModel, ValidationError, ConfigDict

# --- Definición de los Esquemas (Actualizados para V2) ---

class MotivoTerminacionBase(BaseModel):
    descripcion: str


class MotivoTerminacionCreate(MotivoTerminacionBase):
    pass


class MotivoTerminacionUpdate(BaseModel):
    descripcion: str | None = None


class MotivoTerminacionOut(BaseModel):
    id_motivo_terminacion: int
    descripcion: str

    # Configuración Pydantic V2
    model_config = ConfigDict(from_attributes=True)
    # Nota: Tu esquema original usaba 'class Config: orm_mode = True'.
    # Lo he actualizado a la sintaxis de Pydantic V2 para evitar warnings.

# --- Fixtures de Datos de Prueba ---

@pytest.fixture
def base_data():
    """Datos mínimos requeridos para MotivoTerminacionBase."""
    return {
        "descripcion": "Despido con justa causa"
    }

@pytest.fixture
def out_data(base_data):
    """Datos para MotivoTerminacionOut, incluyendo el ID."""
    return {**base_data, "id_motivo_terminacion": 2}

# --- Pruebas Unitarias ---

## MotivoTerminacionBase y MotivoTerminacionCreate

def test_motivo_base_creacion_exitosa(base_data):
    """Verifica la creación exitosa con el campo descripcion."""
    motivo = MotivoTerminacionBase(**base_data)
    assert motivo.descripcion == "Despido con justa causa"

def test_motivo_base_validacion_fallida_campo_faltante():
    """Verifica que falla si falta la descripcion (requerido)."""
    data_invalida = {}
    with pytest.raises(ValidationError):
        MotivoTerminacionBase(**data_invalida)

def test_motivo_base_validacion_fallida_descripcion_tipo():
    """Verifica que falla si descripcion no es un string."""
    data_invalida = {"descripcion": 12345}
    with pytest.raises(ValidationError):
        MotivoTerminacionBase(**data_invalida)

def test_motivo_create_es_identico_a_base(base_data):
    """Verifica que MotivoTerminacionCreate hereda correctamente de Base."""
    motivo_base = MotivoTerminacionBase(**base_data)
    motivo_create = MotivoTerminacionCreate(**base_data)
    assert motivo_base.model_dump() == motivo_create.model_dump()

## MotivoTerminacionUpdate

def test_motivo_update_creacion_vacio_exitosa():
    """Verifica que MotivoTerminacionUpdate se crea exitosamente sin campos."""
    update = MotivoTerminacionUpdate()
    assert update.descripcion is None

def test_motivo_update_creacion_parcial_exitosa():
    """Verifica que MotivoTerminacionUpdate se crea con un campo de actualización."""
    data = {"descripcion": "Mutuo acuerdo"}
    update = MotivoTerminacionUpdate(**data)
    assert update.descripcion == "Mutuo acuerdo"

def test_motivo_update_validacion_fallida_tipos():
    """Verifica que falla si se intenta asignar un tipo incorrecto."""
    data_invalida = {"descripcion": 999}
    with pytest.raises(ValidationError):
        MotivoTerminacionUpdate(**data_invalida)

## MotivoTerminacionOut

def test_motivo_out_creacion_exitosa(out_data):
    """Verifica la creación de MotivoTerminacionOut con id_motivo_terminacion requerido."""
    motivo_out = MotivoTerminacionOut(**out_data)
    assert motivo_out.id_motivo_terminacion == 2
    assert motivo_out.descripcion == "Despido con justa causa"

def test_motivo_out_validacion_fallida_id_faltante(base_data):
    """Verifica que falla si falta id_motivo_terminacion (requerido)."""
    with pytest.raises(ValidationError):
        MotivoTerminacionOut(**base_data)

def test_motivo_out_config_from_attributes():
    """Verifica que from_attributes está habilitado."""
    assert MotivoTerminacionOut.model_config.get('from_attributes') is True