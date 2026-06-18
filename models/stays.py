from models.db import db

class ALOJAMIENTO(db.Model):
    __tablename__='ALOJAMIENTO'

    id_alojamiento= db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_alojamiento=db.Column(db.String(100), nullable=False)
    pais=db.Column(db.String(100),nullable=False)
    estado=db.Column(db.String(100),nullable=False)
    ciudad=db.Column(db.String(100),nullable=False)

    def __init__(self,nombre_alojamiento,pais,estado,ciudad):
        self.nombre_alojamiento = nombre_alojamiento
        self.pais = pais
        self.estado = estado
        self.ciudad = ciudad

    def serialize(self):
        return{
            'id_alojamiento': self.id_alojamiento,
            'nombre_alojamiento': self.nombre_alojamiento,
            'pais': self.pais,
            'estado': self.estado,
            'ciudad': self.ciudad
        }
