import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';
import liquidacion_segura from '../../assets/liquidacion_segura.jpg';
import escudo from '../../assets/escudo-de-seguridad.png'
import libro from '../../assets/libro-de-lectura.png'
import diana from '../../assets/diana.png'

const Home = () => {
  const isLoggedIn = sessionStorage.getItem('token');
  const user = JSON.parse(sessionStorage.getItem('user') || '{}');

  const handleLogout = () => {
    sessionStorage.removeItem('token');
    sessionStorage.removeItem('user');
    sessionStorage.removeItem('email');
    window.location.reload();
  };

  return (
    <div className="home-container">
      <nav className="navbar">
        <div className="nav-brand">
          <img src={liquidacion_segura} alt="SINTIENDO Logo" className="logo-image" />
        </div>
        <div className="nav-links">
          {isLoggedIn ? (
            <>
              <span className="welcome-text">Hola, {user.user || 'Usuario'}</span>
              <button onClick={handleLogout} className="nav-link nav-link-logout">Cerrar Sesión</button>
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
          <h1>Bienvenido a Liquidación Segura</h1>
          <p>Somos tu aliado confiable en el cálculo de liquidaciones laborales, ofreciendo rapidez, seguridad y precisión para que siempre recibas lo que te corresponde.</p>
          
          {!isLoggedIn ? (
            <div className="hero-buttons">
              <Link to="/register" className="hero-button primary">Comenzar Ahora</Link>
              <Link to="/login" className="hero-button secondary">Iniciar Sesión</Link>
            </div>
          ) : (
            <div className="hero-buttons">
              <button className="hero-button primary">Empieza ahora</button>
            </div>
          )}
        </div>
      </div>
      
      <section className="features-section">
        <h1>Con Liquidación Segura no solo calculas cifras, también obtienes tranquilidad y respaldo. Nuestro compromiso es ofrecerte claridad y confianza en cada resultado, asegurando que tus derechos laborales estén protegidos y que recibas lo que realmente te corresponde.</h1>
        <div className="features-grid">
          <div className="feature-card">
            <img src = {diana}alt="Colores que hablan" className="feature-image" />
            <h3>Cálculo Rápido y Preciso</h3>
            <p>Olvídate de las dudas y los cálculos a mano. Nuestra herramienta hace el trabajo por ti en segundos, con total exactitud.</p>
          </div>
          <div className="feature-card">
            <img src = {libro} alt="Así me siento" className="feature-image" />
            <h3>Transparencia Total</h3>
            <p>Te mostramos el paso a paso de tu liquidación, para que entiendas cada valor y tengas la seguridad de que recibes lo justo.</p>
          </div>
          <div className="feature-card">
            <img src = {escudo} alt="Emociones en orden" className="feature-image" />
            <h3>Seguridad y Confianza</h3>
            <p>Tus datos están protegidos con los más altos estándares de seguridad, garantizando un proceso confiable y sin riesgos.</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;