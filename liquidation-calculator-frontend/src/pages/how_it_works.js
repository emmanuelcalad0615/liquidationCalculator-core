import React from "react";
import { Link } from "react-router-dom";

const HowItWorks = () => {
  return (
    <div style={{ fontFamily: "'Poppins', sans-serif", backgroundColor: "#f9f9f9" }}>
      {/* Header */}
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

      {/* Contenido principal */}
      <main style={styles.main}>
        <div style={styles.container}>
          <h1 style={styles.title}>¿Cómo Funciona la Calculadora de Nómina?</h1>
          <p>
            La calculadora de nómina te permite estimar el monto de tu liquidación
            de manera rápida y sencilla. A continuación, te explicamos los pasos
            básicos de cómo funciona:
          </p>

          <div style={styles.steps}>
            <div style={styles.step}>
              <h2>Paso 1</h2>
              <p><strong>Ingresa tu Información Personal:</strong></p>
              <p>Introduce datos básicos como tu salario, auxilio de transporte, total días trabajados.</p>
            </div>
            <div style={styles.step}>
              <h2>Paso 2</h2>
              <p><strong>Parámetros de Cálculo:</strong></p>
              <p>Tener en cuenta días trabajados y otros conceptos importantes para el cálculo de la nómina.</p>
            </div>
            <div style={styles.step}>
              <h2>Paso 3</h2>
              <p><strong>Calcula tu Liquidación:</strong></p>
              <p>Una vez ingresados los datos, haz clic en "Calcular" para obtener el resultado.</p>
            </div>
          </div>

          {/* Imágenes */}
          <div style={styles.images}>
            <img
              src="https://img.freepik.com/fotos-premium/gente-negocios-o-gente-negocios-usa-calculadoras-computadoras-mesa-oficina_73749-583.jpg"
              alt="Imagen 1"
              style={styles.image}
            />
            <img
              src="https://plus.unsplash.com/premium_photo-1664474858290-12e86f613944?fm=jpg&q=60&w=3000"
              alt="Imagen 2"
              style={styles.image}
            />
          </div>

          {/* Botón volver */}
          <Link to="/major" style={styles.closeBtn}>← Volver al Inicio</Link>
        </div>
      </main>

      {/* Footer */}
      <footer style={styles.footer}>
        <p>Made By: Emmanuel Calad - Sofia Correa</p>
      </footer>
    </div>
  );
};

const styles = {
 header: {
    backgroundColor: '#4CAF50',
    color: '#fff',
    padding: '20px',
    textAlign: 'center',
  },
  logo: {
    width: "200px",
  },
  nav: {
    flex: 1,
    display: "flex",
    justifyContent: "center",
  },
  navList: {
    listStyle: "none",
    display: "flex",
    gap: "20px",
  },
  main: {
    padding: "50px",
    textAlign: "center",
  },
  container: {
    backgroundColor: "#fff",
    padding: "50px",
    borderRadius: "10px",
    maxWidth: "1000px",
    margin: "0 auto",
    boxShadow: "0px 0px 10px rgba(0,0,0,0.1)",
  },
  title: {
    color: "#0ac2d2",
  },
  steps: {
    display: "flex",
    justifyContent: "space-between",
    gap: "20px",
    marginTop: "20px",
  },
  step: {
    backgroundColor: "#e8f4f8",
    border: "1px solid #0ac2d2",
    borderRadius: "5px",
    padding: "20px",
    flex: 1,
    boxShadow: "0px 0px 5px rgba(0,0,0,0.1)",
  },
  images: {
    display: "flex",
    justifyContent: "space-between",
    marginTop: "30px",
    gap: "20px",
  },
  image: {
    width: "45%",
    borderRadius: "5px",
    boxShadow: "0px 0px 5px rgba(0,0,0,0.1)",
  },
  closeBtn: {
    display: "inline-block",
    marginTop: "20px",
    padding: "10px 20px",
    backgroundColor: "#0ac2d2",
    color: "#fff",
    textDecoration: "none",
    borderRadius: "5px",
  },
  footer: {
    backgroundColor: "white",
    textAlign: "center",
    padding: "10px",
    borderTop: "1px solid #ccc",
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

export default HowItWorks;
