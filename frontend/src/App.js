import logo from './assets/logo.svg';
import Home from "./pages/Home/Home";
import Login from './pages/Auth/login';
import Register from './pages/Auth/Register';
import ContratoForm from './pages/Contract/Contract';
import Liquidaciones from './pages/Liquidation/Liquidation';
import MisLiquidaciones from './pages/MyLiquidations/MyLiquidations';
import './styles/App.css';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/contract" element={<ContratoForm />} />
      <Route path="/liquidation" element={<Liquidaciones />} />
      <Route path="/myliquidations" element={<MisLiquidaciones />} />
    </Routes>
  );
}

export default App;
