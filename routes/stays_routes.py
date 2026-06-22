from flask import Blueprint,jsonify,request, render_template
from controllers.stays_controller import *
from models.stays import stays
from flask_login import login_required, current_user

estadia_bp = Blueprint('estadia',__name__)

@estadia_bp.route('/stays',methods=['GET'])
@login_required
def get_stay():
    stay=get_all_stay()
    return render_template('stays.html', stays=stay)

@estadia_bp.route('/stays/json', methods=['GET'])
@login_required
def get_stays_json():
    stays_list = get_all_stay()
    return jsonify([s.serialize() for s in stays_list])

@estadia_bp.route('/stays/ciudad/<string:ciudad>',methods=['GET'])
@login_required
def get_stays_by_ciudad(ciudad):
    stay=get_ciudad_stay(ciudad)
    if not stay:
        return render_template('error.html', mensaje='estadia no encontrada'),404
    return render_template('stays.html', stays=stay ),201


@estadia_bp.route('/stays/pais/<string:pais>',methods=['GET'])
@login_required
def get_stays_by_pais(pais):
    stay=get_stay_by_pais(pais)
    if not stays:
        return render_template('error.html', mensaje='estadia no encontrada'),404
    return render_template('stays.html', stays=stay),201    


@estadia_bp.route('/stays/id/<int:id>',methods=['GET'])
@login_required
def get_stays_by_id(id):
    stay=get_stay_by_id(id)
    if not stay:
        return render_template('error.html', mensaje='estadia no encontrada'),404
    return render_template('stays.html', stays=stay ),201

@estadia_bp.route('/stays',methods=['POST'])
@login_required
def create_stay():
    if current_user.admin():
            data=request.get_json()
            stay=create_stay(data)
            return jsonify(stay),201
