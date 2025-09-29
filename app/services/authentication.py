from flask import Blueprint,request,render_template,redirect,url_for
from repositories.database import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user,login_required,current_user


register_bp=Blueprint('register_bp',__name__)
@register_bp.route('/register',methods=['POST','GET'])
def register():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        base_currency=request.form.get("base_currency")

        if User.query.filter_by(email=email).first():
            return render_template("sign_up.html",erorr="Email already taken!")
            
        hashed_password=generate_password_hash(password,method="pbkdf2:sha256")

        new_user=User(email=email,password_hash=hashed_password,base_currency=base_currency)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login_bp.login"))
    return render_template("sign_up.html")
    
login_bp=Blueprint('login_bp',__name__)
@login_bp.route('/login',methods=['POST','GET'])
def login():
       
    if request.method=='POST' and 'email' in request.form and 'password' in request.form:
        email=request.form.get("email")
        password=request.form.get("password")

        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash,password):
            login_user(user)
            return redirect(url_for("dashboard_bp.dashboard"))
        else:
            return render_template("login.html",error="Invalid username or password")
    return render_template("login.html")
    
logout_bp=Blueprint('logout_bp',__name__)
@logout_bp.route('/logout',methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("home_bp.home"))

dashboard_bp=Blueprint('dashboard_bp',__name__)
@dashboard_bp.route('/dashboard',methods=['GET'])
@login_required
def dashboard():
    return render_template("dashboard.html",email=current_user.email)