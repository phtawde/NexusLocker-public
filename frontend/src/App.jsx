// Main react app

import { Routes, Route } from 'react-router-dom';

import Footer from './components/Footer';
import Home from './pages/Home';
import Login from './pages/Login';
import Product from './pages/Product';
import Products from './pages/Products';
import Register from './pages/Register';
import Search from './pages/Search';
import Soon from './pages/Soon';

function NotFound() {
  return <h1>404 - Page Not Found</h1>;
}

export default function App() {

  // Connect pages to main App routes

  return (
    <div className="app-shell">
      <main className="app-main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/products/:id" element={<Product />} />
          <Route path="/products" element={<Products />} />
          <Route path="/register" element={<Register />} />
          <Route path="/search" element={<Search />} />
          <Route path="/coming-soon" element={<Soon />}/>

          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
      <Footer />
    </div>
  );
}