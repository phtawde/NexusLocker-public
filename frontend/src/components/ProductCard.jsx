// Product card that displays products in a reusable detail "card"

import { Link } from "react-router-dom";

export default function ProductCard({ product }) {
  if (!product) return null;

  const imageLink = `/assets/product_photos/${product.id}/thumbnail.jpg`;

  return (
    <article className="product-card">
      <div className="card-content">
      <Link to={`/products/${product.id}`}>
        <div className="card-image">
          <img src={imageLink}></img>
        </div>
        <div className="card-details">
          <p>{product.name}</p>
          <h3>${Number(product.price).toFixed(2)}</h3>
        </div>
      </Link>
      </div>
    </article>
  );
}
