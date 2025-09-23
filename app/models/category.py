from repositories.database import db
from models.user import User


class Category(db.Model):
    __tablename__="category_data"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user_data.user_id'), nullable=False)
    name=db.Column(db.String,nullable=False)