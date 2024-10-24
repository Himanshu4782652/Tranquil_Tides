import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from models import db, UserModel, Assessments, Feedback, login
from forms import MentalHealthAssessmentForm, LoginForm, RegistrationForm, FeedbackForm
from predict import predict_mood
from utils import get_relaxation_techniques, get_eating_disorder_probability_and_techniques
from flask_migrate import Migrate
# import ipdb
from flask_wtf.csrf import CSRFProtect

# Application initialization
app = Flask(__name__)

# Secret key for session management
app.secret_key = os.environ.get("SECRET_KEY", "f9bf78b9a18ce6d46a0cd2b0b86dda")

# CSRF Protection
csrf = CSRFProtect(app)
app.config["WTF_CSRF_ENABLED"] = True

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:////home/aman/Desktop/Tranquil-Tides/instance/data.db"  # Ensure path is correct
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db.init_app(app)
login.init_app(app)
login.login_view = "login"
migrate = Migrate(app, db)

# Allowed file extensions for profile picture uploads
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Routes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        # Check if email or username is already registered
        if UserModel.query.filter_by(email=email).first():
            flash("Email already registered", "error")
            return redirect(url_for("register"))
        if UserModel.query.filter_by(username=username).first():
            flash("Username already taken", "error")
            return redirect(url_for("register"))

        # Create new user
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash("Registration successful!", "success")
        return redirect(url_for("dashboard"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    form = LoginForm()  # Instantiate the form

    if form.validate_on_submit():  # Validates CSRF token and form inputs
        email = form.email.data
        password = form.password.data
        user = UserModel.query.filter_by(email=email).first()

        if user is None:
            flash("No account found with that email", "error")
        elif not user.check_password(password):
            flash("Incorrect password", "error")
        else:
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "success")
    return redirect(url_for("login"))


@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    try:
        # Fetch assessments for the current user
        assessments = Assessments.query.filter_by(user_id=current_user.id).all()

        # Prepare data for charts
        mood_data = [assessment.mood_score for assessment in assessments]
        anxiety_data = [assessment.anxiety for assessment in assessments]
        depression_data = [assessment.depression for assessment in assessments]
        dates = [
            assessment.date_created.strftime("%Y-%m-%d") for assessment in assessments
        ]

        # Determine trend
        trend = "No Data Available"
        if len(mood_data) > 1:
            trend = "improving" if mood_data[-1] > mood_data[-2] else "declining"
        elif len(mood_data) == 1:
            trend = "stable"

        latest_mood = mood_data[-1] if mood_data else "No Data"

        return render_template(
            "dashboard.html",
            user=current_user.username,
            assessments=assessments,
            mood_data=mood_data,
            anxiety_data=anxiety_data,
            depression_data=depression_data,
            dates=dates,
            latest_mood=latest_mood,
            trend=trend,
        )
    except Exception as e:
        flash(f"Error loading dashboard: {str(e)}", "error")
        return redirect(url_for("index"))


@app.route("/assessment", methods=["GET", "POST"])
@login_required
def assessment():
    form = MentalHealthAssessmentForm()

    if form.validate_on_submit():
        try:
            # Extract form data
            anxiety = form.anxiety.data
            depression = form.depression.data
            schizophrenia = form.schizophrenia.data
            bipolar = form.bipolar.data

            # Predict mood score using the machine learning model
            mood_score = predict_mood([anxiety, depression, schizophrenia, bipolar])

            # Get eating disorder probability and relaxation techniques
            eating_disorder_probability, relaxation_techniques = (
                get_eating_disorder_probability_and_techniques(mood_score)
            )

            # Save the assessment in the database
            assessment = Assessments(
                anxiety=anxiety,
                depression=depression,
                schizophrenia=schizophrenia,
                bipolar=bipolar,
                mood_score=mood_score,
                user_id=current_user.id,
            )

            db.session.add(assessment)
            db.session.commit()
            flash("Assessment saved successfully.", "success")

            # Render results page with mood score, probability, and relaxation techniques
            return render_template(
                "results.html",
                mood_score=mood_score,
                eating_disorder_probability=eating_disorder_probability,
                relaxation_techniques=relaxation_techniques,
            )
        except Exception as e:
            db.session.rollback()
            flash(f"Error processing assessment: {str(e)}", "error")
            return redirect(url_for("assessment"))

    else:
        if request.method == "POST":
            flash("Please correct the errors in the form.", "error")

    return render_template("assessment.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        profile_picture = request.files.get("profile_picture")

        user = current_user
        user.username = username
        user.email = email

        # Handle password update
        if password:
            if password == confirm_password:
                user.set_password(password)
            else:
                flash("Passwords do not match", "error")
                return redirect(url_for("profile"))

        # Handle profile picture upload
        if profile_picture and allowed_file(profile_picture.filename):
            profile_picture_path = f"static/uploads/"

            if not os.path.exists(profile_picture_path):
                os.makedirs(profile_picture_path)

            # Save the uploaded picture
            picture_filename = profile_picture.filename
            profile_picture.save(os.path.join(profile_picture_path, picture_filename))

            # Update the user profile picture path
            user.profile_picture = f"{user.id}/{picture_filename}"

        # Save changes to the database
        try:
            db.session.commit()
            flash("Profile updated successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred: {e}", "error")

        return redirect(url_for("profile"))

    # Retrieve user assessments to show in profile page
    user_assessments = Assessments.query.filter_by(user_id=current_user.id).all()

    return render_template(
        "profile.html", user=current_user, user_assessments=user_assessments
    )


@app.route("/feedback", methods=["GET", "POST"])
@login_required
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        try:
            new_feedback = Feedback(
                feedback=form.feedback.data, user_id=current_user.id
            )
            db.session.add(new_feedback)
            db.session.commit()
            flash("Thank you for your feedback!", "success")
            return redirect(url_for("dashboard"))
        except Exception as e:
            db.session.rollback()
            flash(f"Error submitting feedback: {str(e)}", "error")
            return redirect(url_for("feedback"))

    return render_template("feedback.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
