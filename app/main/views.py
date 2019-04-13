from flask import render_template
from . import main
from ..request import news
@main.route("/")
def index():
    top_news=news("top-headlines")
    print(top_news)
    return render_template("index.html",top_headline=top_news)
