from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from controllers.flight_controllers import FlightController
from flask_login import login_required, current_user
from controllers.team_controller import get_all_teams

flight_bp = Blueprint('flight_bp', __name__)


@flight_bp.route('/flights', methods=['GET'])
@login_required
def get_flights():
    flights = FlightController.get_all()
    teams = get_all_teams()

    return render_template(
        'flight.html',
        flights=flights,
        teams=teams       # ← esto hace que aparezcan las selecciones
    )


@flight_bp.route('/flights/<int:id_flight>', methods=['GET'])
@login_required
def get_flight(id_flight):

    flight = FlightController.get_by_id(id_flight)

    if not flight:
        return render_template(
            'error.html',
            message='Vuelo no encontrado'
        ), 404

    return render_template(
        'flight_detail.html',
        flight=flight
    )

@flight_bp.route('/flights', methods=['POST'])
@login_required
def create_flight():
    if current_user.admin:
        data = request.get_json()
        result, status = FlightController.crear_vuelo(data)
        return jsonify(result), status
    return jsonify("No eres admin"), 400
