from app import *

class Northvil_counters_vk(db.Model):
    __tablename__ = 'northvil_counters_vk'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    albums = db.Column(db.Integer)
    videos = db.Column(db.Integer)
    audios = db.Column(db.Integer)
    notes = db.Column(db.Integer)
    photos = db.Column(db.Integer)
    gifts = db.Column(db.Integer)
    followers = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Northvil_counters_vk({0})>".format(self.id)