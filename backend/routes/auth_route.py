# API routes for user authentication related routes

from flask import Blueprint, jsonify, request, session
from backend.services import auth_service as auth

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.post("/login")
def login():

    # Check credentials and log user in
    # Route: POST /api/auth/login
    # Response: 200: JSON success object
    #           400: Malformed/Invalid JSON
    #           401: Invalid credentials

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Expected a JSON object."}), 400

    email = auth.login(
        data.get("email"),
        data.get("password"),
    )

    if email is None:
        return jsonify({
            "error": "Invalid email or password."
        }), 401

    session.clear()
    session["email"] = email

    return jsonify({
        "message": "Login successful",
        "user": {
            "email": email
        }
    }), 200


@auth_bp.post("/register")
def register():

    # Register new user
    # Route: POST /api/auth/register
    # Response: 201: JSON success object
    #           400: Malformed/Invalid JSON; Failed registration

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Expected a JSON object."}), 400

    try:
        registered = auth.register(
            data.get("email"),
            data.get("firstName"),
            data.get("lastName"),
            data.get("password"),
        )
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    if not registered:
        return jsonify({
            "error": "There was an error while creating your account."
        }), 400

    return jsonify({
        "message": "Account created successfully."
    }), 201


@auth_bp.post("/logout")
def logout():

    # Log out of user session
    # Route: POST /api/auth/logout
    # Response: 200: JSON success object

    session.clear()

    return jsonify({
        "message": "Logout successful."
    }), 200


@auth_bp.get("/me")
def current_user():

    # Get current logged in user
    # Route: POST /api/auth/me
    # Response: 200: JSON user object

    email = session.get("email")

    return jsonify({
        "user": {"email": email} if email else None
    }), 200