from models.db import db
from models.team import Team
from models.stadium import Stadium

class Flight(db.Model):
    __tablename__ = 'flights'

    id_flight = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(20), nullable=False)
    origin_city = db.Column(db.String(100), nullable=False)
    destination_city = db.Column(db.String(100), nullable=False)
    departure_datetime = db.Column(db.DateTime, nullable=False)
    arrival_datetime = db.Column(db.DateTime, nullable=False)
    id_team = db.Column(db.Integer, db.ForeignKey('teams.id_team'), nullable=False)
    id_stadium = db.Column(db.Integer, db.ForeignKey('stadiums.id_stadium'), nullable=False)


    
    def __init__(self, id_flight, flight_number, origin_city,
                 destination_city, departure_datetime,
                 arrival_datetime, id_team, id_stadium):
        self.id_flight = id_flight
        self.flight_number = flight_number
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.departure_datetime = departure_datetime
        self.arrival_datetime = arrival_datetime
        self.id_team = id_team
<<<<<<< HEAD
        self.id_stadium = id_stadium
=======
        self.team=self.team
        self.stadium=self.stadium
      
>>>>>>> feature/vuelos

    def serialize(self):
        return {
            'id_flight': self.id_flight,
            'flight_number': self.flight_number,
<<<<<<< HEAD
=======
            'airline': self.airline,
>>>>>>> feature/vuelos
            'origin_city': self.origin_city,
            'destination_city': self.destination_city,
            'departure_datetime': self.departure_datetime.strftime('%Y-%m-%d %H:%M'),
            'arrival_datetime': self.arrival_datetime.strftime('%Y-%m-%d %H:%M'),
            'id_team': self.id_team,
<<<<<<< HEAD
            'id_stadium': self.id_stadium
=======
            'team': self.team,
            'stafium': self.stadium
>>>>>>> feature/vuelos
        }