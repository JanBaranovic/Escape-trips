from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.html")

@flask_app.route("/about/")
def view_about():
    return render_template("about.html")

@flask_app.route("/slovakia/")
def view_slovakia():
    return render_template("slovakia-articles.html")

@flask_app.route("/world/")
def view_world():
    return render_template("world-articles.html")

@flask_app.route("/contact/")
def view_contact():
    return render_template("contact")