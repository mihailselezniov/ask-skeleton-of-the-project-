from app import *

class Lumiera_sprashivai_qa(db.Model):
    __tablename__ = 'lumiera_sprashivai_qa'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_unique = db.Column(db.String(200))
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    timestamp = db.Column(db.Integer)
    post = db.Column(db.Boolean)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)

    def __repr__(self):
        return "<Lumiera_ask_qa({})>".format(self.id_unique)