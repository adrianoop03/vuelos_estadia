from models.db import db

class Stadium(db.Model):
    __tablename__ = 'stadiums'
    
    id_stadium = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    ubication  = db.Column(db.String(100), nullable=False)
    city       = db.Column(db.String(100), nullable=False)
    country    = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'id_stadium': self.id_stadium,
            'name':       self.name,
            'ubication':  self.ubication,
            'city':       self.city,
            'country':    self.country
        }

    