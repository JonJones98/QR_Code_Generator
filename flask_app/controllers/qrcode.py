
from flask import render_template,redirect,request, session
from flask_app import app
import qrcode
import os
from flask_app.models.qrcode import Validate


@app.route("/")
def index():
    return redirect("/qrcodecreation")

@app.route("/qrcodecreation")
def home():
    format_list=["Select Format",".tif",".tiff",".bmp",".jpg",".jpeg",".gif",".png",".eps",".raw",".cr2",".nef",".orf",".sr2",".pdf",".img"]
    return render_template("home_page.html",formats=format_list, urlvalue=session['url'],namevalue=session['name'],formatvalue=session['formattype'])

@app.route("/qrcodevalidate", methods=["POST"])
def validate():
    try:
        session['url']=request.form["url"]
        session['name']=request.form["filename"]
        session['formattype']=request.form["formattype"]
        if not Validate.validate_info(request.form):
            return redirect ("/")
    except:
        return redirect("/qrcodecreation")
    qr_name=str(session["name"])
    qr_format=str(session["formattype"])
    session['file name']= "%s%s"%(qr_name,qr_format)
    return render_template("index.html")
@app.route("/qrcodeproduction")
def downloadpage():
    img =qrcode.make(str(session['url'])) 
    type(img)
    file_name=session['file name']
    img.save('flask_app/static/image/'+file_name)
    return render_template("succesfulQRCreation.html")
@app.route("/qrcodedownload")
def download():
    return render_template("download_page.html",QR_name=session['file name'])
@app.route("/qrcodereset")
def loading():
    try:
        os.remove('flask_app/static/image/'+session['file name'])
    except:
        print("folder empty")
    session.clear()
    session['url']=""
    session['name']=""
    session['formattype']=""
    return redirect("/qrcodecreation")
