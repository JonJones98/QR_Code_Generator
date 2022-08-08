
from flask import render_template,redirect,request, session
from flask_app import app
import qrcode
import os
from flask_app.models.qrcode import Validate
import shutil


@app.route("/")
def index():
    session['url']=""
    session['name']=""
    session['formattype']=""
    return render_template("dashboard.html")
@app.route("/error")
def val_error():
    return redirect("/qr/create")

@app.route("/createuser", methods=["POST"])
def val_2():
    return redirect("/userportal/loginresitraion")
@app.route("/finduser", methods=["POST"])
def val_1():
    return redirect("/userportal/loginresitraion")
@app.route("/userportal/loginresitraion")
def loginRegistration():
    return render_template("loginRegistration.html")
@app.route("/qr/create")
def home():
    dir = 'flask_app/static/image_folder'
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
    try:
        format_list=["Select Format",".tif",".tiff",".bmp",".jpg",".jpeg",".gif",".png",".eps",".raw",".cr2",".nef",".orf",".sr2",".pdf",".img"]
        return render_template("home_page.html",formats=format_list, urlvalue=session['url'],namevalue=session['name'],formatvalue=session['formattype'])
    except:
        return redirect("/")

@app.route("/qr/constructing", methods=["POST"])
def validate_and_constructing():
    try:
        session['url']=request.form["url"]
        session['name']=request.form["filename"]
        session['formattype']=request.form["formattype"]
        if not Validate.validate_info(request.form):
            return redirect ("/error")
    except:
        return redirect("/qr/create")
    qr_name=str(session["name"])
    qr_format=str(session["formattype"])
    session['file name']= "%s%s"%(qr_name,qr_format)
    return render_template("index.html")
@app.route("/qr/complete")
def complete():
    try:
        img=qrcode.make(str(session['url'])) 
        type(img)
        file_name=session['file name']
        img.save('flask_app/static/image_folder/'+file_name)
        return render_template("succesfulQRCreation.html")
    except:
        return render_template("errorQRCreation.html")
@app.route("/qr/download")
def download():
    return render_template("download_page.html",QR_name=session['file name'])
@app.route("/qr/reset")
def loading():
    try:
        os.remove('flask_app/static/image_folder/'+session['file name'])
    except:
        print("folder empty")
    session.clear()
    return redirect("/")
