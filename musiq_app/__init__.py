from flask import Flask, redirect, url_for
from musiq_app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY

    from musiq_app.routes import musiq
    app.register_blueprint(musiq)
    app.register_error_handler(404, page_not_found)

    return app


def page_not_found(e):
    return redirect(url_for("musiq.home"))
