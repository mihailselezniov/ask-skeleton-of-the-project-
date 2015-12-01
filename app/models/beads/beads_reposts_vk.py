from app import *

class Beads_reposts_vk(db.Model):
    __tablename__ = 'beads_reposts_vk'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_id = db.Column(db.Integer, db.ForeignKey('beads_groups_vk.id'))
    group = db.relationship('Beads_groups_vk', backref='beads_reposts_vk')
    id_vk_repost = db.Column(db.String(200))
    int_vk_repost = db.Column(db.Integer)
    post = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)

    def __repr__(self):
        return "<Beads_reposts_vk({0})>".format(self.id_vk_repost)