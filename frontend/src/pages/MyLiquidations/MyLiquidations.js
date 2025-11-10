import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./MyLiquidations.css";
import { getAllLiquidaciones } from "../../services/LiquidacionService";
import { getContratosByEmpleado } from "../../services/ContratoService";
import { deleteLiquidacion } from "../../services/LiquidacionService";

const MisLiquidaciones = () => {
  const [liquidaciones, setLiquidaciones] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // 🔹 Cargar las liquidaciones del empleado autenticado
  useEffect(() => {
    const fetchLiquidaciones = async () => {
      try {
        const user = JSON.parse(sessionStorage.getItem("user"));
        if (!user || !user.id) {
          setError("⚠️ No se encontró el usuario autenticado.");
          setLoading(false);
          return;
        }

        // Obtener contratos del empleado
        const contratosRes = await getContratosByEmpleado(user.id);
        if (!contratosRes.ok) {
          throw new Error("Error al cargar contratos.");
        }

        const contratos = contratosRes.data;
        let todasLiquidaciones = [];

        // 🔹 Obtener liquidaciones asociadas a cada contrato
        for (const contrato of contratos) {
          const res = await getAllLiquidaciones();
          if (res.ok) {
            const filtradas = res.data.filter(
              (l) => l.id_contrato === contrato.id_contrato
            );
            todasLiquidaciones = [...todasLiquidaciones, ...filtradas];
          }
        }

        setLiquidaciones(todasLiquidaciones);
      } catch (err) {
        setError("Error al cargar las liquidaciones.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchLiquidaciones();
  }, []);

  const handleDelete = async (id_liquidacion) => {
    if (
      !window.confirm(
        "¿Seguro que deseas eliminar esta liquidación? Esta acción no se puede deshacer."
      )
    )
      return;

    try {
      const res = await deleteLiquidacion(id_liquidacion);
      if (res.ok) {
        setLiquidaciones((prev) =>
          prev.filter((l) => l.id_liquidacion !== id_liquidacion)
        );
      } else {
        alert("❌ No se pudo eliminar la liquidación.");
      }
    } catch (err) {
      console.error("Error eliminando:", err);
    }
  };

  if (loading)
    return (
      <div className="auth-container">
        <div className="auth-card">
          <h3>Cargando tus liquidaciones...</h3>
        </div>
      </div>
    );

  if (error)
    return (
      <div className="auth-container">
        <div className="auth-card">
          <p className="error-message">{error}</p>
        </div>
      </div>
    );

  return (
    <div className="liquidacion-page">
      {/* 🔹 Botón arriba a la izquierda */}
      <Link to="/" className="back-home-top">
        ⬅️ Volver al Home
      </Link>

      <div className="auth-container">
        <div className="auth-card">
          <h2 className="auth-title">📜 Mis Liquidaciones</h2>

          {liquidaciones.length === 0 ? (
            <p className="no-data">No tienes liquidaciones registradas.</p>
          ) : (
            <div className="liquidacion-list">
              {liquidaciones.map((liq) => (
                <div key={liq.id_liquidacion} className="resultado-card">
                  <div className="resultado-header">
                    <h3>💼 Contrato #{liq.id_contrato}</h3>
                    <button
                      className="delete-btn"
                      onClick={() => handleDelete(liq.id_liquidacion)}
                    >
                      🗑️
                    </button>
                  </div>

                  <p>
                    <strong>Fecha:</strong> {liq.fecha_liquidacion}
                  </p>
                  <p>
                    <strong>Motivo:</strong>{" "}
                    {liq.motivo_terminacion?.descripcion || "No especificado"}
                  </p>
                  <p>
                    <strong>Total:</strong>{" "}
                    ${liq.total_liquidacion.toLocaleString()}
                  </p>
                  <hr />
                  <ul>
                    {liq.detalles_liquidacion && liq.detalles_liquidacion.length > 0 ? (
                      liq.detalles_liquidacion.map((d, i) => (
                        <li key={i}>
                          <strong>{d.concepto}:</strong> ${d.valor.toLocaleString()}
                        </li>
                      ))
                    ) : (
                      <li>No hay detalles registrados.</li>
                    )}

                  </ul>
                </div>
              ))}
            </div>
          )}

          <p className="auth-link">
            ¿Quieres calcular una nueva?{" "}
            <Link to="/liquidation">Ir a Calcular</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default MisLiquidaciones;
