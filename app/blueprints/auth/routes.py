from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User
from app.blueprints.auth import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("ACCESS_DENIED: All fields required.", "error")
            return redirect(url_for("auth.login"))

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash("ACCESS_DENIED: Invalid credentials.", "error")
            return redirect(url_for("auth.login"))

        login_user(user)
        flash("ACCESS_GRANTED: Welcome back.", "success")
        return redirect(url_for("main.index"))

    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "operator").strip()
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("ACCESS_DENIED: Email and password required.", "error")
            return redirect(url_for("auth.register"))

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash("ACCESS_DENIED: Identity already registered.", "error")
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username if username else email.split('@')[0], email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("ACCESS_GRANTED: Identity stored in local DB.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        bio = request.form.get("bio", "").strip()
        interests = request.form.get("interests", "").strip()
        avatar_url = request.form.get("avatar_url", "").strip()

        if not username:
            flash("ACCESS_DENIED: Username cannot be empty.", "error")
            return redirect(url_for("auth.edit_profile"))

        # Check if username is taken by another user
        existing_user = User.query.filter_by(username=username).first()
        if existing_user and existing_user.id != current_user.id:
            flash("ACCESS_DENIED: Username already taken.", "error")
            return redirect(url_for("auth.edit_profile"))

        current_user.username = username
        current_user.bio = bio
        current_user.interests = interests
        if avatar_url:
            current_user.avatar_url = avatar_url

        db.session.commit()
        flash("ACCESS_GRANTED: Profile updated successfully.", "success")
        return redirect(url_for("main.profile", username=current_user.username))

    return render_template("auth/edit_profile.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("SESSION_TERMINATED: Logged out successfully.", "success")
    return redirect(url_for("main.index"))
