from repositories.database import db
from models.user import User
from datetime import datetime
from sqlalchemy import Enum


class Transaction(db.Model):
    
    __tablename__="transaction_data"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user_data.user_id'))
    amount=db.Column(db.Numeric(15,3),nullable=False)
    currency=db.Column(db.String(3),nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey('category_data.id'), nullable=False)
    transaction_date=db.Column(db.DateTime,default=datetime.now)
    