import api from "./api";

const handleResponse = async (promise) => {
  try {
    const res = await promise;
    return { ok: true, data: res.data, status: res.status };
  } catch (err) {
    const res = err.response;
    const message =
      res?.data?.detail || res?.data?.message || err.message || "Network error";
    return { ok: false, status: res?.status, message, errors: res?.data };
  }
};

export const loginUser = (credentials) =>
  handleResponse(api.post("/auth/login", credentials));

export const registerUser = (payload) =>
  handleResponse(api.post("/auth/singup", payload));

export const setToken = (token) => sessionStorage.setItem("token", token);
export const getToken = () => sessionStorage.getItem("token");
export const removeToken = () => sessionStorage.removeItem("token");
export const isAuthenticated = () => Boolean(getToken());

export default {
  loginUser,
  registerUser,
  setToken,
  getToken,
  removeToken,
  isAuthenticated,
};
