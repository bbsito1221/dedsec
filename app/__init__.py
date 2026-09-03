from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name="default"):
    app = Flask(__name__)

    from config import config
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from app.blueprints.main import main_bp
    from app.blueprints.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    with app.app_context():
        db.create_all()

    return app
