import pytest
from datetime import date
from typing import Optional
from pydantic import BaseModel, ValidationError, ConfigDict

# --- Definición de los Esquemas ---

class ContratoBase(BaseModel):
    id_empleado: int
    id_tipo_contrato: int
    fecha_inicio: date
    fecha_fin: Optional[date] = None
    salario_mensual: float
    auxilio_transporte: Optional[int] = None


class ContratoCreate(ContratoBase):
    pass


class ContratoUpdate(BaseModel):
    id_empleado: Optional[int] = None
    id_tipo_contrato: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    salario_mensual: Optional[float] = None
    auxilio_transporte: Optional[int] = None


class ContratoOut(BaseModel):
    id_contrato: int
    id_empleado: int
    id_tipo_contrato: int
    fecha_inicio: date
    fecha_fin: Optional[date]
    salario_mensual: float
    auxilio_transporte: Optional[int]

    # Actualizado a Pydantic V2:
    model_config = ConfigDict(from_attributes=True)

# --- Fixtures de Datos de Prueba ---

@pytest.fixture
def base_data_fijo():
    """
    Datos de contrato fijo. Incluye explícitamente auxilio_transporte=None
    para cumplir con la validación de ContratoOut.
    """
    return {
        "id_empleado": 1,
        "id_tipo_contrato": 1,
        "fecha_inicio": date(2024, 1, 15),
        "fecha_fin": date(2024, 12, 31),
        "salario_mensual": 2500000.00,
        "auxilio_transporte": None, # CORREGIDO
    } # CORREGIDO: Se asegura que esta llave está presente

@pytest.fixture
def base_data_indefinido():
    """Datos para un contrato indefinido."""
    return {
        "id_empleado": 2,
        "id_tipo_contrato": 2,
        "fecha_inicio": "2023-06-01",
        "salario_mensual": 1200000.00,
        "auxilio_transporte": 162000,
    }

@pytest.fixture
def out_data(base_data_fijo):
    """Datos de salida completos (inyecta la fixture base_data_fijo)."""
    return {**base_data_fijo, "id_contrato": 10}

# --- Pruebas Unitarias ---

def test_contrato_base_creacion_fijo_exitosa(base_data_fijo):
    """Verifica que ContratoBase se crea correctamente con todos los campos requeridos y opcionales."""
    contrato = ContratoBase(**base_data_fijo)
    assert contrato.id_empleado == 1
    assert contrato.fecha_fin == date(2024, 12, 31)
    assert contrato.salario_mensual == 2500000.00
    assert contrato.auxilio_transporte is None

def test_contrato_base_creacion_indefinido_exitosa(base_data_indefinido):
    """Verifica que ContratoBase se crea correctamente sin fecha_fin y convierte el string de fecha."""
    contrato = ContratoBase(**base_data_indefinido)
    assert contrato.fecha_inicio == date(2023, 6, 1)
    assert contrato.fecha_fin is None
    assert contrato.auxilio_transporte == 162000

def test_contrato_base_validacion_fallida():
    """Verifica que falla si falta un campo requerido (e.g., salario_mensual)."""
    data_invalida = {
        "id_empleado": 1,
        "id_tipo_contrato": 1,
        "fecha_inicio": "2024-01-01"
    }
    with pytest.raises(ValidationError):
        ContratoBase(**data_invalida)

def test_contrato_create_es_identico_a_base(base_data_fijo):
    """Verifica que ContratoCreate hereda correctamente de ContratoBase."""
    contrato_base = ContratoBase(**base_data_fijo)
    contrato_create = ContratoCreate(**base_data_fijo)
    assert contrato_base.model_dump() == contrato_create.model_dump()
    assert ContratoCreate.model_fields.keys() == ContratoBase.model_fields.keys()

def test_contrato_update_creacion_vacio_exitosa():
    """Verifica que ContratoUpdate se crea exitosamente sin campos (todos son opcionales)."""
    update = ContratoUpdate()
    assert update.id_empleado is None
    assert update.salario_mensual is None

def test_contrato_update_creacion_parcial_exitosa():
    """Verifica que ContratoUpdate se crea con un subconjunto de campos."""
    data = {"salario_mensual": 3000000.00, "auxilio_transporte": 0}
    update = ContratoUpdate(**data)
    assert update.salario_mensual == 3000000.00
    assert update.id_empleado is None

def test_contrato_update_validacion_tipos_fallida():
    """Verifica que falla si se provee un tipo de dato incorrecto (e.g., id_empleado string)."""
    data_invalida = {"id_empleado": "uno"}
    with pytest.raises(ValidationError):
        ContratoUpdate(**data_invalida)

def test_contrato_out_creacion_exitosa(out_data):
    """Verifica la creación de ContratoOut con el campo id_contrato requerido."""
    contrato_out = ContratoOut(**out_data)
    assert contrato_out.id_contrato == 10
    assert contrato_out.fecha_inicio == date(2024, 1, 15)

def test_contrato_out_validacion_fallida_id_contrato(base_data_fijo):
    """Verifica que falla si falta id_contrato, ya que no es Optional."""
    data_invalida = base_data_fijo
    with pytest.raises(ValidationError):
        ContratoOut(**data_invalida)

def test_contrato_out_config_orm_mode():
    """Verifica que from_attributes (anteriormente orm_mode) está habilitado."""
    assert ContratoOut.model_config.get('from_attributes') is True