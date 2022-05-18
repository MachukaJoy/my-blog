from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title_blog = StringField('Title')
    description = TextAreaField('Type here', validators=[InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment', validators=[InputRequired()])
    submit = SubmitField('Comment')