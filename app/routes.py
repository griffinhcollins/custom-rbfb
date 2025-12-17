from flask import render_template
from app import app
from app.forms import NewRBFB


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/new')
def new():
    form = NewRBFB()
    return render_template('new.html', title='New RBFB', form=form)