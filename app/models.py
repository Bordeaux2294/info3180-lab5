# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime
import pytz

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    poster = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('US/Eastern')))

    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at