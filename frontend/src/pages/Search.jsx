import Navbar from "../components/Navbar";
import ProductCard from "../components/ProductCard";
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { apiRequest } from "../services/api.js";

export default function Search() {
  const [searchParams] = useSearchParams();
  const query = searchParams.get("q") || "";

  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    let cancelled = false;

    async function fetchProducts() {

      // Get products matching the query

      if (!query.trim()) {
        setProducts([]);
        setError("");
        return;
      }

      setLoading(true);
      setError("");

      try {
        const data = await apiRequest(
          `/products/search?q=${encodeURIComponent(query)}`
        );

        if (!cancelled) {
          setProducts(data);
        }
      } catch (err) {
        if (!cancelled) {
          setError("Unable to load search results.");
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    fetchProducts();

    return () => {
      cancelled = true;
    };
  }, [query]);

  if (loading) return <Navbar/>

  if (error) return <p>{error}</p>;

  return (
    <section>
    <Navbar/>
    <div className="main-content">
        <div className="product-container">
          <h1>Search results for "{query}"</h1>

          {!products.length ? (
            <p>No products found.</p>
          ) : (
            <div className="product-grid">
                {products.map((product) => (
                  <ProductCard key={product.id} product={product} />
                ))}
            </div>
          )}
      </div>
    </div>
    </section>
  );
}
