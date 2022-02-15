from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    jsonify,
    make_response,
)
import sqlite3
import logging
from datetime import datetime

db_connection_count = 0


# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection(metrics_only=False):
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    global db_connection_count

    if metrics_only:
        posts_count = len(
            connection.execute("SELECT * FROM posts").fetchall(),
        )
        return db_connection_count, posts_count
    else:
        db_connection_count += 1
        return connection


# Function to get a post using its ID, or all posts if no ID is passed
def get_posts(post_id=None):
    connection = get_db_connection()
    if post_id:
        posts = connection.execute(
            "SELECT * FROM posts WHERE id = ?",
            (post_id,),
        ).fetchone()
    else:
        posts = connection.execute("SELECT * FROM posts").fetchall()
    connection.close()
    return posts


def insert_post(title, content):
    connection = get_db_connection()
    connection.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        (
            title,
            content,
        ),
    )
    connection.commit()
    log_msg(msg="New Article Added.")
    connection.close()


# Define the Flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"


# Define the main route of the web application
@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)


# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route("/<int:post_id>")
def post(post_id):
    post = get_posts(post_id)
    if post is None:
        log_msg("Article Not Found.")
        return render_template("404.html"), 404
    else:
        log_msg(msg=f"Article \"{post['title']}\" retrieved!")
        return render_template("post.html", post=post)


# Define the About Us page
@app.route("/about")
def about():
    log_msg(msg="Retrieving `About` Page.")
    return render_template("about.html")


# Define the post creation functionality
@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Title is required!")
        else:
            insert_post(title, content)
            return redirect(url_for("index"))

    return render_template("create.html")


@app.route("/healthz")
def health():
    response = make_response(
        jsonify({"message": str("OK - healthy")}),
        200,
    )
    return response


@app.route("/metrics")
def metrics():
    db_connection_count, posts_count = get_db_connection(metrics_only=True)
    response = make_response(
        jsonify(
            {
                "db_connection_count": db_connection_count,
                "post_count": posts_count,
            }
        ),
        200,
    )
    return response


def log_msg(msg):
    time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    app.logger.info(f"[{time}] {msg}")


# start the application on port 3111
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        datefmt="%d/%m/%Y %I:%M:%S",
    )
    app.run(
        host="0.0.0.0",
        port="3111",
    )
