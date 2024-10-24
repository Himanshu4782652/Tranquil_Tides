from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from datetime import datetime

db = SQLAlchemy()
login = LoginManager()


class UserModel(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(250), nullable=False)
    profile_picture = db.Column(db.String(150), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Assessments(db.Model):
    __tablename__ = "assessments"

    id = db.Column(db.Integer, primary_key=True)
    anxiety = db.Column(db.Integer, nullable=False)
    depression = db.Column(db.Integer, nullable=False)
    schizophrenia = db.Column(db.Integer, nullable=False)
    bipolar = db.Column(db.Integer, nullable=False)
    mood_score = db.Column(db.Float, nullable=False)
    # result = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("UserModel", backref="assessments")


class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("UserModel", backref="feedback")


@login.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))
