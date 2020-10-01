from flask import Flask
from flask import render_template

from .database import articles

flask_app = Flask(__name__)

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