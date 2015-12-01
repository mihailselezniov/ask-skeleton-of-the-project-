from app import *

class Northvil_logs(db.Model):
    __tablename__ = 'northvil_logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Northvil_logs({0})>".format(self.text)