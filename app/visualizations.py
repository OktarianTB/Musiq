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