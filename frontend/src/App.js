import logo from './assets/logo.svg';
import Home from "./pages/Home/Home";
import Login from './pages/Auth/login';
import Register from './pages/Auth/Register';
import './styles/App.css';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;
