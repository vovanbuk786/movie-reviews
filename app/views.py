from flask import render_template, redirect, request, url_for
#from flask_login import login_user, logout_user, login_required, current_user
from . import app, db
#from .forms import AddNewsForm, RegistrationForm, LoginForm
from .models import Movie, Review
from .forms import ReviewForm, AddMovieForm

from pathlib import Path
from werkzeug.utils import secure_filename

BASEDIR = Path(__file__).parent
UPLOAD_FOLDER = BASEDIR / 'static' / 'images'

@app.route('/')
def index():
    return render_template(
        'index.html',
        movies=Movie.query.all()
    )

@app.route('/movie/<int:id>', methods=['GET', 'POST'])
def movie(id):
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review()
        review.movie_id = id
        review.name = form.name.data
        review.text = form.text.data
        review.score = form.score.data

        db.session.add(review)
        db.session.commit()

        return redirect(request.url)
    return render_template(
        'movie.html',
        movie=Movie.query.get(id),
        form=form
    )

@app.route('/reviews')
def reviews():
    return render_template(
        'reviews.html',
        reviews=Review.query.order_by(Review.created_date.desc()).all()
    )

@app.route('/delete_review/<int:id>')
def delete_review(id):
    Review.query.filter(Review.id == id).delete()
    db.session.commit()
    return redirect(url_for('reviews'))
    return 'Redirecting...'

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie = Movie()
        movie.title = form.title.data
        movie.description = form.description.data
        
        image = form.image.data
        image_name = secure_filename(image.filename)
        UPLOAD_FOLDER.mkdir(exist_ok=True)
        image.save(UPLOAD_FOLDER / image_name)
        movie.image = image_name

        db.session.add(movie)
        db.session.commit()

        return redirect('/')

    return render_template(
        'add_movie.html',
        form=form
    )

@app.errorhandler(404)
def error():
    return "404, my friend!", 404