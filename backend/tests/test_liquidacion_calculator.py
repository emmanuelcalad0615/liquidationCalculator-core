import pytest
from datetime import date, datetime
from decimal import Decimal
from unittest.mock import MagicMock, patch
from typing import NamedTuple

# Asumimos que esta clase es importable desde tu servicio
from services.calc_liquidacion_service import LiquidacionCalculator

# Definimos LiquidacionException localmente (solo si tu servicio la tiene)
class LiquidacionException(Exception):
    """Excepción Mock para los tests (usada para los flujos que deberían lanzar errores)."""
    pass

# --- MOCKS DE CLASES Y DATOS ---

class MockContrato(NamedTuple):
    id_contrato: int
    fecha_inicio: date
    fecha_fin: date | None
    salario_mensual: Decimal
    id_tipo_contrato: int

class MockMotivo(NamedTuple):
    id_motivo_terminacion: int
    descripcion: str

class MockLiquidacion:
    """Mock para la clase Liquidacion."""
    id_contrato = MagicMock()

    def __init__(self, **kwargs):
        self.id_liquidacion = kwargs.get('id_liquidacion', 999)
        self.id_contrato = kwargs.get('id_contrato')
        self.id_motivo_terminacion = kwargs.get('id_motivo_terminacion')
        self.fecha_liquidacion = kwargs.get('fecha_liquidacion')
        self.total_liquidacion = kwargs.get('total_liquidacion')

class MockDetalleLiquidacion:
    """
    Mock para la clase DetalleLiquidacion.
    Usa 'concepto' para coincidir con el servicio.
    """
    def __init__(self, id_liquidacion, concepto, valor):
        self.id_liquidacion = id_liquidacion
        self.concepto = concepto
        self.valor = valor

# --- HELPERS ---

def setup_query_mocks(mock_db: MagicMock, contrato, motivo=None, liquidacion_existente=None):
    """Configura el comportamiento de las llamadas a la base de datos."""

    query_mock = MagicMock()
    query_mock.filter.return_value.first.side_effect = [
        contrato,                # Contrato
        motivo,                  # MotivoTerminacion
        liquidacion_existente    # Liquidacion existente
    ]

    mock_db.query.return_value = query_mock
    # Simular la asignación de id_liquidacion al hacer refresh
    mock_db.refresh.side_effect = lambda obj: setattr(obj, 'id_liquidacion', 999)

    return mock_db

# --- FIXTURES DE PYTEST ---

@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def calculator(mock_db):
    """
    Instancia de la calculadora con los mocks de las clases ORM inyectados en el servicio.
    """
    # Parcheamos las referencias de las clases ORM dentro del módulo de servicio
    with patch('services.calc_liquidacion_service.Liquidacion', MockLiquidacion), \
            patch('services.calc_liquidacion_service.DetalleLiquidacion', MockDetalleLiquidacion), \
            patch('services.calc_liquidacion_service.Contrato', MagicMock()), \
            patch('services.calc_liquidacion_service.MotivoTerminacion', MagicMock()):

        yield LiquidacionCalculator(mock_db)


@pytest.fixture
def contrato_data():
    """Datos base para un contrato de 1 año."""
    return MockContrato(
        id_contrato=1,
        fecha_inicio=date(2024, 1, 1),
        fecha_fin=date(2024, 12, 31),
        salario_mensual=Decimal('3000000.00'),
        id_tipo_contrato=1
    )

@pytest.fixture
def motivo_data():
    """Motivo sin indemnización (ID != 4)."""
    return MockMotivo(id_motivo_terminacion=1, descripcion='Renuncia voluntaria')

@pytest.fixture
def motivo_indemnizacion():
    """Motivo con derecho a indemnización (ID = 4)."""
    return MockMotivo(id_motivo_terminacion=4, descripcion='Despido sin justa causa')

# --- PRUEBAS DE FLUJO ---

def test_calculo_base_sin_indemnizacion(calculator, mock_db, contrato_data, motivo_data):
    """Prueba el flujo de cálculo para un motivo sin indemnización (ID != 4)."""

    mock_db = setup_query_mocks(mock_db, contrato_data, motivo_data)

    # CORRECCIÓN DE ORDEN: Definir 'dias' y 'salario' antes de usarlos
    dias = (contrato_data.fecha_fin - contrato_data.fecha_inicio).days
    salario = float(contrato_data.salario_mensual)

    # Cálculos esperados
    cesantias_esperadas = (salario * dias) / 360
    intereses_esperados = cesantias_esperadas * 0.12 * (dias / 360)
    vacaciones_esperadas = (salario * dias) / 720
    prima_esperada = (salario * dias) / 360

    # CORRECCIÓN DE TIPOGRAFÍA: Se usa 'intereses_esperados'
    total_esperado = cesantias_esperadas + intereses_esperados + vacaciones_esperadas + prima_esperada

    resultado = calculator.calcular(contrato_data.id_contrato, motivo_data.id_motivo_terminacion)

    assert resultado['total_liquidacion'] == pytest.approx(total_esperado, 0.01)
    assert resultado['indemnizacion'] == 0.0
    assert mock_db.add.called
    assert mock_db.commit.called

def test_calculo_con_indemnizacion(calculator, mock_db, contrato_data, motivo_indemnizacion):
    """Prueba el flujo de cálculo con indemnización (ID = 4)."""

    mock_db = setup_query_mocks(mock_db, contrato_data, motivo_indemnizacion)

    dias = (contrato_data.fecha_fin - contrato_data.fecha_inicio).days
    salario = float(contrato_data.salario_mensual)

    # Asumimos que la lógica del servicio devuelve 1 mes de salario para este caso
    indemnizacion_esperada = salario

    cesantias_esperadas = (salario * dias) / 360
    intereses_esperados = cesantias_esperadas * 0.12 * (dias / 360)
    vacaciones_esperadas = (salario * dias) / 720
    prima_esperada = (salario * dias) / 360

    total_esperado = cesantias_esperadas + intereses_esperados + vacaciones_esperadas + prima_esperada + indemnizacion_esperada

    resultado = calculator.calcular(contrato_data.id_contrato, motivo_indemnizacion.id_motivo_terminacion)

    assert resultado['total_liquidacion'] == pytest.approx(total_esperado, 0.01)
    assert resultado['indemnizacion'] == pytest.approx(indemnizacion_esperada, 0.01)
    assert mock_db.add.called
    assert mock_db.commit.called

# --- PRUEBAS DE FALLO ---

def test_calculo_falla_contrato_no_encontrado(calculator, mock_db, motivo_data):
    """Verifica que falla si el contrato no se encuentra."""

    mock_db = setup_query_mocks(mock_db, None, motivo_data)

    with pytest.raises(ValueError) as excinfo:
        calculator.calcular(999, motivo_data.id_motivo_terminacion)

    assert "Contrato no encontrado" in str(excinfo.value)
    assert not mock_db.commit.called

def test_calculo_falla_motivo_no_encontrado(calculator, mock_db, contrato_data):
    """Verifica que falla si el motivo no se encuentra."""

    mock_db = setup_query_mocks(mock_db, contrato_data, None)

    with pytest.raises(ValueError) as excinfo:
        calculator.calcular(contrato_data.id_contrato, 999)

    assert "Motivo de terminación no encontrado" in str(excinfo.value)
    assert not mock_db.commit.called

def test_calculo_falla_liquidacion_existente(calculator, mock_db, contrato_data, motivo_data):
    """Verifica que falla si ya existe una liquidación para el contrato."""

    liquidacion_existente = MockLiquidacion(id_liquidacion=100)

    mock_db = setup_query_mocks(mock_db, contrato_data, motivo_data, liquidacion_existente)

    # El test espera ValueError para coincidir con el servicio.
    with pytest.raises(ValueError) as excinfo:
        calculator.calcular(contrato_data.id_contrato, motivo_data.id_motivo_terminacion)

    assert "Ya existe una liquidación registrada" in str(excinfo.value)
    assert not mock_db.add.called
    assert not mock_db.commit.called

def test_calculo_falla_sin_fecha_fin(calculator, mock_db, contrato_data, motivo_data):
    """Verifica que falla si el contrato no tiene fecha de fin."""

    contrato_sin_fin = contrato_data._replace(fecha_fin=None)

    mock_db = setup_query_mocks(mock_db, contrato_sin_fin, motivo_data)

    # El test espera ValueError para coincidir con el servicio.
    with pytest.raises(ValueError) as excinfo:
        calculator.calcular(contrato_sin_fin.id_contrato, motivo_data.id_motivo_terminacion)

    assert "El contrato no tiene fecha de finalización registrada" in str(excinfo.value)
    assert not mock_db.commit.called