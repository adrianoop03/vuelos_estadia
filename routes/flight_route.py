from flask import Blueprint, jsonify
from controllers.flight_controllers import FlightController

flight_bp = Blueprint('flight_bp', __name__)


@flight_bp.route('/flights', methods=['GET'])
def get_flights():
    flights = FlightController.get_all()
    return jsonify(flights), 200


@flight_bp.route('/flights/<int:id_flight>', methods=['GET'])
def get_flight(id_flight):
    flight = FlightController.get_by_id(id_flight)

    if not flight:
        return jsonify({
            "message": "Vuelo no encontrado"
        }), 404

    return jsonify(flight), 200


@flight_bp.route('/flights/<int:id_flight>', methods=['DELETE'])
def delete_flight(id_flight):
    deleted = FlightController.delete(id_flight)

    if not deleted:
        return jsonify({
            "message": "Vuelo no encontrado"
        }), 404

    return jsonify({
        "message": "Vuelo eliminado correctamente"
    }), 200