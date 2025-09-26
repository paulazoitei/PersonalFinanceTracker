from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from repositories.database import db
import psycopg2
from flask_migrate import Migrate
from models.user import User
from models.enum import TypeEnum
from models.transaction import Transaction
from models.category import Category
from services.authentication import register_bp, login_bp, logout_bp
from flask import Flask, render_template, Blueprint
from flask_login import LoginManager,login_manager


class AppFactory:
    home_bp = Blueprint('home_bp', __name__)

    @home_bp.route('/', methods=['POST', 'GET'])
    def home():
        return render_template("home.html")
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.configure_extensions()
        self.login_manager()

    def login_manager(self):
        login_manager = LoginManager()
        login_manager.init_app(self.app)
        login_manager.login_view = "login"

    def configure_app(self):
        self.app.config.from_object(Config)

    def configure_extensions(self):
        db.init_app(self.app)
        Migrate(self.app, db)

    def create_app(self):
        return self.app

    def register_routes(self):
        self.app.register_blueprint(register_bp)
        self.app.register_blueprint(login_bp)
        self.app.register_blueprint(logout_bp)
        self.app.register_blueprint(AppFactory.home_bp)


app = AppFactory().create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)