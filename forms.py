from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class MentalHealthAssessmentForm(FlaskForm):
    anxiety = IntegerField(
        "Anxiety Level (0-10)", validators=[DataRequired(), NumberRange(min=0, max=10)]
    )
    depression = IntegerField(
        "Depression Level (0-10)",
        validators=[DataRequired(), NumberRange(min=0, max=10)],
    )
    schizophrenia = IntegerField(
        "Schizophrenia Disorders Level (0-10)",
        validators=[DataRequired(), NumberRange(min=0, max=10)],
    )
    bipolar = IntegerField(
        "Bipolar Disorder Level (0-10)",
        validators=[DataRequired(), NumberRange(min=0, max=10)],
    )
    submit = SubmitField("Submit Assessment")


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class FeedbackForm(FlaskForm):
    feedback = TextAreaField("Your Feedback", validators=[DataRequired()])
    rating = IntegerField(
        "Rate the Assessment (1-5)",
        validators=[
            DataRequired(),
            NumberRange(min=1, max=5, message="Please rate between 1 and 5"),
        ],
    )
    submit = SubmitField("Submit Feedback")
