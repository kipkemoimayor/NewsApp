from flask import render_template
from . import main
from ..request import news,sources
@main.route("/")
def index():
    top_news=news("top-headlines")
    print(top_news)
    source=sources("sources")
    return render_template("index.html",top_headline=top_news,sources=source)

@main.route("/body/<id>")
def body(id):
    return render_template("body.html")
