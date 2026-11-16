import os
from flask import Flask, jsonify
from dotenv import load_dotenv

from backend.routes.products_route import products_bp
from backend.routes.auth_route import auth_bp

from backend.errors import ProductNotFoundError

# Load secret key from .env secrets file

load_dotenv()

app = Flask(__name__)

@app.errorhandler(ProductNotFoundError)
def handle_product_not_found(error):
    return jsonify({"error": "Product not found."}), 404


@app.errorhandler(500)
def handle_internal_error(error):
    return jsonify({"error": "An internal server error occurred."}), 500

# Configure flask app settings

app.config.update(
    SECRET_KEY=os.environ["FLASK_SECRET_KEY"],
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_SAMESITE="Lax",
)

# Connect routes to main flask app

app.register_blueprint(products_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)