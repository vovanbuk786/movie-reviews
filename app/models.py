from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    upload_time = db.Column(db.Date, default=datetime.now(timezone.utc))
    reviews = db.relationship('Review', back_populates='movie')
    image = db.Column(db.String(255))

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.Date, default=datetime.now(timezone.utc))
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id', ondelete="CASCADE"), nullable=False)
    movie = db.relationship('Movie', back_populates='reviews')