from models.stays import stays
from models.db import db

# obtener todas las estadias
def get_all_stay():
    stay = stays.query.all()
    return [stay.serialize()for stay in stay]


# obtener estadias por ciudad
def get_ciudad_stay(ciudad):
    stay = stays.query.filter_by(ciudad=ciudad).all()
    return [stay.serialize()for stay in stay]


#obtener estadias por pais
def get_stay_by_pais(pais):
    stay= stays.query.filter_by(pais=pais).all()
    return [stay.serialize()for stay in stay]


# obtener estadias por id
def get_stay_by_id(id):
    stay= stays.query.filter_by(id=id).all()
    return [stay.serialize()for stay in stay]


# subir una nueva estadia
def create_stay(team,name_stays,pais,estado,ciudad):
    new_stay = stays(team,name_stays,pais,estado,ciudad)
    db.session.add(new_stay)
    db.session.commit()
    return new_stay.serialize()


# borrar la estadia
def borrar_stay(id):
    stay= stays.query.get(id)
    try:
        db.session.delete(stay)
        db.session.commit()
        return True
    except:
        return False