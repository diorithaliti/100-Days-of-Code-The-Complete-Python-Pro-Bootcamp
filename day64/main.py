from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
db = SQLAlchemy(app)
api_key = "be8bf552000159fb743078aec27cb9d5"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"



class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# with app.app_context():
#     # db.create_all()
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()

class EditForm(FlaskForm):
    rating = StringField(label='Your Rating out of 10', validators=[DataRequired()])
    review = StringField(label='Your Review!', validators=[DataRequired()])
    submit = SubmitField(label="Submit")

class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()
    id = request.args.get('id')
    movie_id = Movie.query.filter_by(id=id).first()
    if request.method == 'POST':
        response = request.form
        with app.app_context():
            movie_to_update = Movie.query.get(id)
            movie_to_update.rating = response["rating"]
            movie_to_update.review = response["review"]
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    id = request.args.get('id')
    with app.app_context():
         movie_to_delete = Movie.query.get(id)
         db.session.delete(movie_to_delete)
         db.session.commit()
         return redirect(url_for('home'))
    return render_template("edit.html")

@app.route("/add", methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if request.method == 'POST':
        response = request.form["title"]
        params = {
            "api_key": api_key,
            "language": "en-US",
            "query": response
        }
        response_api = requests.get(url="https://api.themoviedb.org/3/search/movie?", params=params)
        response_api.raise_for_status()
        data = response_api.json()
        movies = data["results"]
        return render_template("select.html", movies=movies)

    return render_template("add.html", form=add_form)

@app.route("/selected", methods=['GET', 'POST'])
def selected():
    id = request.args.get('id')
    params = {
        "api_key": api_key,
        "language": "en-US",
    }
    response_api = requests.get(url=f"https://api.themoviedb.org/3/movie/{id}", params=params)
    response_api.raise_for_status()
    movie_data = response_api.json()
    print(movie_data)
    release_date = datetime.datetime.strptime(movie_data["release_date"], "%Y-%m-%d")
    with app.app_context():
        # db.create_all()
        new_movie = Movie(
            title=movie_data["original_title"],
            year=release_date.year,
            description=movie_data["overview"],
            rating=0.0,
            ranking="10",
            review="-",
            img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit',id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
