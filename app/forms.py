from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired


class NewEntry(FlaskForm):
    entry = StringField("Entry", validators=[DataRequired()])
    real = SelectField(
        "Real Or Fake?", choices=[("r", "Real"), ("f", "Fake")], validators=[DataRequired()]
    )


class NewRBFB(FlaskForm):
    topic = StringField("Topic")
    questions = FieldList(FormField(NewEntry), min_entries=7)
    submit = SubmitField("Save")
