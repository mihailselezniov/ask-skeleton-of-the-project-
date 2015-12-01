from app import *

class Beads_groups_vk(db.Model):
    __tablename__ = 'beads_groups_vk'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_vk_group = db.Column(db.String(200))
    name = db.Column(db.String(200))
    boolean = db.Column(db.Boolean)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Beads_groups_vk({0})>".format(self.id_vk_group)