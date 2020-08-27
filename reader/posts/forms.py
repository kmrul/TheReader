from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError, HiddenField
from sqlalchemy import not_

from .models import Categories

class CategoryForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Name', 
        render_kw={"class": "form-control", 
            "placeholder": "Name"},
        validators=[
            validators.DataRequired(
                    message='Category name is required'
            )
        ])
    slug = StringField('Slug', 
        render_kw={"class": "form-control", 
            "placeholder": "Slug"},
        validators=[
            validators.DataRequired(
                    message='Slug name is required'
            )
        ])
    description = StringField('Description', 
        render_kw={"class": "form-control", 
            "placeholder": "Description"},
        )