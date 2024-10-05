# File: app/__init__.py
from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.supabase_config import initialize_supabase

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS for all routes
    CORS(app)
    # Initialize Supabase
    initialize_supabase(app)

    # Register blueprints
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app