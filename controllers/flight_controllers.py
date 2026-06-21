from models.flight import Flight
from models.team import Team
from models.stadium import Stadium
from models.db import db

class FlightController:

    @staticmethod
    def get_all():

        resultados = db.session.query(
            Flight,
            Team.name.label("team_name"),
            Stadium.name.label("stadium_name"),
            Stadium.city.label("stadium_city")
        ).join(
            Team,
            Flight.id_team == Team.id_team
        ).outerjoin(
            Stadium,
            Flight.id_stadium == Stadium.id_stadium
        ).all()

        flights = []

        for flight, team_name, stadium_name, stadium_city in resultados:

            duracion = (
                flight.arrival_datetime -
                flight.departure_datetime
            )

            total_minutos = int(duracion.total_seconds() / 60)

            
            flights.append({
                "id_flight": flight.id_flight,
                "id_stadium": flight.id_stadium,
                "flight_number": flight.flight_number,
                "origin_city": flight.origin_city,

                "destination": stadium_name if stadium_name else "Sin estadio",
                "destination_city": stadium_city if stadium_city else flight.destination_city,

                "departure_datetime": flight.departure_datetime.strftime('%d/%m/%Y %H:%M'),
                "arrival_datetime": flight.arrival_datetime.strftime('%d/%m/%Y %H:%M'),

                "team_name": team_name,

                "duration_hours": total_minutos // 60,
                "duration_minutes": total_minutos % 60
            })

        return flights
         
    @staticmethod
    def delete(id_flight):
        flight = Flight.query.get(id_flight)

        if not flight:
            return False

        db.session.delete(flight)
        db.session.commit()

        return True