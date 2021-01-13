from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Regexp, NumberRange


class AdditionForm(FlaskForm):
    """
    This form just queues an addition
    """
    x = StringField(u'X value', default="0", validators=[
        DataRequired(message="enter X"),
        #        NumberRange(min=0, max=1000, message="'cases' is out of range")
    ])

    y = StringField(u'Y value', default="0", validators=[
        DataRequired(message="enter Y"),
        #        NumberRange(min=0, max=10000, message="'cases' is out of range")
    ])

    submit = SubmitField(u"Submit")


# That's all!
