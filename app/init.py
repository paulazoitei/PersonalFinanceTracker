from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

class AppFactory:
    def __init__(self):
        self.app=Flask(__name__)
        self.configure_app()

    def configure_app(self):
        self.app.config.from_object(Config)

    def create_app(self):
        return self.app
    
app=AppFactory().create_app()

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8081)