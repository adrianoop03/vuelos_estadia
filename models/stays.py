sfrom models.db import db

class stays(db.model):
    __tablename__='stays'

    id_stays  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_stays=db.column(db.string(100), nullable=False)
    pais=db.column(db.string(100),nullable=False)
    estado=db.column(db.string(100),nullable=False)
    ciudad=db.column(db.string(100),nullable=False)

    def __init__(self,name_stays,pais,estado,ciudad):
        self.name_stays = name_stays
        self.pais = pais
        self.estado = estado
        self.ciudad = ciudad

    def serialize(self):
        return{
            'id_stays': self.id_stays,
            'name_stays': self.name_stays,
            'pais': self.pais,
            'estado': self.estado,
            'ciudad': self.ciudad
        }
