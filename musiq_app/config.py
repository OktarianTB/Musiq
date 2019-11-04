import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CLIENT_ID = os.environ.get("MUSIQ_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("MUSIQ_CLIENT_SECRET")

