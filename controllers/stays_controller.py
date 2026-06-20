from models.stays import stays
from models.db import db

def get_all_stay():
    stay = stays.query.all()
    return [stay.serialize()for stay in stay]

def get_ciudad_stay(ciudad):
    stay = stays.query.filter_by(ciudad=ciudad).all()
    return [stay.serialize()for stay in stay]

def get_stay_by_pais(pais):
    stay= stays.query.filter_by(pais=pais).all()
    return [stay.serialize()for stay in stay]

def get_stay_by_id(id):
    stay= stays.query.filter_by(id=id).all()
    return [stay.serialize()for stay in stay]

def create_stay(name_stays,pais,estado,ciudad):
    new_stay = stays(name_stays,pais,estado,ciudad)
    db.session.add(new_stay)
    db.session.commit()
    return new_stay.serialize()

def borrar_stay(id):
    stay= stays.query.get(id)
    try:
        db.session.delete(stay)
        db.session.commit()
        return True
    except:
        return False