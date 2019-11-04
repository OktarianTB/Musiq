from flask import Blueprint, render_template, redirect, url_for, flash

musiq = Blueprint("musiq", __name__)


@musiq.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", title="Home - Musiq")


@musiq.route("/play", methods=["GET", "POST"])
def play():
    return render_template("play.html", title="Play - Musiq")