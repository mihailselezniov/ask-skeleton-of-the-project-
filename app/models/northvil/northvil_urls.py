from app import *

class Northvil_urls(db.Model):
    __tablename__ = 'northvil_urls'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sites_id = db.Column(db.Integer, db.ForeignKey('northvil_sites.id'))
    sites = db.relationship('Northvil_sites', backref='northvil_urls')
    name = db.Column(db.String(200))
    users_id = db.Column(db.Integer, db.ForeignKey('northvil_users.id'))
    users = db.relationship('Northvil_users', backref='northvil_urls')

    created_at = db.Column(db.DateTime, default=get_date)
    updated_at = db.Column(db.DateTime, default=get_date, onupdate=get_date)
    
    def __repr__(self):
        return "<Northvil_urls({0})>".format(self.name)