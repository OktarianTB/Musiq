from easy_spotify import Spotify
from rhythm_app.config import Config

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

