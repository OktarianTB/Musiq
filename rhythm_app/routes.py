from flask import Blueprint, render_template, redirect, url_for, flash
from rhythm_app import ranking, tracks_info

rhythm = Blueprint("rhythm", __name__)


@rhythm.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", title="Home - Rhythm", date=ranking[0],
                           ranking=ranking[1:], track_info=tracks_info)


@rhythm.route("/song/<artist>/<title>", methods=["GET", "POST"])
def song(artist, title):
    return render_template("song.html", title=f"{title} - Rhythm", song=title, artist=artist)