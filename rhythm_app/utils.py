from easy_spotify import Spotify
from rhythm_app.config import Config
import datetime
import calendar
import re

spotify = Spotify(Config.SPOTIFY_ID, Config.SPOTIFY_SECRET)


def get_tracks_id(ranking):
    tracks = []
    for rank in ranking[1:]:
        track_id = spotify.get_track_id(rank[0])
        tracks.append(track_id)
    return tracks


def get_tracks_info(tracks):
    tracks_info = []
    for track in tracks:
        info = spotify.get_track_info(track)
        tracks_info.append(info)
    return tracks_info


def get_track_id(title):
    return spotify.get_track_id(title)


def get_track_info(track_id):
    track_info = spotify.get_track_info(track_id)
    track_features = spotify.get_track_audio_features(track_id)
    return track_info, track_features


def get_date_week_later(current_date):
    date = current_date.replace(",", "").split(" ")
    month, day, year = date[0], date[1], date[2]
    name_to_num = {name: num for num, name in enumerate(calendar.month_name) if num}

    start_date = datetime.datetime.strptime(f"{name_to_num[month]}/{day}/{year[-2:]}", "%m/%d/%y")
    end_date = start_date + datetime.timedelta(days=7)

    for k, v in name_to_num.items():
        if v == end_date.month:
            new_month = k
    new_day = end_date.day
    new_year = end_date.year
    final_date = f"{new_month} {new_day}, {new_year}"

    return final_date


def get_artist_id(name, limit=1, only_id=True):
    return spotify.get_artist_id(name, limit=limit, only_id=only_id)


def get_artist_info(artist_id):
    return spotify.get_artist_info_from_id(artist_id)


def get_main_artist(artists):
    if "&" in artists:
        return artists.split(" & ")
    if "Featuring" in artists:
        return artists.split(" Featuring ")
    return [artists]



