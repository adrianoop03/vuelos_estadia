from models.db import db

class Stay(db.Model):
    __tablename__='stays'

    id_stays  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team = db.Column(db.String(100), nullable=False)
    name_stays=db.Column(db.String(100), nullable=False)
    pais=db.Column(db.String(100),nullable=False)
    estado=db.Column(db.String(100),nullable=False)
    ciudad=db.Column(db.String(100),nullable=False)

    def __init__(self,team,name_stays,pais,estado,ciudad):
        self.team = team
        self.name_stays = name_stays
        self.pais = pais
        self.estado = estado
        self.ciudad = ciudad

    def serialize(self):
        return{
            'id_stays': self.id_stays,
            'team': self.team,
            'name_stays': self.name_stays,
            'pais': self.pais,
            'estado': self.estado,
            'ciudad': self.ciudad
        }
