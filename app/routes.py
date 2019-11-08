from flask import Blueprint, render_template, redirect, url_for
from app import ranking, tracks_info
from .utils import get_track_id, get_track_info, get_date_week_later, get_artist_id, \
    get_artist_info, get_main_artist, search_track, get_related_artists, get_top_tracks
from .forms import Search
from .visualizations import get_song_vis
from bokeh.embed import components

rhythm = Blueprint("rhythm", __name__)


@rhythm.route("/", methods=["GET", "POST"])
def home():
    start_date = ranking[0]
    end_date = get_date_week_later(start_date)
    return render_template("home.html", title="Home", start_date=start_date, end_date=end_date,
                           ranking=ranking[1:], track_info=tracks_info)


@rhythm.route("/song/<artist_name>/<title>", methods=["GET", "POST"])
def song(artist_name, title):
    track_id = get_track_id(title)
    artists = get_main_artist(artist_name)

    if not track_id:
        return render_template("error.html", title=title)

    track_info, track_features = get_track_info(track_id)
    if track_info["name"][:5].lower() not in artist_name.lower():
        return render_template("error.html", title=title)

    plot = get_song_vis(track_features)
    script, div = components(plot)

    return render_template("song.html", title=title, song=title, artists=artists, track_info=track_info,
                           audio_features=track_features, script=script, div=div)


@rhythm.route("/artist/<name>", methods=["GET", "POST"])
def artist(name):
    main_artist = get_main_artist(name)[0]
    if main_artist != name:
        return redirect(url_for("rhythm.artist", name=main_artist))

    artist_id = get_artist_id(main_artist)
    if artist_id:
        artist_info = get_artist_info(artist_id)
        main_artist_name = artist_info["name"]
        image_link = artist_info["image_link"]
        genres = artist_info["genres"]
        related_artists = get_related_artists(artist_id)
        top_tracks = get_top_tracks(artist_id)
        return render_template("artist.html", title=main_artist_name, artist=main_artist_name,
                               image_link=image_link, genres=genres, related_artists=related_artists,
                               top_tracks=top_tracks)

    return render_template("error.html", title=main_artist)


@rhythm.route("/search", methods=["GET", "POST"])
def search():
    form = Search()
    if form.validate_on_submit():
        if form.title.data:
            return redirect(url_for("rhythm.results", query=form.title.data))

        elif form.artist.data:
            data = get_artist_id(form.artist.data, only_id=False)
            if data:
                artist_name = data[1]
                return redirect(url_for("rhythm.artist", name=artist_name))
            else:
                form.artist.data = ""

    return render_template("search.html", title="Search", form=form)


@rhythm.route("/results/<query>")
def results(query):
    data = search_track(query)
    if data:
        tracks_info_data = data[0]
        return render_template("results.html", title=query.capitalize(), query=query, track_info=tracks_info_data)
    else:
        return render_template("error.html", title=query)


@rhythm.route("/game")
def game():
    return render_template("game.html", title="Statistics")
