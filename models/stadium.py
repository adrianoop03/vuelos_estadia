from models.db import db

class Stadium(db.Model):
    __tablename__ = 'stadiums'
    
    id_stadium = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
    name = db.Column(db.String(100), nullable=False)
    ubication = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    def __init__(self, id_stadium, name, ubication, city, country):
        self.id_stadium = id_stadium
        self.name = name
        self.ubication = ubication
        self.city = city
        self.country = country
    
    def serialize(self):
        return {
            'id_stadium': self.id_stadium,
            'name': self.name,
            'ubication': self.ubication,
            'city': self.city,
            'country': self.country
=======
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
>>>>>>> origin/feature/stadium_team
        }

    