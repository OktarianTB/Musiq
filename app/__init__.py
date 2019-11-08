from flask import Flask, redirect, url_for
from .config import Config
from .chart_scraper import get_ranking
from .utils import get_tracks_id, get_tracks_info

ranking = get_ranking()
tracks_id = get_tracks_id(ranking)
tracks_info = []


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY
    global tracks_info
    tracks_info = get_tracks_info(tracks_id)

    from app.routes import rhythm
    app.register_blueprint(rhythm)
    app.register_error_handler(404, page_not_found)

    return app


def page_not_found(e):
    return redirect(url_for("rhythm.home"))
