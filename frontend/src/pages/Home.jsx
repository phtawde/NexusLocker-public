// Home page

import Navbar from "../components/Navbar";
import { Link } from "react-router-dom";
export default function Home() {
  return (
    
    <div>
      <Navbar/>
      <h1>Welcome Home.</h1>
      <Link to="/products">View All Products</Link>
    </div>
  );
}