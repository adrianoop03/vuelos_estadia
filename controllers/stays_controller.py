from models.stays import stays
from models.db import db

# obtener todas las estadias
def get_all_stay():
    stay = stays.query.all()
    return [s.serialize() for s in stay]


# obtener estadias por ciudad
def get_ciudad_stay(ciudad):
    result = stays.query.filter_by(ciudad=ciudad).all()
    return [s.serialize() for s in result]


# obtener estadias por pais
def get_stay_by_pais(pais):
    result = stays.query.filter_by(pais=pais).all()
    return [s.serialize() for s in result]


# obtener estadia por id
def get_stay_by_id(id):
    stay = stays.query.get(id)
    return stay.serialize() if stay else None


# subir una nueva estadia
def create_stay(team, name_stays, pais, estado, ciudad):
    new_stay = stays(team, name_stays, pais, estado, ciudad)
    db.session.add(new_stay)
    db.session.commit()
    return new_stay.serialize()


# actualizar una estadia
def update_stay(id, team, name_stays, pais, estado, ciudad):
    stay = stays.query.get(id)
    if not stay:
        return None
    stay.team = team
    stay.name_stays = name_stays
    stay.pais = pais
    stay.estado = estado
    stay.ciudad = ciudad
    db.session.commit()
    return stay.serialize()


# borrar la estadia
def borrar_stay(id):
    stay = stays.query.get(id)
    if not stay:
        return False
    try:
        db.session.delete(stay)
        db.session.commit()
        return True
    except:
        return False
