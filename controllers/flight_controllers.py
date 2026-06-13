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