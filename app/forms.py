from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class Search(FlaskForm):
    title = StringField("Title")
    artist = StringField("Artist")
    submit = SubmitField("Search")
