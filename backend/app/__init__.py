from flask import Flask
from flask_cors import CORS

from app.config.settings import Config

from app.extensions import (
    db,
    jwt,
    socketio,
    mail,
)

from app.routes import register_routes
from app.scheduler import start_scheduler
from app.security.rate_limiter import (
    limiter,
    register_rate_limit_handler
)
from app.core.production import register_error_handler

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    jwt.init_app(app)

    socketio.init_app(
        app,
        cors_allowed_origins="*"
    )

    mail.init_app(app)
    limiter.init_app(app)

    register_rate_limit_handler(app)
    register_error_handler(app)

    with app.app_context():

        db.create_all()

        register_routes(app)

        start_scheduler(app)

    return app