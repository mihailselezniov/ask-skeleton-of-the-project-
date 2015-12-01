from app import *

class Northvil_groups_vk(db.Model):
    __tablename__ = 'northvil_groups_vk'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ask_login = db.Column(db.String(200))
    ask_password = db.Column(db.String(200))
    tag = db.Column(db.String(200))
    id_vk = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Northvil_groups_vk({0})>".format(self.ask_login)