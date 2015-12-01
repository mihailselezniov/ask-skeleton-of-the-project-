from app import *

class Lumiera_variables(db.Model):
    __tablename__ = 'lumiera_variables'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    title = db.Column(db.String(200))
    boolean = db.Column(db.Boolean)
    number = db.Column(db.Integer)
    text = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)

    def __repr__(self):
        return "<Lumiera_variables({})>".format(self.name)