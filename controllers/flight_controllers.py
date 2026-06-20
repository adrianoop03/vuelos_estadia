from datetime import datetime
from models.flight import Flight
from models.db import db


# Convierte la fecha que manda el formulario (texto) a un objeto datetime real
def _parse_datetime(value):
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        value = value.replace('T', ' ')  # "2026-06-15T18:30" -> "2026-06-15 18:30"
        return datetime.strptime(value, '%Y-%m-%d %H:%M')
    raise ValueError('Formato de fecha inválido')


class FlightController:

    # Trae todos los vuelos ( admin)
    @staticmethod
    def get_all():
        flights = Flight.query.order_by(Flight.departure_datetime).all()
        return [flight.serialize() for flight in flights]

    # Trae solo los vuelos de una selección (usuario)
    @staticmethod
    def get_by_team(id_team):
        flights = Flight.query.filter_by(id_team=id_team).order_by(Flight.departure_datetime).all()
        return [flight.serialize() for flight in flights]

    # Busca un vuelo  por id
    @staticmethod
    def get_by_id(id_flight):
        flight = Flight.query.get(id_flight)
        if not flight:
            return None
        return flight.serialize()

    # ALTA: crea un vuelo nuevo
    @staticmethod
    def create(data):
        nuevo_flight = Flight(
            flight_number=data['flight_number'],
            origin_city=data['origin_city'],
            destination_city=data['destination_city'],
            departure_datetime=_parse_datetime(data['departure_datetime']),
            arrival_datetime=_parse_datetime(data['arrival_datetime']),
            id_team=data['id_team'],
            id_stadium=data['id_stadium']
        )
        db.session.add(nuevo_flight)
        db.session.commit()
        return nuevo_flight.serialize()

    # MODIFICACIÓN: edita un vuelo existente No usar porque los vuelos no se modifican
    @staticmethod
    def update(id_flight, data):
        flight = Flight.query.get(id_flight)

        if not flight:
            return None

        flight.flight_number = data['flight_number']
        flight.origin_city = data['origin_city']
        flight.destination_city = data['destination_city']
        flight.departure_datetime = _parse_datetime(data['departure_datetime'])
        flight.arrival_datetime = _parse_datetime(data['arrival_datetime'])
        flight.id_team = data['id_team']
        flight.id_stadium = data['id_stadium']

        db.session.commit()
        return flight.serialize()

    # BAJA: elimina un vuelo
    @staticmethod
    def delete(id_flight):
        flight = Flight.query.get(id_flight)

        if not flight:
            return False

        db.session.delete(flight)
        db.session.commit()
        return True