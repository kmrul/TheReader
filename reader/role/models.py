import datetime
from reader import db

from sqlalchemy import event

class Role(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(255), nullable=False)
    active     = db.Column(db.Boolean, nullable=False, default=True)
    created_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())
    updated_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow)


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