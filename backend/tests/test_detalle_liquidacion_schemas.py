import pytest
from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel, ValidationError, ConfigDict

# --- Definición de los Esquemas (Actualizados para V2) ---

class DetalleLiquidacionBase(BaseModel):
    concepto: str
    valor: Decimal


class DetalleLiquidacionCreate(DetalleLiquidacionBase):
    id_liquidacion: int


class DetalleLiquidacionUpdate(BaseModel):
    concepto: str | None = None
    valor: Decimal | None = None


class DetalleLiquidacionOut(BaseModel):
    id_detalle: int
    id_liquidacion: int
    concepto: str
    valor: Decimal

    # Configuración Pydantic V2
    model_config = ConfigDict(from_attributes=True)

# --- Fixtures de Datos de Prueba ---

@pytest.fixture
def base_data():
    """Datos mínimos requeridos para DetalleLiquidacionBase."""
    return {
        "concepto": "Cesantías",
        "valor": Decimal("500000.55")  # Usar Decimal para precisión
    }

@pytest.fixture
def create_data(base_data):
    """Datos para DetalleLiquidacionCreate, extiende base_data."""
    return {
        **base_data,
        "id_liquidacion": 1
    }

@pytest.fixture
def out_data(create_data):
    """Datos de salida para DetalleLiquidacionOut."""
    return {
        **create_data,
        "id_detalle": 100
    }

# --- Pruebas Unitarias ---

## DetalleLiquidacionBase

def test_detalle_base_creacion_exitosa(base_data):
    """Verifica la creación exitosa y la correcta tipificación de Decimal."""
    detalle = DetalleLiquidacionBase(**base_data)
    assert detalle.concepto == "Cesantías"
    assert detalle.valor == Decimal("500000.55")
    assert isinstance(detalle.valor, Decimal)

def test_detalle_base_validacion_string_a_decimal():
    """Verifica que acepta strings convertibles a Decimal."""
    data = {"concepto": "Intereses", "valor": "12500.75"}
    detalle = DetalleLiquidacionBase(**data)
    assert detalle.valor == Decimal("12500.75")

def test_detalle_base_validacion_fallida_valor():
    """Verifica que falla si el valor no es convertible a Decimal."""
    with pytest.raises(ValidationError):
        DetalleLiquidacionBase(concepto="Prima", valor="not_a_number")

def test_detalle_base_validacion_fallida_concepto_faltante():
    """Verifica que falla si falta el concepto (requerido)."""
    with pytest.raises(ValidationError):
        DetalleLiquidacionBase(valor=Decimal("100"))

## DetalleLiquidacionCreate

def test_detalle_create_herencia_exitosa(create_data):
    """Verifica la creación exitosa y que hereda de Base."""
    detalle_c = DetalleLiquidacionCreate(**create_data)
    assert detalle_c.id_liquidacion == 1
    assert detalle_c.concepto == "Cesantías"
    assert isinstance(detalle_c, DetalleLiquidacionBase)

def test_detalle_create_validacion_fallida_id_faltante(base_data):
    """Verifica que falla si falta el campo id_liquidacion (requerido en Create)."""
    with pytest.raises(ValidationError):
        DetalleLiquidacionCreate(**base_data)

## DetalleLiquidacionUpdate

def test_detalle_update_creacion_vacia_exitosa():
    """Verifica que se puede crear un objeto Update vacío."""
    update = DetalleLiquidacionUpdate()
    assert update.concepto is None
    assert update.valor is None

def test_detalle_update_creacion_parcial_exitosa():
    """Verifica que se puede crear un objeto Update con solo un campo."""
    data = {"valor": "8000.00"}
    update = DetalleLiquidacionUpdate(**data)
    assert update.valor == Decimal("8000.00")
    assert update.concepto is None

def test_detalle_update_validacion_fallida_tipos():
    """
    Verifica que la actualización falla con un tipo incorrecto para valor.
    CORRECCIÓN: Usamos una lista, que no se puede convertir implícitamente a Decimal.
    """
    with pytest.raises(ValidationError):
        DetalleLiquidacionUpdate(valor=[500]) # Tipo que causará la falla

## DetalleLiquidacionOut

def test_detalle_out_creacion_exitosa(out_data):
    """Verifica que DetalleLiquidacionOut se crea correctamente con id_detalle."""
    detalle_out = DetalleLiquidacionOut(**out_data)
    assert detalle_out.id_detalle == 100
    assert detalle_out.id_liquidacion == 1
    assert detalle_out.valor == Decimal("500000.55")

def test_detalle_out_validacion_fallida_id_detalle(create_data):
    """Verifica que falla si falta id_detalle (requerido)."""
    with pytest.raises(ValidationError):
        DetalleLiquidacionOut(**create_data)

def test_detalle_out_config_from_attributes():
    """Verifica que from_attributes (anteriormente orm_mode) está habilitado."""
    assert DetalleLiquidacionOut.model_config.get('from_attributes') is True