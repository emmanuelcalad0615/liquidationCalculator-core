import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Auth.css';

import logo from '../../assets/liquidacion_segura.jpg';
import { registerUser } from '../../services/AuthService'; 

const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    password2: '',
    nombres: '',
    apellidos: '',
    tipo_documento: '',
    documento: '',
    fecha_nacimiento: ''
  });
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const {
    username,
    email,
    password,
    password2,
    nombres,
    apellidos,
    tipo_documento,
    documento,
    fecha_nacimiento
  } = formData;

  const onChange = e =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = async e => {
    e.preventDefault();

    if (password !== password2) {
      setError('Las contraseñas no coinciden');
      return;
    }

    setIsLoading(true);
    setError('');

    const payload = {
      username,
      email,
      password,
      empleado: {
        nombres,
        apellidos,
        tipo_documento: Number(tipo_documento), // aseguramos que sea número
        documento,
        fecha_nacimiento
      }
    };

    const res = await registerUser(payload);
    console.log("Payload enviado:", payload);

    if (res.ok) {
      sessionStorage.setItem('registrationData', JSON.stringify(payload));
      navigate(`/login?email=${encodeURIComponent(email)}&fromRegister=true`);
    } else {
      if (Array.isArray(res)) {
        setError(res.map(err => `${err.loc.join('.')} → ${err.msg}`).join(', '));
      } else if (res.detail && Array.isArray(res.detail)) {
        setError(res.detail.map(err => `${err.loc.join('.')} → ${err.msg}`).join(', '));
      } else {
        setError(res.message || 'Error al crear la cuenta');
      }
    }

    setIsLoading(false);
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="logo">
          <img src={logo} alt="Liquidación Segura Logo" className="logo-image" />
        </div>

        <h2>Crear Cuenta</h2>
        <p className="auth-subtitle">
          Únete a Liquidación Segura y vive la tranquilidad de recibir lo justo.
        </p>

        {error && <div className="error-message">{JSON.stringify(error)}</div>}

        <form onSubmit={onSubmit}>
          {/* Datos de acceso */}
          

          {/* Datos del empleado */}
          <div className="form-group">
            <label htmlFor="nombres">Nombres</label>
            <input
              type="text"
              id="nombres"
              placeholder="Tus nombres"
              name="nombres"
              value={nombres}
              onChange={onChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="apellidos">Apellidos</label>
            <input
              type="text"
              id="apellidos"
              placeholder="Tus apellidos"
              name="apellidos"
              value={apellidos}
              onChange={onChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="tipo_documento">Tipo de documento</label>
            <select
              id="tipo_documento"
              name="tipo_documento"
              value={tipo_documento}
              onChange={onChange}
              required
            >
              <option value="">Selecciona...</option>
              <option value="0">Cédula de Ciudadanía</option>
              <option value="1">Tarjeta de Identidad</option>
              <option value="2">Cédula de Extranjería</option>
              <option value="3">Pasaporte</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="documento">Número de documento</label>
            <input
              type="text"
              id="documento"
              placeholder="Número de documento"
              name="documento"
              value={documento}
              onChange={onChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="fecha_nacimiento">Fecha de nacimiento</label>
            <input
              type="date"
              id="fecha_nacimiento"
              name="fecha_nacimiento"
              value={fecha_nacimiento}
              onChange={onChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="username">Usuario</label>
            <input
              type="text"
              id="username"
              placeholder="Nombre de usuario"
              name="username"
              value={username}
              onChange={onChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="email">Correo electrónico</label>
            <input
              type="email"
              id="email"
              placeholder="tu@email.com"
              name="email"
              value={email}
              onChange={onChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Contraseña</label>
            <input
              type="password"
              id="password"
              placeholder="••••••••"
              name="password"
              value={password}
              onChange={onChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password2">Confirmar contraseña</label>
            <input
              type="password"
              id="password2"
              placeholder="••••••••"
              name="password2"
              value={password2}
              onChange={onChange}
              required
            />
          </div>

          <button type="submit" className="auth-button" disabled={isLoading}>
            {isLoading ? 'Creando cuenta...' : 'Registrarse'}
          </button>
        </form>

        <p className="auth-link">
          ¿Ya tienes una cuenta? <Link to="/login">Inicia sesión aquí</Link>
        </p>
      </div>
    </div>
  );
};

export default Register;
