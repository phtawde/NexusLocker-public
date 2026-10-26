// Products page that displays all products

import { useEffect, useState } from "react";
import { apiRequest } from "../services/api.js";
import Navbar from "../components/Navbar";
import ProductCard from "../components/ProductCard";

// App.jsx routes "nexuslocker.com/products" to the Products function 

export default function Products() {

  // Link UI variables to JSX variables with useState, so that the UI
  // will update when the JSX variable is updated.

  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Execute sequence of events when page is requested

  useEffect(() => {
    apiRequest("/products")
    .then(setProducts)
    .catch((err) => setError(err.message))
    .finally(() => setLoading(false));
  }, []);


  // UI code block

  return (
    <section className="products-page">
      <Navbar/>
      {/*

        Switch Statement in JavaScript

        {Case 1 ? (
          do something
        ): Case 2 ? (
          do something
        ): Case 3 ? (
          do something
        ) : (
          else 
        )}
        
        Below we use a switch statement to write different things to the
        UI depending on the status of the request.

      */}

      {loading ?(
        <p></p>
      ): error ? (
        <p>Error: {error}</p>
      ): products.length === 0 ? (
        <p>No products available.</p>
      ) : (
        <div className="main-content">
        <div className="product-container">
          <h1>All Products</h1>
          <div className="product-grid">
            {products.map((product) => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        </div>
        </div>
      )}
    </section>
  );
}