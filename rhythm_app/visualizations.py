from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import factor_cmap


def get_song_vis(audio_features):

    features = ['Danceability', 'Energy', 'Acousticness', 'Liveness', 'Valence']
    counts = [audio_features[key.lower()] for key in features]

    source = ColumnDataSource(data=dict(features=features, counts=counts))

    p = figure(x_range=features, plot_height=350, toolbar_location=None)
    p.vbar(x='features', top='counts', width=0.7, source=source,
           line_color='white',
           fill_color=factor_cmap('features', palette=['#3288bd', '#99d594', '#e6f598', '#fee08b', '#fc8d59', '#d53e4f'], factors=features))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 1
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    p.background_fill_alpha = 0
    p.border_fill_alpha = 0
    p.toolbar.logo = None

    return p


#data = {'danceability': 0.577, 'energy': 0.833, 'key': 5, 'loudness': -3.337, 'mode': 1, 'speechiness': 0.0695, 'acousticness': 0.0137, 'instrumentalness': 0, 'liveness': 0.121, 'valence': 0.58, 'tempo': 107.936, 'type': 'audio_features', 'id': '22oEJW6r2rMb9z4IntfyEa', 'uri': 'spotify:track:22oEJW6r2rMb9z4IntfyEa', 'track_href': 'https://api.spotify.com/v1/tracks/22oEJW6r2rMb9z4IntfyEa', 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/22oEJW6r2rMb9z4IntfyEa', 'duration_ms': 169667, 'time_signature': 4}
#get_song_vis(data)