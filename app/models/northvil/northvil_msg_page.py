from app import *

class Northvil_msg_page(db.Model):
    __tablename__ = 'northvil_msg_page'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_wall = db.Column(db.Integer)
    message = db.Column(db.Text)
    post = db.Column(db.Boolean)
    group_id = db.Column(db.Integer, db.ForeignKey('northvil_groups_vk.id'))
    group = db.relationship('Northvil_groups_vk', backref='northvil_msg_page')

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Northvil_msg_page({0})>".format(self.id_wall)