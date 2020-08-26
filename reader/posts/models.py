import datetime
from reader import db

from sqlalchemy import event

class Posts(db.Model):
    id           = db.Column(db.Integer, primary_key=True) # primary_key
    name         = db.Column(db.String(120), nullable=True)
    content      = db.Column(db.String(5000), nullable=False)
    category_id  = db.Column(db.String(120), nullable=False)
    author_id    = db.Column(db.String(120), nullable=False)
    publish_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    timestamp    = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    updated      = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

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

        def delete(self, commit=True):
            if self.id:
                db.session.delete(self)
                try:
                    db.session.commit()
                except expression as e:
                    print("Exception occured\n", e, '\n')
                    db.session.rollback()
                    return False
                return True
            return False

class Categories(db.Model):
    id           = db.Column(db.Integer, primary_key=True) # primary_key
    name         = db.Column(db.String(500), nullable=True)
    timestamp    = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    updated      = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


    def save(self, commit=True):
        print('start save')
        # create and update
        if commit:
            instance = self
            if not instance.id:
                db.session.add(instance)
            try:
                db.session.commit()
            except Exception as e:
                print("Exception occured\n", e, '\n')
                db.session.rollback()
                return False
            return True
        return False

    def delete(self, commit=True):
        if self.id:
            db.session.delete(self)
            try:
                db.session.commit()
            except expression as e:
                print("Exception occured\n", e, '\n')
                db.session.rollback()
                return False
            return True
        return False