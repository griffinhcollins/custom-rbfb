from flask_wtf import FlaskForm, Form
from wtforms import StringField, SelectField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired


class NewEntry(Form):
    entry = StringField("Entry", validators=[DataRequired()])
    real = SelectField("Real Or Fake?", choices=[("r", "Real"), ("f", "Fake")])


class NewRBFB(FlaskForm):
    topic = StringField("Topic: ", validators=[DataRequired()])
    questions = FieldList(FormField(NewEntry), min_entries=7)
    submit = SubmitField("Save")
