from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import NewRBFB


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/new", methods=["GET", "POST"])
def new():
    form = NewRBFB()
    if form.validate_on_submit():
        flash(f"Created (not really) RBFB with topic {form.topic.data}")
        return redirect(url_for("index"))
    return render_template("new.html", title="New RBFB", form=form)
