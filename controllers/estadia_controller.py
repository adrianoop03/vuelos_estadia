from models.estadia import ALOJAMIENTO
from models.db import db

def get_all_alojamientos():
    alojamientos = ALOJAMIENTO.query.all()
    return [alojamiento.serialize()for alojamiento in alojamientos]

def get_ciudad_alojamientos(ciudad):
    alojamientos = ALOJAMIENTO.query.filter_by(ciudad=ciudad).all()
    return [alojamiento.serialize()for alojamiento in alojamientos]

def get_alojamiento_by_pais(pais):
    alojamientos= ALOJAMIENTO.query.filter_by(pais=pais).all()
    return [alojamiento.serialize()for alojamiento in alojamientos]

def get_alojamiento_by_id(id):
    alojamientos= ALOJAMIENTO.query.filter_by(id=id).all()
    return [alojamiento.serialize()for alojamiento in alojamientos]

def create_alojamiento(nombre_alojamiento,pais,estado,ciudad):
    nuevo_alojamiento = ALOJAMIENTO(nombre_alojamiento,pais,estado,ciudad)
    db.session.add(nuevo_alojamiento)
    db.session.commit()
    return nuevo_alojamiento.serialize()

def borrar_alojamiento(id):
    alojamiento= ALOJAMIENTO.query.get(id)
    try:
        db.session.delete(alojamiento)
        db.session.commit()
        return True
    except:
        return False