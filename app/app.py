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
from services.authentication import register_bp, login_bp, logout_bp,dashboard_bp
from flask import Flask, render_template, Blueprint
from flask_login import LoginManager
from routes.home import home_bp
import os
from dotenv import load_dotenv


class AppFactory:

    
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.configure_extensions()
        self.configure_login()
        self.register_routes()
        
    
        
    def configure_login(self):
        self.login_manager=LoginManager()
        self.login_manager.login_view = "login"
        self.login_manager.init_app(self.app)
        
        @self.login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))
            

    def configure_app(self):
        self.app.config.from_object(Config)
        self.app.config["SECRET_KEY"]=os.getenv("SECRET_KEY") or "sdajhoiwhyroqyhrohkjhsfkjah"
        
        
        self.app.config['SESSION_TYPE']='filesystem'
        

    def configure_extensions(self):
        db.init_app(self.app)
        Migrate(self.app, db)

    def create_app(self):
        return self.app

    def register_routes(self):
        self.app.register_blueprint(register_bp)
        self.app.register_blueprint(login_bp)
        self.app.register_blueprint(logout_bp)
        self.app.register_blueprint(home_bp)
        self.app.register_blueprint(dashboard_bp)


app = AppFactory().create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)