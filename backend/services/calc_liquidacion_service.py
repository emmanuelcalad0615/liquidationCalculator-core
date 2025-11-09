from datetime import date
from decimal import Decimal
from sqlalchemy.orm import Session
from models.contrato import Contrato
from models.liquidacion import Liquidacion
from models.detalle_liquidacion import DetalleLiquidacion
from models.motivo_terminacion import MotivoTerminacion


class LiquidacionCalculator:
    def __init__(self, db: Session):
        self.db = db

    def calcular(self, id_contrato: int, id_motivo_terminacion: int):
        contrato = self.db.query(Contrato).filter(Contrato.id_contrato == id_contrato).first()
        motivo = self.db.query(MotivoTerminacion).filter(
            MotivoTerminacion.id_motivo_terminacion == id_motivo_terminacion
        ).first()

        if not contrato:
            raise ValueError("Contrato no encontrado.")
        if not motivo:
            raise ValueError("Motivo de terminación no encontrado.")

        # Verificar si ya existe una liquidación para el contrato
        existente = self.db.query(Liquidacion).filter(Liquidacion.id_contrato == id_contrato).first()
        if existente:
            raise ValueError("Ya existe una liquidación registrada para este contrato.")

        # Calcular días trabajados
        if not contrato.fecha_fin:
            raise ValueError("El contrato no tiene fecha de finalización registrada.")
        dias_trabajados = (contrato.fecha_fin - contrato.fecha_inicio).days
        salario = float(contrato.salario_mensual)

        # --- Cálculos base ---
        cesantias = (salario * dias_trabajados) / 360
        intereses_cesantias = cesantias * 0.12 * (dias_trabajados / 360)
        vacaciones = (salario * dias_trabajados) / 720
        prima = (salario * dias_trabajados) / 360

        total = cesantias + intereses_cesantias + vacaciones + prima
        indemnizacion = Decimal(0)

        # --- Indemnización solo si el motivo es "Despido sin justa causa" (ID = 4) ---
        if id_motivo_terminacion == 4:
            indemnizacion = self.calcular_indemnizacion(dias_trabajados, salario)
            total += indemnizacion

        # --- Crear liquidación ---
        liquidacion = Liquidacion(
            id_contrato=id_contrato,
            id_motivo_terminacion=id_motivo_terminacion,
            fecha_liquidacion=date.today(),
            total_liquidacion=total
        )

        self.db.add(liquidacion)
        self.db.commit()
        self.db.refresh(liquidacion)

        # --- Crear detalles ---
        detalles = [
            ("Cesantías", cesantias),
            ("Intereses de Cesantías", intereses_cesantias),
            ("Vacaciones", vacaciones),
            ("Prima de servicios", prima),
        ]

        if indemnizacion > 0:
            detalles.append(("Indemnización por despido sin justa causa", indemnizacion))

        for concepto, valor in detalles:
            detalle = DetalleLiquidacion(
                id_liquidacion=liquidacion.id_liquidacion,
                concepto=concepto,
                valor=valor
            )
            self.db.add(detalle)

        self.db.commit()

        return {
            "id_liquidacion": liquidacion.id_liquidacion,
            "fecha_liquidacion": liquidacion.fecha_liquidacion,
            "total_liquidacion": float(total),
            "detalles": [{"concepto": c, "valor": float(v)} for c, v in detalles]
        }

    def calcular_indemnizacion(self, dias_trabajados: int, salario: float) -> float:
        """
        Cálculo simple de indemnización:
        - Hasta 1 año: 1 mes de salario
        - Más de 1 año: 1 mes + 20 días por cada año adicional
        """
        años = dias_trabajados / 360
        if años <= 1:
            return salario
        else:
            # 1 mes por el primer año + 20 días por cada año adicional
            return salario + ((años - 1) * (salario / 30) * 20)
