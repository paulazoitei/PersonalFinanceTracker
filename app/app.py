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

class AppFactory:
    def __init__(self):
        self.app=Flask(__name__)
        self.configure_app()
        self.configure_extensions()


    def configure_app(self):
        self.app.config.from_object(Config)
    def configure_extensions(self):
        db.init_app(self.app)
        Migrate(self.app,db)
    def create_app(self):
        return self.app
    
app=AppFactory().create_app()

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8081)