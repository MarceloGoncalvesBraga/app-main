from flask import render_template
from application import main

@main.route("/")
def home():
    return render_template("index.html")