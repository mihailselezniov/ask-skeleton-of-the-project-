from app import *

class Lumiera_wall(db.Model):
    __tablename__ = 'lumiera_wall'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wall_id = db.Column(db.String(200))
    post = db.Column(db.Boolean)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)

    def __repr__(self):
        return "<Lumiera_wall({})>".format(self.wall_id)