import os
import json
from app import app
from models.db import db
from models.user import User
from models.flight import Flight
from models.stadium import Stadium
from models.stays import ALOJAMIENTO
from models.team import Team

DATA_DIR = 'data'

def populate_flights(data):
    created = 0
    for item in data:
        id_flight = item.get('id_flight')
        flight_number = item.get('flight_number')
        origin_city = item.get('origin_city')
        destination_city = item.get('destination_city') 
        departure_datetime = item.get('departure_datetime')
        arrival_datetime = item.get('arrival_datetime')
        id_team = item.get('id_team')
        id_stadium = item.get('id_stadium')

        if not id_flight or not flight_number:
            continue

        exists = Flight.query.filter(Flight.id_flight == id_flight).first()
        if exists:
            continue

        flight = Flight(
            id_flight=id_flight,
            flight_number=flight_number,
            origin_city=origin_city,
            destination_city=destination_city,
            departure_datetime=departure_datetime,
            arrival_datetime=arrival_datetime,
            id_team=id_team,
            id_stadium=id_stadium
        )
        db.session.add(flight)
        created += 1

    return created

def populate_teams(data):
    created = 0
    for item in data:
        id_team = item.get('id_team')
        name = item.get('name')
        
        if not id_team or not name:
            continue

        exists = Team.query.filter(Team.id_team == id_team).first()
        if exists:
            continue

        team = Team(
            id_team=id_team,
            name=name
        )
        db.session.add(team)
        
        created += 1

    return created

def populate_stadiums(data):
    created = 0
    for item in data:
        id_stadium = item.get('id_stadium')
        name = item.get('name')
        ubication = item.get('ubication')
        city = item.get('city')
        country = item.get('country')

        if not id_stadium or not name:
            continue

        exists = Stadium.query.filter(Stadium.id_stadium == id_stadium).first()
        if exists:
            continue

        stadium = Stadium(
            id_stadium=id_stadium,
            name=name,
            ubication=ubication,
            city=city,
            country=country
        )
        db.session.add(stadium)
        
        created += 1

    return created

def populate_all():
    with app.app_context():
        print("Entrando en el contexto de la app...")
        for filename in os.listdir(DATA_DIR):
            print(f"Revisando archivo: {filename}")
            if not filename.endswith('.json'):
                print(f"Archivo ignorado: {filename}")
                continue

            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)

            print(f"Datos cargados desde {filename}: {data}")

            if 'flights' in filename:
                created = populate_flights(data)
                print(f'{created} vuelos cargados desde {filename}')
            elif 'teams' in filename:
                created = populate_teams(data)
                print(f'{created} equipos cargados desde {filename}')
            elif 'stadiums' in filename:
                created = populate_stadiums(data)
                print(f'{created} estadios cargados desde {filename}')
            else:
                print(f'Se ignoró el archivo {filename}, tipo desconocido.')

        print("Haciendo commit a la base de datos...")
        db.session.commit()


if __name__ == '__main__':
    populate_all()