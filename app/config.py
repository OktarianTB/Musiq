import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SPOTIFY_ID = os.environ.get("SPOTIFY_ID")
    SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")

