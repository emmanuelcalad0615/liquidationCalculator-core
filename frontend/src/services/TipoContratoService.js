import api from "./api";

// Crear un nuevo tipo de contrato
export const createTipoContrato = async (payload) => {
  try {
    const response = await api.post("/tipo_contrato/", payload);
    return { ok: true, data: response.data };
  } catch (error) {
    return handleError(error);
  }
};

// Obtener todos los tipos de contrato
export const getAllTipoContratos = async () => {
  try {
    const response = await api.get("/tipo_contrato/");
    return { ok: true, data: response.data };
  } catch (error) {
    return handleError(error);
  }
};

// Obtener un tipo de contrato por ID
export const getTipoContratoById = async (id) => {
  try {
    const response = await api.get(`/tipo_contrato/${id}`);
    return { ok: true, data: response.data };
  } catch (error) {
    return handleError(error);
  }
};

// Actualizar un tipo de contrato
export const updateTipoContrato = async (id, payload) => {
  try {
    const response = await api.put(`/tipo_contrato/${id}`, payload);
    return { ok: true, data: response.data };
  } catch (error) {
    return handleError(error);
  }
};

// Eliminar un tipo de contrato
export const deleteTipoContrato = async (id) => {
  try {
    await api.delete(`/tipo_contrato/${id}`);
    return { ok: true };
  } catch (error) {
    return handleError(error);
  }
};

// 🔧 Función de manejo de errores reutilizable
const handleError = (error) => {
  console.error("Error en TipoContratoService:", error);
  return {
    ok: false,
    message:
      error.response?.data?.detail ||
      "Error de conexión o respuesta inesperada del servidor",
  };
};
