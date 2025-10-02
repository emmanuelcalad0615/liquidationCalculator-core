import React, { useState } from "react";
import { Link } from "react-router-dom";   


const Profile = () => {
  // Datos iniciales (pueden venir de una base de datos o del registro)
  const [profile, setProfile] = useState({
    nombre: "Juan",
    apellidos: "Pérez",
    tipoDocumento: "Cédula de ciudadanía",
    numeroDocumento: "123456789",
    fechaNacimiento: "1990-05-10",
    correo: "juan@example.com",
  });

  // Estados de edición
  const [editMode, setEditMode] = useState(false);

  // Manejo de cambios en los inputs
  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile({
      ...profile,
      [name]: value,
    });
  };

  // Guardar cambios
  const handleSave = () => {
    alert("Datos guardados con éxito ✅");
    setEditMode(false);
  };

  // Eliminar perfil
  const handleDelete = () => {
    if (window.confirm("¿Estás seguro de que deseas eliminar tu perfil?")) {
      setProfile(null);
      alert("Perfil eliminado ❌");
    }
  };

  // Si el perfil fue eliminado
  if (!profile) {
    return (
      <div style={styles.container}>
        <h2>Perfil eliminado</h2>
      </div>
    );
  }

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
        {!editMode ? (
          <div style={styles.profileView}>
            <p><strong>Nombre:</strong> {profile.nombre}</p>
            <p><strong>Apellidos:</strong> {profile.apellidos}</p>
            <p><strong>Tipo de Documento:</strong> {profile.tipoDocumento}</p>
            <p><strong>Número de Documento:</strong> {profile.numeroDocumento}</p>
            <p><strong>Fecha de Nacimiento:</strong> {profile.fechaNacimiento}</p>
            <p><strong>Correo:</strong> {profile.correo}</p>

            <div style={styles.buttons}>
              <button style={styles.editButton} onClick={() => setEditMode(true)}>
                Editar
              </button>
              <button style={styles.deleteButton} onClick={handleDelete}>
                Eliminar
              </button>
            </div>
          </div>
        ) : (
          <div style={styles.editForm}>
            <label>Nombre:</label>
            <input
              type="text"
              name="nombre"
              value={profile.nombre}
              onChange={handleChange}
            />

            <label>Apellidos:</label>
            <input
              type="text"
              name="apellidos"
              value={profile.apellidos}
              onChange={handleChange}
            />

            <label>Tipo de Documento:</label>
            <select
              name="tipoDocumento"
              value={profile.tipoDocumento}
              onChange={handleChange}
            >
              <option value="Cédula de ciudadanía">Cédula de ciudadanía</option>
              <option value="Cédula extranjera">Cédula extranjera</option>
              <option value="Pasaporte">Pasaporte</option>
            </select>

            <label>Número de Documento:</label>
            <input
              type="text"
              name="numeroDocumento"
              value={profile.numeroDocumento}
              onChange={handleChange}
            />

            <label>Fecha de Nacimiento:</label>
            <input
              type="date"
              name="fechaNacimiento"
              value={profile.fechaNacimiento}
              onChange={handleChange}
            />

            <label>Correo:</label>
            <input
              type="email"
              name="correo"
              value={profile.correo}
              onChange={handleChange}
            />

            <div style={styles.buttons}>
              <button style={styles.saveButton} onClick={handleSave}>
                Guardar
              </button>
              <button style={styles.cancelButton} onClick={() => setEditMode(false)}>
                Cancelar
              </button>
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

// 🎨 Estilos en JS
const styles = {
  container: {
    fontFamily: "Poppins, sans-serif",
    backgroundColor: "#f9f9f9",
    minHeight: "100vh",
    padding: "20px",
  },
  header: {
    backgroundColor: "#0ac2d2",
    color: "#fff",
    padding: "20px",
    textAlign: "center",
    borderRadius: "8px",
  },
  main: {
    maxWidth: "600px",
    margin: "30px auto",
    backgroundColor: "#fff",
    padding: "20px",
    borderRadius: "10px",
    boxShadow: "0 4px 8px rgba(0,0,0,0.1)",
  },
  profileView: {
    textAlign: "left",
  },
  editForm: {
    display: "flex",
    flexDirection: "column",
    gap: "15px",
  },
  buttons: {
    marginTop: "20px",
    display: "flex",
    justifyContent: "space-between",
  },
  editButton: {
    backgroundColor: "#0ac2d2",
    color: "#fff",
    border: "none",
    padding: "10px 20px",
    borderRadius: "5px",
    cursor: "pointer",
  },
  deleteButton: {
    backgroundColor: "red",
    color: "#fff",
    border: "none",
    padding: "10px 20px",
    borderRadius: "5px",
    cursor: "pointer",
  },
  saveButton: {
    backgroundColor: "green",
    color: "#fff",
    border: "none",
    padding: "10px 20px",
    borderRadius: "5px",
    cursor: "pointer",
  },
  cancelButton: {
    backgroundColor: "#777",
    color: "#fff",
    border: "none",
    padding: "10px 20px",
    borderRadius: "5px",
    cursor: "pointer",
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

export default Profile;
