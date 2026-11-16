// Navbar containing logo, searchbar, and nav links

import { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { apiRequest } from "../services/api.js";
import "../App.css";
import logo from "../assets/logo.png";
import UserCircle from "../assets/user-circle.svg";
import cart from "../assets/cart.svg";
import box from "../assets/box-iso.svg";

export default function Navbar() {
  const [searchQuery, setSearchQuery] = useState("");
  const [user, setUser] = useState(null);
  const [authError, setAuthError] = useState("");
  const [loggingOut, setLoggingOut] = useState(false);

  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    let active = true;

    async function checkSession() {

      // Check which user is signed in

      try {
        const data = await apiRequest("/auth/me");

        if (active) {
          setUser(data.user);
          setAuthError("");
        }
      } catch (error) {
        if (active) {
          setAuthError(error.message);
        }
      }
    }

    checkSession();

    return () => {
      active = false;
    };
  }, [location.pathname]);

  const handleSearchSubmit = (event) => {

    // Call backend search function when search is submitted

    event.preventDefault();

    const query = searchQuery.trim();

    if (!query) return;

    navigate(`/search?q=${encodeURIComponent(query)}`);
  };

  async function handleLogout() {

    // Log user out

    setAuthError("");
    setLoggingOut(true);

    try {
      await apiRequest("/auth/logout", null, "POST");
      setUser(null);
      navigate("/");
    } catch (error) {
      setAuthError(error.message);
    } finally {
      setLoggingOut(false);
    }
  }

  return (
    <div className="navbar-container">
      <div className="navbar-content">
        <Link to="/" className="logo-container">
          <img className="logo" src={logo} alt="Logo" />
        </Link>

        <form
          onSubmit={handleSearchSubmit}
          className="search-container"
        >
          <input
            id="search"
            type="search"
            placeholder="Search..."
            className="search-bar"
            value={searchQuery}
            onChange={(event) => setSearchQuery(event.target.value)}
          />
        </form>

        <div className="nav-cluster">
          {user ? (
            <button
              type="button"
              className="nav-link"
              onClick={handleLogout}
              disabled={loggingOut}
            >
              <img src={UserCircle} alt="" />
              <div>
                <p>Account</p>
                <h3>{loggingOut ? "Signing Out..." : "Sign Out"}</h3>
              </div>
            </button>
          ) : (
            <Link to="/login" className="nav-link">
              <img src={UserCircle} alt="" />
              <div>
                <p>Account</p>
                <h3>Sign In</h3>
              </div>
            </Link>
          )}

          <Link to="/coming-soon" className="nav-link">
            <img src={box} alt="" />
            <div>
              <p>Returns &</p>
              <h3>Orders</h3>
            </div>
          </Link>

          <Link to="/coming-soon" className="nav-link">
            <img src={cart} alt="Shopping cart" />
          </Link>
        </div>
      </div>

      {authError && <p role="alert">{authError}</p>}
    </div>
  );
}