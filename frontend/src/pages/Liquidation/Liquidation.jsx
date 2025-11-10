import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./Liquidation.css";
import { getAllMotivosTerminacion } from "../../services/MotivoTerminacionService";
import { calcularLiquidacion } from "../../services/calcLiquidacionService";
import { getContratosByEmpleado } from "../../services/ContratoService";

const Liquidaciones = () => {
  const [form, setForm] = useState({
    id_contrato: "",
    id_motivo_terminacion: "",
  });
  const [motivos, setMotivos] = useState([]);
  const [contratos, setContratos] = useState([]);
  const [resultado, setResultado] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // 🔹 Cargar motivos de terminación
  useEffect(() => {
    const fetchMotivos = async () => {
      try {
        const res = await getAllMotivosTerminacion();
        if (res.ok) setMotivos(res.data);
        else console.error("Error cargando motivos:", res.message);
      } catch (err) {
        console.error("Error de conexión:", err);
      }
    };
    fetchMotivos();
  }, []);

  // 🔹 Cargar contratos del empleado autenticado
  useEffect(() => {
    const fetchContratos = async () => {
      const user = JSON.parse(sessionStorage.getItem("user"));
      if (!user || !user.id) {
        console.warn("⚠️ No se encontró el usuario autenticado");
        return;
      }
      try {
        const res = await getContratosByEmpleado(user.id);
        if (res.ok) setContratos(res.data);
        else console.error("Error cargando contratos:", res.message);
      } catch (err) {
        console.error("Error al cargar contratos:", err);
      }
    };
    fetchContratos();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResultado(null);
    setLoading(true);

    try {
      const data = await calcularLiquidacion(
        Number(form.id_contrato),
        Number(form.id_motivo_terminacion)
      );
      setResultado(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="liquidacion-page">
      {/* 🔹 Botón arriba a la izquierda */}
      <Link to="/" className="back-home-top">
        ⬅️ Volver al Home
      </Link>

      <div className="auth-container">
        <div className="auth-card">
          <h2 className="auth-title">💰 Calcular Liquidación</h2>

          <form onSubmit={handleSubmit} className="auth-form">
            <div className="form-group">
              <label>Contrato</label>
              <select
                name="id_contrato"
                value={form.id_contrato}
                onChange={handleChange}
                required
              >
                <option value="">Selecciona un contrato</option>
                {contratos.map((c) => (
                  <option key={c.id_contrato} value={c.id_contrato}>
                    Contrato del {c.fecha_inicio} al{" "}
                    {c.fecha_fin || "sin fecha fin"}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label>Motivo de Terminación</label>
              <select
                name="id_motivo_terminacion"
                value={form.id_motivo_terminacion}
                onChange={handleChange}
                required
              >
                <option value="">Selecciona uno</option>
                {motivos.map((motivo) => (
                  <option
                    key={motivo.id_motivo_terminacion}
                    value={motivo.id_motivo_terminacion}
                  >
                    {motivo.descripcion}
                  </option>
                ))}
              </select>
            </div>

            <button type="submit" className="auth-button" disabled={loading}>
              {loading ? "Calculando..." : "Calcular Liquidación"}
            </button>
          </form>

          

          {error && <p className="error-message">⚠️ {error}</p>}

          {resultado && (
            <div className="resultado-card">
              <h3>🧾 Resultado</h3>
              <p>
                <strong>Fecha:</strong> {resultado.fecha_liquidacion}
              </p>
              <p>
                <strong>Total:</strong>{" "}
                ${resultado.total_liquidacion.toLocaleString()}
              </p>
              <hr />
              <ul>
                {resultado.detalles?.map((d, i) => (
                  <li key={i}>
                    <strong>{d.concepto}:</strong> ${d.valor.toLocaleString()}
                  </li>
                ))}
              </ul>
            </div>
          )}

          <p className="auth-link">
            ¿Deseas registrar un contrato?{" "}
            <Link to="/contract">Ir a Contratos</Link>
          </p>
          <p className="auth-link" style={{ marginTop: "1rem" }}>
            ¿Ya tienes liquidaciones registradas?{" "}
            <Link to="/myliquidations">Ver Mis Liquidaciones</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Liquidaciones;
