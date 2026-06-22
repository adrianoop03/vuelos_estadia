from flask_mail import Mail

mail = Mail()

from flask_login import LoginManager

login_manager = LoginManager()

login_manager.login_view = 'user.login_page'
login_manager.login_message = 'Debes iniciar sesión para acceder.'
login_manager.login_message_category = 'warning'