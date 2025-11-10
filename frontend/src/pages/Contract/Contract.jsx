import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getAllTipoContratos } from "../../services/TipoContratoService";
import { createContrato } from "../../services/ContratoService";
import "./Contract.css";

const Contratos = () => {
  const [form, setForm] = useState({
    id_empleado: "",
    id_tipo_contrato: "",
    fecha_inicio: "",
    fecha_fin: "",
    salario_mensual: "",
    auxilio_transporte: "",
  });

  const [tiposContrato, setTiposContrato] = useState([]);
  const [mensaje, setMensaje] = useState("");

  // ✅ Cargar id_empleado del sessionStorage
  useEffect(() => {
    const user = JSON.parse(sessionStorage.getItem("user"));
    if (user && user.id) {
      setForm((prev) => ({ ...prev, id_empleado: user.id }));
    } else {
      console.warn("⚠️ No se encontró el usuario autenticado en sessionStorage");
    }
  }, []);

  // ✅ Cargar tipos de contrato desde el backend
  useEffect(() => {
    const fetchTiposContrato = async () => {
      const res = await getAllTipoContratos();
      if (res.ok) setTiposContrato(res.data);
      else console.error("Error cargando tipos de contrato:", res.message);
    };
    fetchTiposContrato();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("📦 Datos enviados:", form);

    const res = await createContrato(form);
    if (res.ok) {
      setMensaje("✅ Contrato registrado correctamente");
      setForm({
        ...form,
        id_tipo_contrato: "",
        fecha_inicio: "",
        fecha_fin: "",
        salario_mensual: "",
        auxilio_transporte: "",
      });
    } else {
      setMensaje("❌ " + res.message);
    }
  };

  return (
    <div className="contract-page">
      {/* 🔹 Botón arriba a la izquierda */}
      <Link to="/" className="back-home-top">
        ⬅️ Volver al Home
      </Link>

      <div className="auth-container">
        <div className="auth-card">
          <h2 className="auth-title">📝 Registrar Contrato</h2>

          <form onSubmit={handleSubmit} className="auth-form">
            <div className="form-group">
              <label>ID Empleado</label>
              <input
                type="number"
                name="id_empleado"
                value={form.id_empleado}
                readOnly
                disabled
                className="input-disabled"
              />
            </div>

            <div className="form-group">
              <label>Tipo de Contrato</label>
              <select
                name="id_tipo_contrato"
                value={form.id_tipo_contrato}
                onChange={handleChange}
                required
              >
                <option value="">Selecciona uno</option>
                {tiposContrato.map((tipo) => (
                  <option key={tipo.id_tipo_contrato} value={tipo.id_tipo_contrato}>
                    {tipo.descripcion}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label>Fecha Inicio</label>
              <input
                type="date"
                name="fecha_inicio"
                value={form.fecha_inicio}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Fecha Fin</label>
              <input
                type="date"
                name="fecha_fin"
                value={form.fecha_fin}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Salario Mensual</label>
              <input
                type="number"
                name="salario_mensual"
                value={form.salario_mensual}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Auxilio de Transporte</label>
              <input
                type="number"
                name="auxilio_transporte"
                value={form.auxilio_transporte}
                onChange={handleChange}
              />
            </div>

            <button type="submit" className="auth-button">
              Guardar Contrato
            </button>
          </form>

          {mensaje && <p className="message">{mensaje}</p>}

          <p className="auth-link">
            ¿Deseas calcular una liquidación?{" "}
            <Link to="/liquidation">Ir a Liquidaciones</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Contratos;
