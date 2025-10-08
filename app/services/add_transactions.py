from flask import Blueprint,request
from repositories.database import db
from models.transaction import Transaction
from models.category import Category
from decimal import Decimal, InvalidOperation



add_transaction_bp=Blueprint('add_transaction_bp',__name__)
@add_transaction_bp.route('/add_transaction',methods=['POST'])
def add_transaction():
        amount_raw=request.form.get("amount")
        currency=request.form.get("currency")
        category=request.form.get("category")
    
        
        try:
            amount=Decimal(amount_raw)
        except InvalidOperation:
            return render_template("dashboard.html",error="Invalid amount format.")
        
        amount=amount.quantize(Decimal("0.01"))
        if amount <=0 or amount(Decimal("100000000")):
            return render_template("dashboard.html",error="Amount out of range")
    
    
    