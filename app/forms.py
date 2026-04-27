from flask_wtf import FlaskForm, Form
from wtforms import StringField, BooleanField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, Length


class NewEntry(Form):
    entry = StringField("Candidate", validators=[DataRequired(), Length(max=50, message="Too long!")])
    real = BooleanField("Real Or Fake?")


class NewRBFB(FlaskForm):
    topic = StringField("Topic: ", validators=[DataRequired(), Length(max=40, message="Too long!")])
    questions = FieldList(FormField(NewEntry), min_entries=7)
    submit = SubmitField("Save")
