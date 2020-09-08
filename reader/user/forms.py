from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError, HiddenField
from sqlalchemy import not_

from .models import Role

class UserForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Name', 
        render_kw={"class": "form-control", 
            "placeholder": "Name"},
        validators=[
            validators.DataRequired(
                    message='Name is required'
            )
        ])

    user_name = StringField('User name', 
        render_kw={"class": "form-control", 
            "placeholder": "User Name"},
        validators=[
            validators.DataRequired(
                    message='User name is required'
            )
        ])

    email = StringField('Email',
        render_kw={"class": "form-control",
        "placeholder": "Email address"},
        validators=[
            validators.DataRequired(
                message="Email address is required"
            )
        ])

    password = StringField('Password',
        render_kw={"class": "form-control",
        "placeholder": "Password"},
        validators=[
            validators.DataRequired(
                message="Password is required"
            )
        ])
    
    first_name = StringField('First Name',
        render_kw={"class": "form-control",
        "placeholder": "First Name"},
        validators=[
            validators.DataRequired(
                message="First name is required"
            )
        ])

    last_name = StringField('Last Name',
        render_kw={"class": "form-control",
        "placeholder": "Last Name"})

    website = StringField('Website',
        render_kw={"class": "form-control",
        "placeholder": "Website"})

    website = StringField('Website',
        render_kw={"class": "form-control",
        "placeholder": "Website"})

    membership_id = StringField('Membership',
        render_kw={"class": "form-control",
        "placeholder": "Select membership"},
        validators=[
            validators.DataRequired(
                message="Membership is required"
            )
        ])

