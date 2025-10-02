import React from "react";
import { Link } from "react-router-dom";

const About = () => {
  return (
    <div style={styles.page}>
      {/* HEADER */}
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

      {/* ABOUT SECTION */}
      <section style={styles.aboutSection}>
        <div style={styles.container}>
          <div style={styles.aboutContent}>
            {/* IMAGE */}
            <div style={styles.aboutImage}>
              <img
                src="https://www.p2cinfo-tech.com/images/services/service-single/3.jpg"
                alt="About Us"
                style={styles.image}
              />
            </div>

            {/* TEXT */}
            <div style={styles.aboutText}>
              <div style={styles.mainContainer}>
                <h2 style={styles.heading}>About Us</h2>
                <p style={styles.paragraph}>
                  At Liquidación Segura, we offer a definitive liquidation calculator
                  that helps workers calculate their severance pay quickly and accurately.
                  Our goal is to provide useful tools that empower individuals to make
                  informed decisions about their labor rights.
                </p>
              </div>

              <div style={styles.smallContainer}>
                <h3 style={styles.subHeading}>Our Vision</h3>
                <p style={styles.paragraph}>
                  To be the reference resource for liquidation calculations,
                  promoting transparency and knowledge of labor rights.
                </p>
              </div>

              <div style={styles.smallContainer}>
                <h3 style={styles.subHeading}>Our Values</h3>
                <p style={styles.paragraph}>
                  Transparency, commitment to the user, and respect for the labor
                  rights of all workers.
                </p>
              </div>
            </div>
          </div>

          {/* BACK TO HOME BUTTON */}
          <button
            style={styles.backButton}
            onClick={() => window.location.href = '/'}
          >
            ↑ Back to Home
          </button>
        </div>
      </section>
    </div>
  );
};

export default About;

const styles = {
  page: {
    fontFamily: "'Poppins', sans-serif",
    backgroundColor: "#f9f9f9",
    color: "#333",
    minHeight: "100vh",
  },
  header: {
    display: "flex",
    alignItems: "center",
    padding: "10px 20px",
    backgroundColor: "#fff",
    boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
  },
  logo: {
    marginRight: "250px",
  },
  nav: {
    display: "flex",
    gap: "20px",
  },
  navLink: {
    textDecoration: "none",
    color: "#000",
    fontWeight: "500",
    position: "relative",
  },
  aboutSection: {
    padding: "50px 20px",
    backgroundColor: "#f9f9f9",
  },
  container: {
    maxWidth: "1200px",
    margin: "0 auto",
    backgroundColor: "rgba(255,255,255,0.9)",
    borderRadius: "8px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
    padding: "20px",
  },
  aboutContent: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    gap: "20px",
  },
  aboutImage: {
    display: "flex",
    justifyContent: "center",
  },
  image: {
    width: "250px",
    height: "250px",
    borderRadius: "50%",
    objectFit: "cover",
    border: "double 5px #0ac2d2",
    boxShadow: "0 4px 8px rgba(0,0,0,0.2)",
  },
  aboutText: {
    display: "flex",
    flexDirection: "column",
    gap: "20px",
    textAlign: "center",
  },
  mainContainer: {
    backgroundColor: "#fff",
    padding: "20px",
    borderRadius: "8px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
  },
  smallContainer: {
    backgroundColor: "#fff",
    padding: "20px",
    borderRadius: "8px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
  },
  heading: {
    fontSize: "2em",
    color: "#0ac2d2",
    marginBottom: "10px",
  },
  subHeading: {
    fontSize: "1.5em",
    color: "#0ac2d2",
    marginBottom: "10px",
  },
  paragraph: {
    fontSize: "1em",
    color: "#333",
  },
  backButton: {
    display: "block",
    margin: "20px auto 0",
    padding: "15px 30px",
    backgroundColor: "#0ac2d2",
    border: "none",
    borderRadius: "5px",
    color: "#fff",
    fontSize: "1em",
    cursor: "pointer",
    transition: "background-color 0.3s",
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
