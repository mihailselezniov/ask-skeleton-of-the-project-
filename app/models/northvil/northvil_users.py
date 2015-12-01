from app import *

class Northvil_users(db.Model):
    __tablename__ = 'northvil_users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    
    group_id = db.Column(db.Integer, db.ForeignKey('northvil_groups_vk.id'))
    group = db.relationship('Northvil_groups_vk', backref='northvil_users')
    
    photo_id = db.Column(db.Integer, db.ForeignKey('northvil_photos_vk.id'))
    photo = db.relationship("Northvil_photos_vk", uselist=False, backref="northvil_users")

    counter_id = db.Column(db.Integer, db.ForeignKey('northvil_counters_vk.id'))
    counter = db.relationship("Northvil_counters_vk", uselist=False, backref="northvil_users")
    
    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Northvil_users({0})>".format(self.uid)