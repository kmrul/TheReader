import datetime
from reader import db

from sqlalchemy import event

class Posts(db.Model):
    id           = db.Column(db.Integer, primary_key=True) # primary_key
    title        = db.Column(db.String(120), nullable=True)
    content      = db.Column(db.String(5000), nullable=False)
    category_id  = db.Column(db.Integer, nullable=False)
    author_id    = db.Column(db.Integer, nullable=False)
    status       = db.Column(db.String(255), nullable=False)
    publish_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    tags         = db.Column(db.String(500), nullable=True)
    feature_image= db.Column(db.LargeBinary, nullable=True)
    is_premium   = db.Column(db.Boolean, nullable=True)
    active      = db.Column(db.Boolean, nullable=True, default=True)
    created_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

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
    slug         = db.Column(db.String(255), nullable=True)
    description  = db.Column(db.String(255), nullable=True)
    active      = db.Column(db.Boolean, nullable=True, default=True)
    created_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


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