from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    """ Database operations """

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_all_paginate(cls, page, per_page, **kwargs):
        return cls.query.filter_by(**kwargs).paginate(page=page, per_page=per_page)

    @classmethod
    def count_all(cls):
        return cls.query.count()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)

    @classmethod
    def find_latest(cls):
        return cls.query.order_by(cls.id.desc()).first()

    @classmethod
    def find_enabled_item(cls, _id):
        return cls.query.filter_by(id=_id, status='enabled').first()

    @classmethod
    def find_by_first(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def find_and_order_by(cls, order_by='id', **kwargs):
        return cls.query.filter_by(**kwargs).order_by(order_by).all()

    @classmethod
    def find_by_slug(cls, slug):
        return cls.query.filter_by(slug=slug).first()

    @classmethod
    def find_all_omit_record_with_this_id(cls, _id):
        return cls.query.filter(cls.id != _id).all()

    @classmethod
    def find_all_omit_record_with_this_name(cls, name):
        return cls.query.filter(cls.name != name).all()

    @classmethod
    def find_all_omit_record_with_this_slug(cls, slug):
        return cls.query.filter(cls.slug != slug).all()

    @classmethod
    def find_first_omit_record_with_this_name(cls, _id, name):
        return cls.query.filter_by(name=name).filter(cls.id != _id).first()

    def save_to_db(self):
        if self.id is not None:
            self.updated_at = datetime.utcnow()

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()