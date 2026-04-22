from flask_wtf import FlaskForm, Form
from wtforms import StringField, SelectField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, Length


class NewEntry(Form):
    entry = StringField("Candidate", validators=[DataRequired(), Length(max=50, message="Too long!")])
    real = SelectField("Real Or Fake?", choices=[("r", "Real"), ("f", "Fake")])


class NewRBFB(FlaskForm):
    topic = StringField("Topic: ", validators=[DataRequired()])
    questions = FieldList(FormField(NewEntry), min_entries=7)
    submit = SubmitField("Save")
