from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Post, User
from app.blueprints.main import main_bp


@main_bp.route("/")
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("main/index.html", posts=posts)


@main_bp.route("/u/<string:username>")
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).all()
    return render_template("main/profile.html", user=user, posts=posts)


@main_bp.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("main/post_detail.html", post=post)


@main_bp.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    if request.method == "POST":
        title = request.form.get("title")
        category = request.form.get("category")
        summary = request.form.get("summary")
        content = request.form.get("content")
        source_url = request.form.get("source_url")
        image_url = request.form.get("image_url")
        accent_color = request.form.get("accent_color")

        if not title or not category or not content:
            flash("ACCESS_DENIED: Title, category and main content are required.", "error")
            return redirect(url_for("main.new_post"))

        post = Post(
            title=title,
            category=category,
            summary=summary,
            content=content,
            source_url=source_url,
            image_url=image_url,
            accent_color=accent_color if accent_color else "#00f0ff",
            author=current_user
        )
        db.session.add(post)
        db.session.commit()

        flash("ACCESS_GRANTED: Research log successfully saved.", "success")
        return redirect(url_for("main.index"))

    return render_template("main/new_post.html")
