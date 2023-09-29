from flask import Flask
from config import Config
from flask_cors import CORS
from.routes.user_bp import user_bp
from.routes.server_bp import server_bp
from.routes.channel_bp import channel_bp
from.routes.message_bp import message_bp
from.routes.auth_bp import auth_bp


def init_app():
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    app.register_blueprint(user_bp)
    app.register_blueprint(server_bp)
    app.register_blueprint(channel_bp)
    app.register_blueprint(message_bp)
    app.register_blueprint(auth_bp)

    return app