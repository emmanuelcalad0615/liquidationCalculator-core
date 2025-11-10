import api from "./api";

export const createDetalleLiquidacion = async (data) => {
  try {
    const response = await api.post("/detalle_liquidacion/", data);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al crear detalle de liquidación:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al crear detalle de liquidación",
    };
  }
};

export const getAllDetallesLiquidacion = async () => {
  try {
    const response = await api.get("/detalle_liquidacion/");
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al obtener detalles de liquidación:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al obtener detalles de liquidación",
    };
  }
};

export const getDetalleLiquidacionById = async (id_detalle) => {
  try {
    const response = await api.get(`/detalle_liquidacion/${id_detalle}`);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al obtener detalle de liquidación:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al obtener detalle de liquidación",
    };
  }
};

export const updateDetalleLiquidacion = async (id_detalle, data) => {
  try {
    const response = await api.put(`/detalle_liquidacion/${id_detalle}`, data);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al actualizar detalle de liquidación:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al actualizar detalle de liquidación",
    };
  }
};

export const deleteDetalleLiquidacion = async (id_detalle) => {
  try {
    await api.delete(`/detalle_liquidacion/${id_detalle}`);
    return { ok: true };
  } catch (error) {
    console.error("❌ Error al eliminar detalle de liquidación:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al eliminar detalle de liquidación",
    };
  }
};
