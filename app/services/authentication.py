from flask import Blueprint,request,render_template,redirect,url_for
from repositories.database import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user
class Authentication:
    regiser_bp=Blueprint('register_bp',__name__)
    @regiser_bp.route('/register',methods=['POST','GET'])
    def register():
        if request.method=="POST":
            email=request.form.get("email")
            password=request.form.get("password")
            base_currency=request.form.get("base_currency")
    
    login_bp=Blueprint('login_bp',__name__)
    @login_bp.route('/login',methods=['POST','GET'])
    def login():
       
        if request.methods=='POST' and 'email' in request.form and 'password' in request.form:
            email=request.form.get("email")
            password=request.form.get("password_hash")

            user=User.query.filterche_by(email=email).first()

            if user and check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for("dashboard"))
            else:
                return render_template("login.html",error="Invalid username or password")
        return render_template("login.html")
    
    logout_bp=Blueprint('logout_bp',__name__)
    @logout_bp.route('/logout',methods=['POST'])
    def logout():
        logout_user()
        return redirect(url_for("home"))