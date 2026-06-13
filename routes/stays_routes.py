from flask import Blueprint,jsonify,request
from vuelos_estadia.controllers.stays_controller import *

estadia_bp = Blueprint('estadia',__name__)

@estadia_bp.route('/alojamientos',methods=['GET'])
def get_alojamientos():
    return jsonify(get_all_alojamientos())

@estadia_bp.route('/alojamientos/ciudad/<string:ciudad>',methods=['GET'])
def get_alojamientos_by_ciudad(ciudad):
    return jsonify(get_ciudad_alojamientos(ciudad))

@estadia_bp.route('/alojamientos/pais/<string:pais>',methods=['GET'])
def get_alojamientos_by_pais(pais):
    return jsonify(get_alojamientos_by_pais(pais))

@estadia_bp.route('/alojamientos/id/<int:id>',methods=['GET'])
def get_alojamientos_by_id(id):
    return jsonify(get_alojamiento_by_id(id))

@estadia_bp.route('/alojamientos',methods=['POST'])
def create_alojamiento():
    data=request.json
    create_alojamiento(data)
    return "alojamiento creado",201

@estadia_bp.route('/alojamientos/<int:id>',methods=['DELETE'])
def delete_alojamiento(id):
    try:
        borrar=delete_alojamiento(id)
        return jsonify({'mensaje':'alojamiento borrado'})
    except:
        return jsonify({'mensaje':'error al borrar el alojamiento'}),404