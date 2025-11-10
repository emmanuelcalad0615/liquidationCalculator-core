import api from "./api";

// ✅ Crear contrato
export const createContrato = async (data) => {
  try {
    const response = await api.post("/contrato/", data);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al crear contrato:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al crear contrato",
    };
  }
};

// ✅ Obtener todos los contratos
export const getAllContratos = async () => {
  try {
    const response = await api.get("/contrato/");
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al obtener contratos:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al obtener contratos",
    };
  }
};

// ✅ Obtener contrato por ID
export const getContratoById = async (id_contrato) => {
  try {
    const response = await api.get(`/contrato/${id_contrato}`);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al obtener contrato:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al obtener contrato",
    };
  }
};

// ✅ Obtener contratos por ID de empleado
export const getContratosByEmpleado = async (id_empleado) => {
  try {
    const response = await api.get(`/contrato/empleado/${id_empleado}`);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al obtener contratos por empleado:", error);
    return {
      ok: false,
      message:
        error.response?.data?.detail ||
        "Error al obtener contratos del empleado",
    };
  }
};

// ✅ Actualizar contrato
export const updateContrato = async (id_contrato, data) => {
  try {
    const response = await api.put(`/contrato/${id_contrato}`, data);
    return { ok: true, data: response.data };
  } catch (error) {
    console.error("❌ Error al actualizar contrato:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al actualizar contrato",
    };
  }
};

// ✅ Eliminar contrato
export const deleteContrato = async (id_contrato) => {
  try {
    await api.delete(`/contrato/${id_contrato}`);
    return { ok: true };
  } catch (error) {
    console.error("❌ Error al eliminar contrato:", error);
    return {
      ok: false,
      message: error.response?.data?.detail || "Error al eliminar contrato",
    };
  }
};
