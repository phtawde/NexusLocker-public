import os
from flask import Flask
from dotenv import load_dotenv

from backend.routes.products_route import products_bp
from backend.routes.auth_route import auth_bp

# Load secret key from .env secrets file

load_dotenv()

app = Flask(__name__)

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