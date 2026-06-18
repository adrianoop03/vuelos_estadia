from atexit import register
from unicodedata import category

from flask import Flask, render_template
from config.config import DATABASE_CONNECTION_URI

from models.db import db
from sqlalchemy.exc import OperationalError
from sqlalchemy_utils import database_exists, create_database


app = Flask(__name__)


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

@app.route('/admin')
def admin():
    return render_template("register.html")


with app.app_context():
    from models.user import User
    from models.flight import Flight
    from models.stadium import Stadium
    from models.stays import ALOJAMIENTO
    from models.team import Team
    # db.drop_all()
    db.create_all()
    
    

if __name__ == '__main__':
    app.run(debug=True)