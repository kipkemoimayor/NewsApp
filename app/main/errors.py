from flask import render_template
from . import main
@main.errorhandler(404)
def four_ow_four(error):
    return render_template("error.html"),404
