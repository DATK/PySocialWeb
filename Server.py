from flask import Flask,request,redirect,url_for,abort,session,render_template,flash,make_response
import random
from src.config import *
from src.SQL import SQL
from src.Chat import Chat
import datetime
from src.shifr import sh,unsh
import hashlib



sql=SQL(DATEBASE)
sql.create_table()
del sql

app=Flask(__name__)
app.config["SECRET_KEY"]=SECRET_KEY
app.permanent_session_lifetime=datetime.timedelta(hours=12)

@app.route("/")
def other():
    return redirect(MAIN_ADRES)

@app.route("/<path:way>")
def other2(way):
    return redirect(MAIN_ADRES)

@app.route(f"{UPLOAD_FILE}/<id>",methods=["POST"])
def upload(id):
    session.permanent=True
    if request.method=="POST":
        if "login" in session and "loginin" in session and "id" in session:
            sql=SQL(DATEBASE)
            file=request.files["file"]
            try:
                img=file.read()
                sql.change_ava(img,id)
            except:
                pass
    return redirect(url_for('user',id=id))

@app.route(f'{AVA}/<id>')
def setava(id):
    sql=SQL(DATEBASE)
    img=sql.get_ava(id)
    if img!=[]:
        h=make_response(img)
        h.headers['Content-Type']='image/'
        return h
    else:
        return ""
 

@app.route(MAIN_ADRES,methods=["GET","POST"])
def mainForm():
    session.permanent=True
    if "loginin" not in session:
        session["loginin"]=False
    if "login" not in session:
        session["login"]=""
    if "id" not in session:
        session["id"]=""
    if request.method=="GET":
        return render_template("main.html")
    elif request.method=="POST":
        data=request.form
        sql=SQL(DATEBASE)
        if len(data)==4:
            ERROR=False
            if len(data["login"])<4:
                flash("Логин должен быть не менее 3 символов",category="error")
                ERROR=True
            if len(data["name"])<1 and len(data["surname"]<1):
                flash("Имя и фамилия должны иметь не менее 1 символа",category="error")
                ERROR=True
            if len(data["password"])<8:
                flash("Парроль должен содержать не менее 8 символов",category="error")
                ERROR=True
            if ERROR:
                return redirect(MAIN_ADRES)
            if sql.reg_user(data["login"],data["name"],data["surname"],hashlib.md5(data["password"].encode()).hexdigest()):
                flash("Пользователь успешно зарегестрирован",category="success")
            else:
                flash("Вероятно, данный логин уже занят",category="error")
        elif len(data)==2:
            if sql.vhod_user(data["login"],hashlib.md5(data["password"].encode()).hexdigest()):
                user_id=sql.get_id_user(data["login"])
                session["loginin"]=True
                session["login"]=data["login"]
                session["id"]=user_id
                del sql
                return redirect(f"{USER}/{user_id}")
            else:
                flash("Неправильный логин или пароль",category="error")
        del sql
        return redirect(MAIN_ADRES)

@app.route(f"{USER}/<id>",methods=["GET","POST"])
def user(id):
    session.permanent=True
    sql=SQL(DATEBASE)
    if "login" in session and "loginin" in session and session["id"]==id:
        if request.method=="GET":
            data=sql.get_info(id)
            user_info=sql.get_dop_info(id)
            return render_template("user_logining.html",data=data,user_info=user_info)
        elif request.method=="POST":
            return redirect(f"{USER}/{id}")
    else:
        if request.method=="GET":
            data=sql.get_info(id)
            user_info=sql.get_dop_info(id)
            return render_template("user_notlog.html",data=data,user_info=user_info)
        elif request.method=="POST":
            return redirect(f"{USER}/{id}")

@app.route(f"{MESSAGES}/<id>",methods=["GET","POST"])
def messanges(id):
    sql=SQL(DATEBASE)
    if "login" in session and "loginin" in session and "id" in session and session["id"]!="":
        current_id=session["id"]
        #print(current_id)
        chat=Chat([id,current_id])
        sms=chat.get_sms()
        name=sql.get_name(current_id)
        if request.method=="GET":
            return render_template("chating_login.html",messages=[unsh(i) for i in sms])
        elif request.method=="POST":
            try:
                text=request.form["text"]
            except:
                text=""
            if text!="" or text!=" ":
                text=sh(f"{name}--->>> {text}")
                chat.add_sms(text)
                
            return redirect(url_for('messanges',id=id))
    else:
        flash("Войдите в аккаунт для общения" ,category="error")
        return redirect(MAIN_ADRES)
            
@app.route(f"{USER}/exit",methods=["GET","POST"])
def logout(): 
    if "login" in session and "loginin" in session and session["id"]!=id:
        del session["login"]
        del session["loginin"]
        del session["id"]
        return redirect(MAIN_ADRES)
  
@app.route(USER,methods=["GET","POST"])
def list_users():
    session.permanent=True
    sql=SQL(DATEBASE)
    data=sql.list_users()
    if request.method=="GET":  
        return render_template("list_users.html",ln=len(data),data=[random.choice(data) for i in range(random.randint(15,30))])
    elif request.method=="POST":
        return redirect(USER)
    
@app.route(f"{SETTINGS}/<id>",methods=["GET","POST"])
def settings(id):
    if "login" in session and "loginin" in session and session["id"]==id:
        sql=SQL(DATEBASE)
        if request.method=="GET":
            return render_template("user_settings.html",id=id)
        elif request.method=="POST":
            data=request.form
            if "password" in data:
                if len(data["password"])<8:
                    return redirect(url_for('settings',id=id))
                data={"password":hashlib.md5(data["password"].encode()).hexdigest()}
            sql.settings_ch(data,id)    
            return redirect(url_for('settings',id=id))
    else:
        return redirect(url_for('mainForm'))
    