import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Register = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    nombre: '',
    apellido: '',
    tipoDocumento: '',
    numeroDocumento: '',
    fechaNacimiento: '',
    correo: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validación simple del correo
    if (!formData.correo.includes('@')) {
      alert('El correo debe contener @');
      return;
    }

    alert('¡Registro exitoso!');
    navigate('/major'); 
  };

  return (
    <div style={styles.container}>
      <h2>Registro de Usuario</h2>
      <form onSubmit={handleSubmit} style={styles.form}>
        <label>Nombre:</label>
        <input type="text" name="nombre" onChange={handleChange} required />

        <label>Apellido:</label>
        <input type="text" name="apellido" onChange={handleChange} required />

        <label>Tipo de Documento:</label>
        <select name="tipoDocumento" onChange={handleChange} required>
          <option value="">Seleccione...</option>
          <option value="CC">Cédula de Ciudadanía</option>
          <option value="CE">Cédula Extranjera</option>
        </select>

        <label>Número de Documento:</label>
        <input type="number" name="numeroDocumento" onChange={handleChange} required />

        <label>Fecha de Nacimiento:</label>
        <input type="date" name="fechaNacimiento" onChange={handleChange} required />

        <label>Correo Electrónico:</label>
        <input type="email" name="correo" onChange={handleChange} required />

        <button type="submit" style={styles.button}>Registrarse</button>
      </form>
    </div>
  );
};

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '100vh',
    backgroundColor: '#f5f5f5',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    width: '300px',
    gap: '10px',
  },
  button: {
    marginTop: '10px',
    padding: '10px',
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
};

export default Register;
