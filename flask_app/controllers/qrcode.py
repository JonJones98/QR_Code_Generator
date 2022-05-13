from threading import local
from traceback import format_list
from flask import render_template,redirect,request, session
from flask_app import app
import qrcode
from PIL import Image
import urllib
from pathlib import Path
import os


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
    session['file name']=(qr_name,qr_format)
    #path_to_download_folder = (os.path.join(Path.home(), "Desktop"))
    #session['file location']="%s%c"(path_to_download_folder,session['file name'])
    session['file location']= "qr_code/%s%s"%(qr_name,qr_format)
    #img.save(path_to_download_folder+session['file name'])
    img.save(session['file location'])
    return redirect("/qrcodedownload")
    #return render_template("validateQRCreation.html",submission=data)

@app.route("/qrcodedownload")
def download():
    qr_Name = session['file name']
    qrImage = session['file location']
    return redirect("/downloads")

@app.route("/downloads")
def source():
    preview=Image.open(session['file location'])
    preview.show()
    #return render_template("succesfulQRCreation.html",preview=preview)
    return redirect("/")