import api from "./api";

export const createLiquidacion = async (data) => {
  try {
    const response = await api.post("/liquidacion/", data);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al crear liquidación:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al crear liquidación",
    };
  }
};

export const getAllLiquidaciones = async () => {
  try {
    const response = await api.get("/liquidacion/");
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al obtener liquidaciones:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al obtener liquidaciones",
    };
  }
};

export const getLiquidacionById = async (id_liquidacion) => {
  try {
    const response = await api.get(`/liquidacion/${id_liquidacion}`);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al obtener liquidación:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al obtener liquidación",
    };
  }
};

export const updateLiquidacion = async (id_liquidacion, data) => {
  try {
    const response = await api.put(`/liquidacion/${id_liquidacion}`, data);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al actualizar liquidación:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al actualizar liquidación",
    };
  }
};

export const deleteLiquidacion = async (id_liquidacion) => {
  try {
    await api.delete(`/liquidacion/${id_liquidacion}`);
    return { ok: true };
  } catch (error) {
    console.error("❌ Error al eliminar liquidación:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al eliminar liquidación",
    };
  }
};
