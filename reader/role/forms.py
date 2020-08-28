from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError, HiddenField
from sqlalchemy import not_

from .models import Role

class RoleForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Name', 
        render_kw={"class": "form-control", 
            "placeholder": "Role Name"},
        validators=[
            validators.DataRequired(
                    message='Role name is required'
            )
        ])