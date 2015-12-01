from app import *

class Beads_variables(db.Model):
    __tablename__ = 'beads_variables'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    title = db.Column(db.String(200))
    boolean = db.Column(db.Boolean)
    number = db.Column(db.Integer)
    text = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)

    def __repr__(self):
        return "<Beads_variables({0})>".format(self.name)