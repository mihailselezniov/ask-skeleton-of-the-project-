from app import *

class Northvil_photos_vk(db.Model):
    __tablename__ = 'northvil_photos_vk'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo_50 = db.Column(db.String(200))
    photo_100 = db.Column(db.String(200))
    photo_200_orig = db.Column(db.String(200))
    photo_200 = db.Column(db.String(200))
    photo_400_orig = db.Column(db.String(200))
    photo_max = db.Column(db.String(200))
    photo_max_orig = db.Column(db.String(200))

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Northvil_photos_vk({0})>".format(self.id)