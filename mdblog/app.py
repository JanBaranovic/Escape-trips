from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from .database import articles

flask_app = Flask(__name__)
flask_app.secret_key = b'\x00\x14\xd1\x87\x08f\r\x86T\xd9\xf5\x06}d\xefN\x8d%\xbc\xef\xe9\xb9H\xf5'

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.html")

@flask_app.route("/about/")
def view_about():
    return render_template("about.html")

@flask_app.route("/slovakia/")
def view_slovakia():
    return render_template("slovakia_articles.html", articles = articles.items())

@flask_app.route("/slovakia/<int:art_id>/")
def view_slovakia_article(art_id):
    article = articles.get(art_id)
    if article:
        return render_template("slovakia_article.html", article = article)
    return render_template("article_not_found.html", art_id = art_id)

@flask_app.route("/world/")
def view_world():
    return render_template("world_articles.html", articles = articles.items())

@flask_app.route("/world/<int:art_id>/")
def view_world_article(art_id):
    article = articles.get(art_id)
    if article:
        return render_template("world_article.html", article = article)
    return render_template("article_not_found.html", art_id = art_id)

@flask_app.route("/contact/")
def view_contact():
    return render_template("contact.html")

@flask_app.route("/login/", methods = ["GET"])
def view_login():
    return render_template("login.html")

@flask_app.route("/login/", methods = ["POST"])
def login_user():
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            session["logged"] = True
            return redirect(url_for("view_admin"))
        else:
            return redirect(url_for("view_login"))

@flask_app.route("/admin/")
def view_admin():
    if "logged" not in session:
        return redirect(url_for("view_login"))
    return render_template("admin.html")

@flask_app.route("/logout/", methods = ["POST"])
def logout_user():
    session.pop("logged")
    return redirect(url_for("view_welcome_page"))