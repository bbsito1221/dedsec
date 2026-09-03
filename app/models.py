from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, default="operator")
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    bio = db.Column(db.String(250), nullable=True, default="Building my digital brain and research logs.")
    interests = db.Column(db.String(250), nullable=True, default="python, cybersecurity, linux")
    avatar_url = db.Column(db.String(300), nullable=True)
    posts = db.relationship("Post", backref="author", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    summary = db.Column(db.String(300), nullable=True)
    content = db.Column(db.Text, nullable=False)
    source_url = db.Column(db.String(300), nullable=True)
    image_url = db.Column(db.String(300), nullable=True)
    accent_color = db.Column(db.String(20), nullable=True, default="#00f0ff")
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Post {self.title}>"
