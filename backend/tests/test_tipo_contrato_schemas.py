import pytest
from typing import Optional
from pydantic import BaseModel, ValidationError, ConfigDict

# --- Definición de los Esquemas (Actualizados para V2) ---

class TipoContratoBase(BaseModel):
    descripcion: str


class TipoContratoCreate(TipoContratoBase):
    pass


class TipoContratoUpdate(BaseModel):
    descripcion: str | None = None


class TipoContratoOut(BaseModel):
    id_tipo_contrato: int
    descripcion: str

    # Configuración Pydantic V2
    model_config = ConfigDict(from_attributes=True)

# --- Fixtures de Datos de Prueba ---

@pytest.fixture
def base_data():
    """Datos mínimos requeridos para TipoContratoBase."""
    return {
        "descripcion": "Término Fijo"
    }

@pytest.fixture
def out_data(base_data):
    """Datos para TipoContratoOut, incluyendo el ID."""
    return {**base_data, "id_tipo_contrato": 1}

# --- Pruebas Unitarias ---

## TipoContratoBase y TipoContratoCreate

def test_tipo_contrato_base_creacion_exitosa(base_data):
    """Verifica la creación exitosa con el campo descripcion."""
    tipo = TipoContratoBase(**base_data)
    assert tipo.descripcion == "Término Fijo"

def test_tipo_contrato_base_validacion_fallida_campo_faltante():
    """Verifica que falla si falta la descripcion (requerido)."""
    data_invalida = {}
    with pytest.raises(ValidationError):
        TipoContratoBase(**data_invalida)

def test_tipo_contrato_base_validacion_fallida_descripcion_tipo():
    """Verifica que falla si descripcion no es un string."""
    data_invalida = {"descripcion": 10}
    with pytest.raises(ValidationError):
        TipoContratoBase(**data_invalida)

def test_tipo_contrato_create_es_identico_a_base(base_data):
    """Verifica que TipoContratoCreate hereda correctamente de Base."""
    tipo_base = TipoContratoBase(**base_data)
    tipo_create = TipoContratoCreate(**base_data)
    assert tipo_base.model_dump() == tipo_create.model_dump()

## TipoContratoUpdate

def test_tipo_contrato_update_creacion_vacio_exitosa():
    """Verifica que TipoContratoUpdate se crea exitosamente sin campos."""
    update = TipoContratoUpdate()
    assert update.descripcion is None

def test_tipo_contrato_update_creacion_parcial_exitosa():
    """Verifica que TipoContratoUpdate se crea con un campo de actualización."""
    data = {"descripcion": "Término Indefinido"}
    update = TipoContratoUpdate(**data)
    assert update.descripcion == "Término Indefinido"

def test_tipo_contrato_update_validacion_fallida_tipos():
    """Verifica que falla si se intenta asignar un tipo incorrecto."""
    data_invalida = {"descripcion": 50.5}
    with pytest.raises(ValidationError):
        TipoContratoUpdate(**data_invalida)

## TipoContratoOut

def test_tipo_contrato_out_creacion_exitosa(out_data):
    """Verifica la creación de TipoContratoOut con id_tipo_contrato requerido."""
    tipo_out = TipoContratoOut(**out_data)
    assert tipo_out.id_tipo_contrato == 1
    assert tipo_out.descripcion == "Término Fijo"

def test_tipo_contrato_out_validacion_fallida_id_faltante(base_data):
    """Verifica que falla si falta id_tipo_contrato (requerido)."""
    with pytest.raises(ValidationError):
        TipoContratoOut(**base_data)

def test_tipo_contrato_out_config_from_attributes():
    """Verifica que from_attributes está habilitado."""
    assert TipoContratoOut.model_config.get('from_attributes') is True