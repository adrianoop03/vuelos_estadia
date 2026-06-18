import os
import json
from app import app
from models.db import db
from models.user import User
from models.flight_models import Flight
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
            id_team=id_team
        )
        db.session.add(flight)
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
            else:
                print(f'Se ignoró el archivo {filename}, tipo desconocido.')

        print("Haciendo commit a la base de datos...")
        db.session.commit()


if __name__ == '__main__':
    populate_all()