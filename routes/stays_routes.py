from flask import Blueprint,jsonify,request
from vuelos_estadia.controllers.stays_controller import *

estadia_bp = Blueprint('estadia',__name__)

@estadia_bp.route('/stays',methods=['GET'])
def get_stay():
    return jsonify(get_all_stay())

@estadia_bp.route('/stays/ciudad/<string:ciudad>',methods=['GET'])
def get_stays_by_ciudad(ciudad):
    return jsonify(get_ciudad_stay(ciudad))

@estadia_bp.route('/stays/pais/<string:pais>',methods=['GET'])
def get_stays_by_pais(pais):
    return jsonify(get_stay_by_pais(pais))

@estadia_bp.route('/stays/id/<int:id>',methods=['GET'])
def get_stays_by_id(id):
    return jsonify(get_stay_by_id(id))

@estadia_bp.route('/stays',methods=['POST'])
def create_stay():
    data=request.json
    create_stay(data)
    return "estadia creada",201

@estadia_bp.route('/stays/<int:id>',methods=['DELETE'])
def delete_stay(id):
    try:
        borrar=borrar_stay(id)
        return jsonify({'mensaje':'estadia borrada'})
    except:
        return jsonify({'mensaje':'error al borrar la estadia'}),404