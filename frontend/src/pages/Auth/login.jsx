import React, { useState, useEffect } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import './Auth.css';
import logo from "../../assets/liquidacion_segura.jpg";
import { loginUser, setToken } from '../../services/AuthService'; 

const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  const { email, password } = formData;

  // ✅ Función para manejar cambios en los inputs
  const onChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  useEffect(() => {
    const urlEmail = searchParams.get('email');
    const fromRegister = searchParams.get('fromRegister');
    
    if (urlEmail) {
      setFormData(prev => ({ ...prev, email: decodeURIComponent(urlEmail) }));
    }
    
    if (fromRegister) {
      setSuccessMessage('¡Registro exitoso! Ahora inicia sesión con tus credenciales.');
    }
  }, [searchParams]);

  const onSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');
    setSuccessMessage('');

    try {
      const resp = await loginUser({ email, password });

      if (resp.ok) {
        const data = resp.data;

        // Extraemos los datos que vienen desde el backend
        const token = data?.access_token || data?.token;
        const userData = {
          id: data?.id,
          username: data?.username,
          email: data?.email,
        };

        // Guardar token en el AuthService
        if (token) {
          setToken(token);
        }

        // 🔥 Guardar todo en sessionStorage
        sessionStorage.setItem('token', token);
        sessionStorage.setItem('user', JSON.stringify(userData));

        // Navegamos al home
        navigate('/');
      } else {
        setError(resp.message || 'Credenciales incorrectas');
      }
    } catch (err) {
      setError(err?.response?.data?.detail || 'Error de conexión');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="auth-container">
      {/* 🔹 Botón arriba a la izquierda */}
            <Link to="/" className="back-home-top">
              ⬅️ Volver al Home
            </Link>
      <div className="auth-card">
        <div className="logo">
          <img src={logo} alt="SINTIENDO Logo" className="logo-image" />
        </div>
        
        <h2>Iniciar Sesión</h2>
        <p className="auth-subtitle">Liquidación Segura: rápida, clara y confiable</p>
        
        {successMessage && <div className="success-message">{successMessage}</div>}
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={onSubmit}>
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
          <button 
            type="submit" 
            className="auth-button"
            disabled={isLoading}
          >
            {isLoading ? 'Iniciando sesión...' : 'Iniciar Sesión'}
          </button>
        </form>
        
        <p className="auth-link">
          ¿No tienes una cuenta? <Link to="/register">Regístrate aquí</Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
