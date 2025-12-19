from flask import render_template, flash, redirect, url_for, request
import sqlalchemy as sa
from app import app, db
from app.models import RBFB, Candidate
from app.forms import NewRBFB


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/new", methods=["GET", "POST"])
def new():
    form = NewRBFB()
    if form.validate_on_submit():
        rbfb = RBFB(topic=form.topic.data)
        rbfb.urlval = hex(hash(str(rbfb.id)))
        flash(
            f"Created RBFB with topic {form.topic.data}, share here: http://127.0.0.1:5000/view/{rbfb.urlval}"
        )
        db.session.add(rbfb)
        for question in form.questions:
            c = Candidate(value=question.entry.data, real=question.real.data == "r", parent=rbfb)
            db.session.add(c)
        db.session.commit()
        return redirect(url_for("share", urlval=rbfb.urlval))
    return render_template("new.html", title="New RBFB", form=form)


@app.route("/view/<urlval>")
def view(urlval):
    query = sa.select(RBFB).where(RBFB.urlval == urlval)
    rbfb = db.session.scalars(query).first()
    candidates = []
    for candidate in db.session.scalars(rbfb.candidates.select()).all():
        candidates.append((candidate.value, candidate.real))
    return render_template("view.html", topic=rbfb.topic, candidates=candidates)


@app.route("/share/<urlval>")
def share(urlval):
    shareurl = f"http://127.0.0.1:5000/view/{urlval}"
    return render_template("share.html", url=shareurl)