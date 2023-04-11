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
    created_at = db.Column(db.DateTime)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
        time = datetime.now(pytz.timezone('US/Eastern'))
        self.created_at = time