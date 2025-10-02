import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../logo.svg';

function Home() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Bienvenido a la calculadora de liquidación!!!</p>

        <Link to="/register" className="App-link">
          Registrarse
        </Link>
      </header>
    </div>
  );
}

export default Home;

