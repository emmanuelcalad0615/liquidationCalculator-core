import api from "./api";

const BASE_URL = "/motivo_terminacion";

// ✅ Obtener todos los motivos de terminación
export const getAllMotivosTerminacion = async () => {
  try {
    const response = await api.get(BASE_URL);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("Error al obtener los motivos:", error);
    return { ok: false, message: error.response?.data?.detail || "Error al obtener los motivos" };
  }
};

// ✅ Obtener un motivo por ID
export const getMotivoTerminacionById = async (id) => {
  try {
    const response = await api.get(`${BASE_URL}/${id}`);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("Error al obtener el motivo:", error);
    return { ok: false, message: error.response?.data?.detail || "Error al obtener el motivo" };
  }
};

// ✅ Crear un nuevo motivo
export const createMotivoTerminacion = async (payload) => {
  try {
    const response = await api.post(BASE_URL, payload);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("Error al crear motivo:", error);
    return { ok: false, message: error.response?.data?.detail || "Error al crear motivo" };
  }
};

// ✅ Actualizar motivo existente
export const updateMotivoTerminacion = async (id, payload) => {
  try {
    const response = await api.put(`${BASE_URL}/${id}`, payload);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("Error al actualizar motivo:", error);
    return { ok: false, message: error.response?.data?.detail || "Error al actualizar motivo" };
  }
};

// ✅ Eliminar motivo
export const deleteMotivoTerminacion = async (id) => {
  try {
    await api.delete(`${BASE_URL}/${id}`);
    return { ok: true };
  } catch (error) {
    console.error("Error al eliminar motivo:", error);
    return { ok: false, message: error.response?.data?.detail || "Error al eliminar motivo" };
  }
};
