import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home.js';
import Register from './pages/register.js';
import Major from './pages/major.js';
import About from './pages/about.js';
import How_it_works from './pages/how_it_works.js';
import Calculate_settlement from './pages/calculate_settlement.js';
import Profile from './pages/profile.js';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/major" element={<Major />} />
        <Route path="/about" element={<About />} />        
        <Route path="/how_it_works" element={<How_it_works />} />
        <Route path="/calculate" element={<Calculate_settlement />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </Router>
  );
};

export default App;
