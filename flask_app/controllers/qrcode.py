from traceback import format_list
from flask import render_template,redirect,request, session
from flask_app import app
from flask_app.models.qrcode import Dojos
import qrcode
from PIL import Image

@app.route("/")
def index():
    return redirect("/qrcodecreation")

@app.route("/qrcodecreation")
def home():
    format_list=[".tif",".tiff",".bmp",".jpg",".jpeg",".gif",".png",".eps",".raw",".cr2",".nef",".orf",".sr2",".pdf",".img"]
    return render_template("home_page.html",formats=format_list)

@app.route("/qrcodevalidate", methods=["POST"])
def validate():
    session['url']=request.form["url"]
    session['filename']=request.form["filename"]
    session['formattype']=request.form["formattype"]
    qr_url=str(session['url'])
    qr_name=str(session["filename"])
    qr_format=str(session["formattype"])
    img =qrcode.make(qr_url)
    type(img)
    session['file location']= "Standard format/qr_code/%s%s"%(qr_name,qr_format)
    img.save(session['file location'])
    print("validate")
    return redirect("/qrcodedownload")
    #return render_template("validateQRCreation.html",submission=data)

@app.route("/qrcode_create")
def create():
    qr_url=session['url']
    qr_name=session["filename"]
    qr_format=session["formattype"]
    img =qrcode.make(qr_url)
    type(img)
    img.save("Standard format/qr_code/"+qr_name+qr_format)
    #session['save_location']=img.save(qr_name+"."+qr_format)
    return redirect("/")

@app.route("/qrcodedownload")
def download():
    qrImage = Image.open(session['file location'])
    preview=qrImage.show()
    return render_template("succesfulQRCreation.html",preview=preview)
