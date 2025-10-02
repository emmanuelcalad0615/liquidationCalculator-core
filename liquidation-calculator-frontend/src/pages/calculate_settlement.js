import React, { useState } from "react";
import { Link } from 'react-router-dom';


const Calculate_settlement = () => {
  // Estados de los campos
  const [salario, setSalario] = useState("");
  const [auxilio, setAuxilio] = useState("");
  const [dias, setDias] = useState("");

  // Resultados
  const [cesantias, setCesantias] = useState(null);
  const [interesesCesantias, setInteresesCesantias] = useState(null);
  const [prima, setPrima] = useState(null);
  const [vacaciones, setVacaciones] = useState(null);
  const [liquidacionTotal, setLiquidacionTotal] = useState(null);

  // Indemnización
  const [compensate, setCompensate] = useState("no");
  const [contractType, setContractType] = useState("fijo_1_año");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [indemnizacion, setIndemnizacion] = useState(null);

  const [error, setError] = useState("");
  const [errorIndemnizacion, setErrorIndemnizacion] = useState("");

  // Calcular liquidación
  const handleCalcular = () => {
    setError("");
    if (!salario || !auxilio || !dias) {
      setError("Todos los campos son obligatorios.");
      return;
    }

    try {
      const s = parseFloat(salario);
      const a = parseFloat(auxilio);
      const d = parseInt(dias);

      if (s < 0 || a < 0 || d < 0) throw new Error("Todos los valores deben ser positivos.");

      const totalSalario = s + a;
      const c = totalSalario * (d / 360);
      const i = (c * d * 0.12) / 360;
      const p = totalSalario * (d / 360);
      const v = (s * d) / 720;
      const lt = c + i + p + v;

      setCesantias(c.toFixed(2));
      setInteresesCesantias(i.toFixed(2));
      setPrima(p.toFixed(2));
      setVacaciones(v.toFixed(2));
      setLiquidacionTotal(lt.toFixed(2));
    } catch (err) {
      setError(`Error: ${err.message}`);
    }
  };

  // Calcular indemnización
  const handleIndemnizacion = () => {
    setErrorIndemnizacion("");
    if (!startDate || !endDate) {
      setErrorIndemnizacion("Las fechas de inicio y finalización son obligatorias.");
      return;
    }

    const inicio = new Date(startDate);
    const fin = new Date(endDate);
    if (inicio > fin) {
      setErrorIndemnizacion("La fecha de inicio no puede ser mayor que la fecha de finalización.");
      return;
    }

    const mesesTrabajados =
      (fin.getFullYear() - inicio.getFullYear()) * 12 +
      (fin.getMonth() - inicio.getMonth()) +
      (fin.getDate() - inicio.getDate()) / 30;

    let ind = 0;
    const s = parseFloat(salario);

    switch (contractType) {
      case "fijo_1_año":
        ind = s * (mesesTrabajados / 12);
        break;
      case "fijo_inferior_1_año":
        ind = s * (mesesTrabajados * 0.75) / 12;
        break;
      case "indefinido":
        ind = s * (mesesTrabajados / 12);
        break;
      default:
        setErrorIndemnizacion("Tipo de contrato no válido.");
        return;
    }

    setIndemnizacion(ind.toFixed(2));
  };

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <div style={styles.cards}>
          <div style={styles.card}>
             <Link to="/major" style={styles.link}>
              <h3>Inicio</h3>
            </Link>  
          </div> 
          <div style={styles.card}>
             <Link to="/about" style={styles.link}>
              <h3>Acerca</h3>
            </Link>  
          </div>           
          <div style={styles.card}>
            <Link to="/profile" style={styles.link}>
              <h3>Perfil</h3>
            </Link>
            
          </div>
                  
          <div style={styles.card}>
             <Link to="/calculate" style={styles.link}>
              <h3>Calcular liquidacion</h3>
            </Link>        
            
          </div>
          <div style={styles.card}>
             <Link to="/how_it_works" style={styles.link}>
              <h3>Como funciona</h3>
            </Link>
            
          </div>   
            
        </div>
      </header>

      <main style={styles.main}>
        <h2>Ingresa los datos</h2>

        <div style={styles.form}>
          <label>Salario Mínimo:</label>
          <input
            type="number"
            value={salario}
            onChange={(e) => setSalario(e.target.value)}
          />

          <label>Auxilio de Transporte:</label>
          <input
            type="number"
            value={auxilio}
            onChange={(e) => setAuxilio(e.target.value)}
          />

          <label>Días Trabajados:</label>
          <input
            type="number"
            value={dias}
            onChange={(e) => setDias(e.target.value)}
          />

          <button onClick={handleCalcular}>Calcular</button>
          {error && <p style={styles.error}>{error}</p>}
        </div>

        {liquidacionTotal && (
          <div style={styles.result}>
            <h3>Resultados:</h3>
            <p>Cesantías: ${cesantias}</p>
            <p>Intereses de Cesantías: ${interesesCesantias}</p>
            <p>Prima de Servicios: ${prima}</p>
            <p>Vacaciones: ${vacaciones}</p>
            <p>Liquidación Total: ${liquidacionTotal}</p>

            <div>
              <label>¿Debe ser indemnizado?</label>
              <select
                value={compensate}
                onChange={(e) => setCompensate(e.target.value)}
              >
                <option value="no">No</option>
                <option value="si">Sí</option>
              </select>
            </div>

            {compensate === "si" && (
              <div style={styles.indemnizacion}>
                <label>Tipo de contrato:</label>
                <select
                  value={contractType}
                  onChange={(e) => setContractType(e.target.value)}
                >
                  <option value="fijo_1_año">Fijo 1 Año</option>
                  <option value="fijo_inferior_1_año">Fijo Inferior a 1 Año</option>
                  <option value="indefinido">Indefinido</option>
                </select>

                <label>Fecha de inicio:</label>
                <input
                  type="date"
                  value={startDate}
                  onChange={(e) => setStartDate(e.target.value)}
                />

                <label>Fecha de finalización:</label>
                <input
                  type="date"
                  value={endDate}
                  onChange={(e) => setEndDate(e.target.value)}
                />

                <button onClick={handleIndemnizacion}>Calcular Indemnización</button>
                {errorIndemnizacion && (
                  <p style={styles.error}>{errorIndemnizacion}</p>
                )}

                {indemnizacion && (
                  <p>Indemnización: ${indemnizacion}</p>
                )}
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  );
};

const styles = {
  container: {
    fontFamily: "Poppins, sans-serif",
    backgroundColor: "#f9f9f9",
    minHeight: "100vh",
    padding: "20px",
  },
  header: {
    backgroundColor: "#0ac2d2",
    color: "#fff",
    padding: "20px",
    textAlign: "center",
  },
  main: {
    maxWidth: "600px",
    margin: "20px auto",
    backgroundColor: "#fff",
    padding: "20px",
    borderRadius: "10px",
    boxShadow: "0 4px 8px rgba(0,0,0,0.1)",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "15px",
  },
  result: {
    marginTop: "20px",
    textAlign: "left",
  },
  indemnizacion: {
    marginTop: "20px",
    textAlign: "left",
  },
  error: {
    color: "red",
    fontWeight: "bold",
  },
  link: {
    textDecoration: 'none',
    color: '#4CAF50',
    fontWeight: 'bold',
  },
  card: {
    backgroundColor: '#fff',
    padding: '20px',
    width: '200px',
    borderRadius: '8px',
    boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
  },
  cards: {
    display: 'flex',
    justifyContent: 'center',
    gap: '20px',
    flexWrap: 'wrap',
    marginTop: '30px',
  },
};

export default Calculate_settlement;


