from app import *

class Northvil_sites(db.Model):
    __tablename__ = 'northvil_sites'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Northvil_sites({0})>".format(self.name)