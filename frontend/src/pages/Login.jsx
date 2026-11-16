// Login page

import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import { apiRequest } from "../services/api.js";
import Header from "../components/Header";

export default function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {

    // Authenticate user

    event.preventDefault();
    setError("");
    setLoading(true);

    try {
      await apiRequest("/auth/login", { email, password }, "POST");
      navigate("/");
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <Header />

      <div className="main-content">
        <div className="signin">
          <h3>Sign in or Register</h3>

          <form onSubmit={handleSubmit}>
            <input
              type="email"
              placeholder="Enter email address"
              autoComplete="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              required
            />

            <input
              type="password"
              placeholder="Enter password"
              autoComplete="current-password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              required
            />

            {error && <p role="alert">{error}</p>}

            <button type="submit" disabled={loading}>
              {loading ? "Signing in..." : "Sign in"}
            </button>
          </form>

          <div>
            <h5>Don't have an account?</h5>
            <Link to="/register">Create an account</Link>
          </div>
        </div>
      </div>
    </div>
  );
}