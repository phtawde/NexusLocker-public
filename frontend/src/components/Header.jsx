// Header to be displayed on Login and Register pages instead of navbar

import { Link } from "react-router-dom";
import "../App.css";
import logo from "../assets/logo.png";

export default function Header() {
  return (
    <div className="header">
        <Link to="/" className="logo-container">
          <img className="logo" src={logo} alt="Logo" />
        </Link>
    </div>
  );
}