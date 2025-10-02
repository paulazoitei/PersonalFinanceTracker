from repositories.database import db
from datetime import datetime
from flask_login import  UserMixin

class User(UserMixin,db.Model):
    __tablename__='user_data'
    user_id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50),nullable=False,unique=True)
    password_hash=db.Column(db.String(1000),nullable=False)
    base_currency=db.Column(db.String(3),nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.now)
    
    def get_id(self):
        return str(self.user_id)    