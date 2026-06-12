from models.stadium import Stadium
from models.db import db

def get_all_stadiums():
    stadiums = Stadium.query.all()
    return [stadium.serialize() for stadium in stadiums]

def get_stadium_by_id(id_stadium):
    stadium = Stadium.query.get(id_stadium)
    if not stadium:
        return None
    return stadium.serialize()