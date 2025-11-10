import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Home.css';
import calculo from '../../assets/presupuesto.png';
import liquidacion_segura from '../../assets/liquidacion_segura.jpg'
import registro from '../../assets/registro.png';
import libro from '../../assets/libro-de-lectura.png';

const Home = () => {
  const navigate = useNavigate();
  const token = sessionStorage.getItem('token');
  const user = JSON.parse(sessionStorage.getItem('user') || '{}');
  const isLoggedIn = !!token;

  const handleLogout = () => {
    sessionStorage.removeItem('token');
    sessionStorage.removeItem('user');
    window.location.reload();
  };

  const handleStart = () => {
    navigate('/contract');
  };

  return (
    <div className="home-container">
      <nav className="navbar">
        <div className="nav-brand">
          <img src={liquidacion_segura} alt="Liquidación Segura Logo" className="logo-image" />
        </div>
        <div className="nav-links">
          {isLoggedIn ? (
            <>
              <span className="welcome-text">
                Hola, <strong>{user.username || 'Usuario'}</strong>
              </span>
              <button onClick={handleLogout} className="nav-link nav-link-logout">
                Cerrar Sesión
              </button>
            </>
          ) : (
            <>
              <Link to="/login" className="nav-link">Iniciar Sesión</Link>
              <Link to="/register" className="nav-link nav-link-primary">Registrarse</Link>
            </>
          )}
        </div>
      </nav>

      <div className="hero-section">
        <div className="hero-content">
          <h1>Bienvenido a <span className="highlight">Liquidación Segura</span></h1>
          <p>
            Somos tu aliado confiable en el cálculo de liquidaciones laborales, ofreciendo
            rapidez, seguridad y precisión para que siempre recibas lo que te corresponde.
          </p>

          {!isLoggedIn ? (
            <div className="hero-buttons">
              <Link to="/register" className="hero-button primary">Comenzar Ahora</Link>
              <Link to="/login" className="hero-button secondary">Iniciar Sesión</Link>
            </div>
          ) : (
            <div className="hero-buttons">
              <button className="hero-button primary" onClick={handleStart}>
                Empieza ahora
              </button>
            </div>
          )}
        </div>
      </div>

      {isLoggedIn && (
        <section className="features-section">
          <h1>
            Con Liquidación Segura no solo calculas cifras, también obtienes tranquilidad y respaldo.
            Nuestro compromiso es ofrecerte claridad y confianza en cada resultado, asegurando que tus
            derechos laborales estén protegidos y que recibas lo que realmente te corresponde.
          </h1>

          <div className="features-grid">
            {/* Registrar Contrato */}
            <Link to="/contract" className="feature-card">
              <img src={registro} alt="Registrar Contrato" className="feature-image" />
              <h3>Registrar Contrato</h3>
              <p>
                Crea un nuevo contrato laboral ingresando los datos del empleado y las condiciones
                del acuerdo. Este será el punto de partida para calcular futuras liquidaciones.
              </p>
            </Link>

            {/* Calcular Liquidación */}
            <Link to="/liquidation" className="feature-card">
              <img src={calculo} alt="Calcular Liquidación" className="feature-image" />
              <h3>Calcular Liquidación</h3>
              <p>
                Genera de forma automática la liquidación de un contrato con base en las fechas,
                salario y motivo de terminación. Precisión total, sin complicaciones.
              </p>
            </Link>

            {/* Ver Mis Liquidaciones */}
            <Link to="/myliquidations" className="feature-card">
              <img src={libro} alt="Ver Mis Liquidaciones" className="feature-image" />
              <h3>Ver Mis Liquidaciones</h3>
              <p>
                Consulta el historial de todas las liquidaciones realizadas, con detalles
                completos de cada cálculo y sus conceptos asociados.
              </p>
            </Link>
          </div>
        </section>
      )}
    </div>
  );
};

export default Home;
