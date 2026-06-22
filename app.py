from atexit import register
from unicodedata import category

from flask import Flask, render_template
from config.config import *

from models.db import db
from sqlalchemy.exc import OperationalError
from sqlalchemy_utils import database_exists, create_database
from flask_mail import Mail
from routes.user_route import user_bp
from routes.flight_route import flight_bp
from routes.stadium_routes import stadium_bp
from routes.stays_routes import estadia_bp
from routes.team_routes import team_bp

from flask import Flask, render_template, session, redirect, url_for
from models.user import User

from extensions import mail, login_manager

app = Flask(__name__)

#Configuracion de mail automatizado


app.config['MAIL_SERVER'] = mail_server
app.config['MAIL_PORT'] = mail_port
app.config['MAIL_USE_TLS'] = use_tls
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail.init_app(app)

#Configuracion de base de datos

app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Configuracion del sistema de login

app.config['SECRET_KEY'] = secret_key

login_manager.init_app(app)

#Rutas de cada clase

app.register_blueprint(user_bp)
app.register_blueprint(flight_bp)
app.register_blueprint(stadium_bp)
app.register_blueprint(estadia_bp)
app.register_blueprint(team_bp)

#Verificacion de base de datos

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
#index 
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/admin')
def admin():
    if not session.get('user_id') or not session.get('is_admin'):
        return redirect(url_for('user.login_page'))

    current_user = User.query.get(session['user_id'])

    
    return render_template("admin.html", current_user=current_user)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    from models.user import User
    from models.flight import Flight
    from models.team import Team
    from models.stays import stays
    from models.stadium import Stadium
    # db.drop_all()
    db.create_all()
    
    

if __name__ == '__main__':
    app.run(debug=True)