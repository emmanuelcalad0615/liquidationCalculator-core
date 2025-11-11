import pytest
from datetime import date
from typing import List, Optional
from pydantic import BaseModel, ValidationError, ConfigDict

# --- Definición de los Esquemas (Actualizados para V2) ---

class DetalleLiquidacionOut(BaseModel):
    id_detalle: int
    concepto: str
    valor: float

    model_config = ConfigDict(from_attributes=True) # Actualizado V2


class MotivoTerminacionOut(BaseModel):
    id_motivo_terminacion: int
    descripcion: str

    model_config = ConfigDict(from_attributes=True) # Actualizado V2


class LiquidacionBase(BaseModel):
    id_contrato: int
    fecha_liquidacion: date
    id_motivo_terminacion: int
    total_liquidacion: float


class LiquidacionCreate(LiquidacionBase):
    pass


class LiquidacionUpdate(BaseModel):
    id_contrato: Optional[int] = None
    fecha_liquidacion: Optional[date] = None
    id_motivo_terminacion: Optional[int] = None
    total_liquidacion: Optional[float] = None


class LiquidacionOut(BaseModel):
    id_liquidacion: int
    id_contrato: int
    fecha_liquidacion: date
    id_motivo_terminacion: int
    total_liquidacion: float
    motivo_terminacion: Optional[MotivoTerminacionOut]
    detalles_liquidacion: List[DetalleLiquidacionOut] = []

    model_config = ConfigDict(from_attributes=True) # Actualizado V2

# --- Fixtures de Datos de Prueba ---

@pytest.fixture
def detalle_data():
    """Datos de un detalle de liquidación."""
    return {
        "id_detalle": 1,
        "concepto": "Salario pendiente",
        "valor": 500000.00
    }

@pytest.fixture
def motivo_data():
    """Datos de un motivo de terminación."""
    return {
        "id_motivo_terminacion": 3,
        "descripcion": "Renuncia voluntaria"
    }

@pytest.fixture
def liquidacion_base_data():
    """Datos mínimos requeridos para LiquidacionBase."""
    return {
        "id_contrato": 15,
        "fecha_liquidacion": date(2025, 10, 31),
        "id_motivo_terminacion": 3,
        "total_liquidacion": 2800000.50
    }

@pytest.fixture
def liquidacion_out_data(liquidacion_base_data, motivo_data, detalle_data):
    """Datos completos para LiquidacionOut, incluyendo objetos anidados."""
    return {
        "id_liquidacion": 100,
        **liquidacion_base_data,
        "motivo_terminacion": motivo_data,
        "detalles_liquidacion": [detalle_data,
                                 {"id_detalle": 2, "concepto": "Vacaciones", "valor": 2300000.50}]
    }

# --- Pruebas Unitarias ---

## LiquidacionBase y LiquidacionCreate

def test_liquidacion_base_creacion_exitosa(liquidacion_base_data):
    """Verifica la creación exitosa con todos los campos requeridos."""
    liquidacion = LiquidacionBase(**liquidacion_base_data)
    assert liquidacion.id_contrato == 15
    assert liquidacion.fecha_liquidacion == date(2025, 10, 31)
    assert liquidacion.total_liquidacion == 2800000.50

def test_liquidacion_base_validacion_fallida_fecha_incorrecta():
    """Verifica que falla con un formato de fecha incorrecto."""
    data_invalida = {
        "id_contrato": 1,
        "fecha_liquidacion": "31/10/2025", # Formato inválido
        "id_motivo_terminacion": 1,
        "total_liquidacion": 1000.0
    }
    with pytest.raises(ValidationError):
        LiquidacionBase(**data_invalida)

def test_liquidacion_create_es_identico_a_base(liquidacion_base_data):
    """Verifica que LiquidacionCreate hereda correctamente de LiquidacionBase."""
    liquidacion_base = LiquidacionBase(**liquidacion_base_data)
    liquidacion_create = LiquidacionCreate(**liquidacion_base_data)
    assert liquidacion_base.model_dump() == liquidacion_create.model_dump()

## LiquidacionUpdate

def test_liquidacion_update_creacion_vacio_exitosa():
    """Verifica que LiquidacionUpdate se crea exitosamente sin campos."""
    update = LiquidacionUpdate()
    assert update.total_liquidacion is None
    assert update.id_contrato is None

def test_liquidacion_update_creacion_parcial_exitosa():
    """Verifica que LiquidacionUpdate se crea con un subconjunto de campos."""
    data = {"total_liquidacion": 3500000.00, "fecha_liquidacion": "2026-01-01"}
    update = LiquidacionUpdate(**data)
    assert update.total_liquidacion == 3500000.00
    assert update.fecha_liquidacion == date(2026, 1, 1)
    assert update.id_contrato is None

def test_liquidacion_update_validacion_fallida_tipos():
    """Verifica que falla si se intenta asignar un tipo incorrecto (e.g., string a int)."""
    data_invalida = {"id_contrato": "quince"}
    with pytest.raises(ValidationError):
        LiquidacionUpdate(**data_invalida)

## LiquidacionOut (Anidación y Campos Requeridos)

def test_liquidacion_out_creacion_exitosa(liquidacion_out_data):
    """Verifica la creación de LiquidacionOut con id y anidación de objetos."""
    liquidacion_out = LiquidacionOut(**liquidacion_out_data)

    # Campos base
    assert liquidacion_out.id_liquidacion == 100
    assert liquidacion_out.total_liquidacion == 2800000.50

    # Campo anidado simple (MotivoTerminacionOut)
    assert liquidacion_out.motivo_terminacion is not None
    assert liquidacion_out.motivo_terminacion.descripcion == "Renuncia voluntaria"

    # Campo anidado lista (detalles_liquidacion)
    assert isinstance(liquidacion_out.detalles_liquidacion, List)
    assert len(liquidacion_out.detalles_liquidacion) == 2
    assert liquidacion_out.detalles_liquidacion[1].concepto == "Vacaciones"

def test_liquidacion_out_validacion_fallida_id_liquidacion(liquidacion_base_data):
    """Verifica que falla si falta id_liquidacion (requerido)."""
    with pytest.raises(ValidationError):
        LiquidacionOut(**liquidacion_base_data)

def test_liquidacion_out_campos_anidados_opcionales(liquidacion_base_data):
    """Verifica que puede crearse LiquidacionOut sin los objetos anidados opcionales (motivo_terminacion)."""
    data = {
        "id_liquidacion": 101,
        **liquidacion_base_data,
        "motivo_terminacion": None,  # Es Optional
        "detalles_liquidacion": []  # Por defecto o lista vacía
    }
    liquidacion_out = LiquidacionOut(**data)
    assert liquidacion_out.motivo_terminacion is None
    assert liquidacion_out.detalles_liquidacion == []