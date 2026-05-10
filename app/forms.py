from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class ReviewForm(FlaskForm):
    name = StringField("Ваше имя", validators=[DataRequired()])
    text = TextAreaField("Текст отзыва", validators=[DataRequired()])
    score = SelectField("Ваша оценка", choices=range(1,11))
    submit = SubmitField("Отправить!")

class AddMovieForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    description = TextAreaField("Описание", validators=[DataRequired()])
    image = FileField("Ваша оценка", validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField("Отправить!")