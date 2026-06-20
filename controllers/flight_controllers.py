from models.flight_models import Flight
from models.db import db


class FlightController:


    @staticmethod
    def get_all():
        flights = Flight.query.all()
        return [flight.serialize() for flight in flights]


    @staticmethod
    def get_by_id(id_flight):
        flight = Flight.query.get(id_flight)

        if not flight:
            return None

        return flight.serialize()


    @staticmethod
    def delete(id_flight):
        flight = Flight.query.get(id_flight)

        if not flight:
            return False

        db.session.delete(flight)
        db.session.commit()

        return True
    

    @staticmethod
    def update(id_flight, data):
        flight = Flight.query.get(id_flight)

        if not flight:
            return None

        flight.flight_number = data['flight_number']
        flight.airline = data['airline']
        flight.origin_city = data['origin_city']
        flight.origin_airport = data['origin_airport']
        flight.destination_city = data['destination_city']
        flight.destination_airport = data['destination_airport']
        flight.departure_datetime = data['departure_datetime']
        flight.arrival_datetime = data['arrival_datetime']
        flight.id_team = data['id_team']

        db.session.commit()

        return flight.serialize()
    

    @staticmethod
    def patch(id_flight, data):
        flight = Flight.query.get(id_flight)

        if not flight:
            return None

        for key, value in data.items():
            if hasattr(flight, key):
                setattr(flight, key, value)

        db.session.commit()

        return flight.serialize()