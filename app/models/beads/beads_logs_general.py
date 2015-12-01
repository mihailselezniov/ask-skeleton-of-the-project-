from app import *

class Beads_logs_general(db.Model):
    __tablename__ = 'beads_logs_general'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Beads_logs_general({0})>".format(self.text)