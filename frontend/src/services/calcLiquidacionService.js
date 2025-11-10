import api from "./api"; // importa tu base de servicios

/**
 * Servicio para calcular la liquidación de un contrato.
 * @param {number} id_contrato - ID del contrato a liquidar.
 * @param {number} id_motivo_terminacion - ID del motivo de terminación.
 * @returns {Promise<Object>} Datos de la liquidación calculada.
 */
export const calcularLiquidacion = async (id_contrato, id_motivo_terminacion) => {
  try {
    const response = await api.post("/calc_liquidaciones/calcular", {
      id_contrato,
      id_motivo_terminacion,
    });
    return response.data;
  } catch (error) {
    if (error.response) {
      throw new Error(error.response.data.detail || "Error al calcular la liquidación.");
    } else {
      throw new Error("Error de conexión con el servidor.");
    }
  }
};
