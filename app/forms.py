# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField("Poster", validators=[InputRequired(), FileRequired(), FileAllowed(['jpg','jpeg', 'png', 'gif', 'tiff', 'ai', 'raw', 'eps', 'webp', 'avif', 'svg'], 'Images only')])
