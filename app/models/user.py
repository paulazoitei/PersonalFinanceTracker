from repositories.database import db
from datetime import datetime

class User(db.Model):
    __tablename__='user_data'
    user_id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50),nullable=False,unique=True)
    password_hash=db.Column(db.String(100),nullable=False)
    base_currency=db.Column(db.String(3),nullable=False)
    created_at=db.Column(db.Integer,default=lambda: datetime.now(),nullable=False)
    