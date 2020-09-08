import datetime
from reader import db
from flask_login import UserMixin

from sqlalchemy import event

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    website = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, nullable=False, default=0)
    membership_id = db.Column(db.Integer, nullable=False, default=0)
    active = db.Column(db.Boolean, nullable=True, default=True)
    created_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def save(self, commit=True):
        if commit:
            instance = self
            if not instance.id:
                db.session.add(instance)
            try:
                db.session.commit()
            except expression as e:
                print("Exception occured\n", e, '\n')
                db.session.rollback()
                return False
            return True
        return False