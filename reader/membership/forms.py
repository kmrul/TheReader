from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError, HiddenField
from sqlalchemy import not_

from .models import Membership

class MembershipForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Name', 
        render_kw={"class": "form-control", 
            "placeholder": "Membership Name"},
        validators=[
            validators.DataRequired(
                    message='Membership name is required'
            )
        ])
    price = StringField('Price', 
        render_kw={"class": "form-control", 
            "placeholder": "Price"},
        validators=[
            validators.DataRequired(
                    message='Price name is required'
            )
        ])
    post_limit = StringField('Post Limit', 
        render_kw={"class": "form-control", 
            "placeholder": "Readable Post Limit"},
        )