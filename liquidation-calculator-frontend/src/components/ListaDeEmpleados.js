// src/components/ListaDeEmpleados.js
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; // Importa Link para navegar

function ListaDeEmpleados() {
  const [empleados, setEmpleados] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/empleados')
      .then(response => {
        if (!response.ok) {
          throw new Error('No se pudo obtener la lista de empleados.');
        }
        return response.json();
      })
      .then(data => {
        setEmpleados(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Cargando empleados...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Lista de Empleados</h1>
      <ul>
        {empleados.map(empleado => (
          <li key={empleado.id_empleado}>
            {empleado.nombres} {empleado.apellidos} ({empleado.documento})
            {/* Agrega un enlace al detalle del empleado */}
            <Link to={`/empleados/${empleado.id_empleado}`}>Ver Detalles</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListaDeEmpleados;
