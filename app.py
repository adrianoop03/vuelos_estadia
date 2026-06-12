import token
from unicodedata import category

from flask import Flask
from config.config import DATABASE_CONNECTION_URI
from routes.client_route import client
from routes.vehicle_route import vehicle
from routes.location_route import location
from routes.register_route import register
from routes.category_routes import category

from models.db import db
from sqlalchemy.exc import OperationalError
from sqlalchemy_utils import database_exists, create_database
from flask_mail import Mail
app = Flask(__name__)

app.register_blueprint(client)
app.register_blueprint(vehicle)
app.register_blueprint(location)
app.register_blueprint(register)
app.register_blueprint(category)


app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

try:
    if not database_exists(DATABASE_CONNECTION_URI):
        print("Base de datos no encontrada! \nCreando base de datos...")
        create_database(DATABASE_CONNECTION_URI)
        print("Base de datos creada!")
except OperationalError:
    print("Error de conexión a la base de datos. Verifique que las credenciales sean correctas y la configuración.")
    exit()
except Exception:
    print("Error al crear la base de datos")


db.init_app(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'

with app.app_context():
    from models.user import Usuario
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)