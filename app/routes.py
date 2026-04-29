from flask import render_template, flash, redirect, url_for, request, send_file
import sqlalchemy as sa
from app import app, db
from app.models import RBFB, Candidate
from app.forms import NewRBFB
from app.imagegen import generate_scorecard
import colorsys, random
import io
import base64
from datetime import date


@app.route("/")
@app.route("/index")
def index():
    user_posts = db.session.scalars(sa.select(RBFB))
    return render_template("index.html", title="Home", posts=user_posts)


@app.route("/new", methods=["GET", "POST"])
def new():
    form = NewRBFB()
    if form.validate_on_submit():
        rbfb = RBFB(topic=form.topic.data)
        rbfb.author = form.author.data or "Anonymous"
        rbfb.date = date.today()
        db.session.add(rbfb)
        db.session.flush()
        rbfb.urlval = hex(hash(str(rbfb.id)))
        for question in form.questions:
            c = Candidate(
                value=question.entry.data, real=question.real.data, parent=rbfb
            )
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
    if rbfb.hue is None:
        rbfb.hue = random.randint(0, 255)
        db.session.commit()
    rgb = colorsys.hsv_to_rgb(rbfb.hue / 255, 0.4, 0.7)
    rgb_string = f"{rgb[0] * 255} {rgb[1] * 255} {rgb[2] * 255}"
    return render_template(
        "view.html", topic=rbfb.topic, candidates=candidates, rgb=rgb_string
    )


@app.route("/score")
def score():
    topic = request.args.get('topic')
    rgb = request.args.get('rgb')
    score = request.args.get('score')
    img = generate_scorecard(rgb, topic, score)
    im_file = io.BytesIO()
    img.save(im_file, format="JPEG")
    im_file.seek(0)
    return send_file(
        path_or_file=im_file, download_name="score.jpg", mimetype="image/jpg"
    )


@app.route("/credits")
def credits():
    return render_template("credits.html")

@app.route("/share/<urlval>")
def share(urlval):
    shareurl = f"http://griffinhcollins.xyz/view/{urlval}"
    return render_template("share.html", url=shareurl)
