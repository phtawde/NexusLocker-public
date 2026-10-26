// Sign up page

import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { apiRequest } from "../services/api.js";
import Header from "../components/Header";

export default function Register() {
  const navigate = useNavigate();

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {

    // Attempt to register user

    event.preventDefault();
    setError("");

    if (!firstName.trim() || !lastName.trim()) {
      setError("First and last name are required.");
      return;
    }

    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    setLoading(true);

    try {
      await apiRequest(
        "/auth/register",
        {
          firstName: firstName.trim(),
          lastName: lastName.trim(),
          email: email.trim(),
          password,
        },
        "POST"
      );

      navigate("/login");
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
          <h3>Create your account</h3>

          <form onSubmit={handleSubmit}>
            <input
              type="text"
              placeholder="First Name"
              autoComplete="given-name"
              value={firstName}
              onChange={(event) => setFirstName(event.target.value)}
              required
            />

            <input
              type="text"
              placeholder="Last Name"
              autoComplete="family-name"
              value={lastName}
              onChange={(event) => setLastName(event.target.value)}
              required
            />

            <input
              type="email"
              placeholder="Email Address"
              autoComplete="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              required
            />

            <input
              type="password"
              placeholder="Password"
              autoComplete="new-password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              required
            />

            <input
              type="password"
              placeholder="Confirm Password"
              autoComplete="new-password"
              value={confirmPassword}
              onChange={(event) =>
                setConfirmPassword(event.target.value)
              }
              required
            />

            {error && <p role="alert">{error}</p>}

            <button type="submit" disabled={loading}>
              {loading ? "Creating account..." : "Create account"}
            </button>
          </form>

          <div>
            <h5>Already have an account?</h5>
            <Link to="/login">Sign in</Link>
          </div>
        </div>
      </div>
    </div>
  );
}