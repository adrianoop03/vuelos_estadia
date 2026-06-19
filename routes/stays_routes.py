from flask import Blueprint,jsonify,request
from vuelos_estadia.controllers.stays_controller import *

estadia_bp = Blueprint('estadia',__name__)

@estadia_bp.route('/stays',methods=['GET'])
def get_stay():
     stay=get_all_stay()
    return render_template('stays.html', stays=stay)

@estadia_bp.route('/stays/ciudad/<string:ciudad>',methods=['GET'])
def get_stays_by_ciudad(ciudad):
    stay=get_ciudad_stay(ciudad)
    if not stay:
        return render_template('error.html', mensaje='estadia no encontrada'),404
    return render_template('stays.html', stays=stay ),201


@estadia_bp.route('/stays/pais/<string:pais>',methods=['GET'])
def get_stays_by_pais(pais):
     stay=get_stay_by_pais(pais)
    if not stay:
        return render_template('error.html', mensaje='estadia no encontrada'),404
    return render_template('stays.html', stays=stay),201    


@estadia_bp.route('/stays/id/<int:id>',methods=['GET'])
def get_stays_by_id(id):
    stay=get_stay_by_id(id)
    if not stay:
        return render_template('error.html', mensaje='estadia no encontrada'),404
    return render_template('stays.html', stays=stay ),201

@estadia_bp.route('/stays',methods=['POST'])
def create_stay():
   data=request.get_json()
    stay=create_stay(data)
    return jsonify(stay),201


@estadia_bp.route('/stays/<int:id>',methods=['DELETE'])
def delete_stay(id):
     delete=borrar_stay(id)
    try:
        borrar=borrar_stay(id)
        return "",201
    except:
        return render_template('error.html', mensaje='error al borrar la estadia'),404
