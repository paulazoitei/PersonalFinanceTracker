from repositories.database import db
from datetime import datetime

class User(db.Model):
    __tablename__='user_data'
    email=db.Column(db.String(50),nullable=False,unique=True)
    base_currency=db.Column(db.String(3),nullable=False)
    created_at=db.Column(db.Integer,default=lambda: datetime.now(),nullable=False)
    