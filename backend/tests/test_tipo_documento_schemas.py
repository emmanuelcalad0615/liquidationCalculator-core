import pytest
from typing import Optional
from pydantic import BaseModel, ValidationError, ConfigDict

# --- Definición de los Esquemas (Actualizados para V2) ---

class TipoDocumentoBase(BaseModel):
    descripcion: str

class TipoDocumentoCreate(TipoDocumentoBase):
    pass

class TipoDocumentoUpdate(BaseModel):
    descripcion: str | None = None

class TipoDocumentoOut(BaseModel):
    id_tipo_documento: int
    descripcion: str

    # Configuración Pydantic V2
    model_config = ConfigDict(from_attributes=True)

# --- Fixtures de Datos de Prueba ---

@pytest.fixture
def base_data():
    """Datos mínimos requeridos para TipoDocumentoBase."""
    return {
        "descripcion": "Cédula de Ciudadanía"
    }

@pytest.fixture
def out_data(base_data):
    """Datos para TipoDocumentoOut, incluyendo el ID."""
    return {**base_data, "id_tipo_documento": 1}

# --- Pruebas Unitarias ---

## TipoDocumentoBase y TipoDocumentoCreate

def test_tipo_documento_base_creacion_exitosa(base_data):
    """Verifica la creación exitosa con el campo descripcion."""
    tipo = TipoDocumentoBase(**base_data)
    assert tipo.descripcion == "Cédula de Ciudadanía"

def test_tipo_documento_base_validacion_fallida_campo_faltante():
    """Verifica que falla si falta la descripcion (requerido)."""
    data_invalida = {}
    with pytest.raises(ValidationError):
        TipoDocumentoBase(**data_invalida)

def test_tipo_documento_create_es_identico_a_base(base_data):
    """Verifica que TipoDocumentoCreate hereda correctamente de Base."""
    tipo_base = TipoDocumentoBase(**base_data)
    tipo_create = TipoDocumentoCreate(**base_data)
    assert tipo_base.model_dump() == tipo_create.model_dump()

## TipoDocumentoUpdate

def test_tipo_documento_update_creacion_vacio_exitosa():
    """Verifica que TipoDocumentoUpdate se crea exitosamente sin campos."""
    update = TipoDocumentoUpdate()
    assert update.descripcion is None

def test_tipo_documento_update_creacion_parcial_exitosa():
    """Verifica que TipoDocumentoUpdate se crea con un campo de actualización."""
    data = {"descripcion": "Cédula de Extranjería"}
    update = TipoDocumentoUpdate(**data)
    assert update.descripcion == "Cédula de Extranjería"

def test_tipo_documento_update_validacion_fallida_tipos():
    """Verifica que falla si se intenta asignar un tipo incorrecto (e.g., int)."""
    data_invalida = {"descripcion": 2}
    with pytest.raises(ValidationError):
        TipoDocumentoUpdate(**data_invalida)

## TipoDocumentoOut

def test_tipo_documento_out_creacion_exitosa(out_data):
    """Verifica la creación de TipoDocumentoOut con id_tipo_documento requerido."""
    tipo_out = TipoDocumentoOut(**out_data)
    assert tipo_out.id_tipo_documento == 1
    assert tipo_out.descripcion == "Cédula de Ciudadanía"

def test_tipo_documento_out_validacion_fallida_id_faltante(base_data):
    """Verifica que falla si falta id_tipo_documento (requerido)."""
    with pytest.raises(ValidationError):
        TipoDocumentoOut(**base_data)

def test_tipo_documento_out_config_from_attributes():
    """Verifica que from_attributes está habilitado."""
    assert TipoDocumentoOut.model_config.get('from_attributes') is True