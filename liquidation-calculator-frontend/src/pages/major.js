import React from 'react';
import { Link } from 'react-router-dom';   // ✅ Importación necesaria

const Major = () => {
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
        <h3>Liquidacion segura</h3>
        <h2>Bienvenido a la aplicación</h2>
        <p>Tu registro fue exitoso, ahora puedes explorar la app.</p>
        
      </main>
    </div>
  );
};

const styles = {
  container: {
    fontFamily: 'Arial, sans-serif',
    backgroundColor: '#f4f4f4',
    minHeight: '100vh',
  },
  header: {
    backgroundColor: '#4CAF50',
    color: '#fff',
    padding: '20px',
    textAlign: 'center',
  },
  h3:{
    padding: '20px',
    textAlign: 'center',
  },
  main: {
    padding: '20px',
    textAlign: 'center',
  },
  cards: {
    display: 'flex',
    justifyContent: 'center',
    gap: '20px',
    flexWrap: 'wrap',
    marginTop: '30px',
  },
  card: {
    backgroundColor: '#fff',
    padding: '20px',
    width: '200px',
    borderRadius: '8px',
    boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
  },
  link: {
    textDecoration: 'none',
    color: '#4CAF50',
    fontWeight: 'bold',
  },
};

export default Major;


