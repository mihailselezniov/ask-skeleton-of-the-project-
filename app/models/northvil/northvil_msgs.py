from app import *

class Northvil_msgs(db.Model):
    __tablename__ = 'northvil_msgs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_unique = db.Column(db.String(200))
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    urls_id = db.Column(db.Integer, db.ForeignKey('northvil_urls.id'))
    urls = db.relationship('Northvil_urls', backref='northvil_msgs')
    post = db.Column(db.Boolean)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)

    def __repr__(self):
        return "<Northvil_msgs({0})>".format(self.id_unique)