from app import *

class Beads_logs_vk(db.Model):
    __tablename__ = 'beads_logs_vk'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    repost_id = db.Column(db.Integer, db.ForeignKey('beads_reposts_vk.id'))
    repost = db.relationship('Beads_reposts_vk', backref='beads_logs_vk')
    text = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Beads_logs_vk({0})>".format(self.text)