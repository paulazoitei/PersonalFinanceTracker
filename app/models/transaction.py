from repositories.database import db
from decimal import *
from user import User
from datetime import datetime
from sqlalchemy import Enum
from enum import TypeEnum

class Transaction(db.Model):
    
    __tablename__="transaction_data"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user_data.user_id'))
    amount=db.Column(db.Decimal(15,3),nullable=False)
    currency=db.Column(db.String(3),nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey('category_data.category_id'), nullable=False)
    date=db.Column(db.datetime,default=lambda:datetime.now(),nullable=False)
    type=db.Column(Enum(TypeEnum,name="typeenum"),nullable=False)