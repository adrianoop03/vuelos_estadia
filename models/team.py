from models.db import db

class Team(db.Model):
    __tablename__ = 'teams'

    id_team = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

def __init__(self, name):
    self.name = name

def serialize(self):
    return {
        'id_team': self.id_team,
        'name': self.name
    }
