import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import ProductViewer from "../components/ProductViewer";
import Navbar from "../components/Navbar";
import { apiRequest } from "../services/api.js";

export default function Product() {
  
  // Get the productId from the url 

  const { id } = useParams();

  // Link UI variables to JSX variables with useState, so that the UI
  // will update when the JSX variable is updated.

  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Execute sequence of events when page is requested

  useEffect(() => {
    apiRequest(`/products/${id}`)
    .then(setProduct)
    .catch((err) => setError(err.message))
    .finally(() => setLoading(false));
  }, [id]);

  // UI code block

  return (
    <div>
      <Navbar />
      <h1>Product</h1>

      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>Error: {error}</p>
      ) : !product ? (
        <p>Product not found.</p>
      ) : (
        <ProductViewer product={product} />
      )}
    </div>
  );
}