import shutil
import requests
from threading import local
from traceback import format_list
from flask import render_template,redirect,request, session
from flask_app import app
import qrcode
from PIL import Image
import urllib
from pathlib import Path
import os
import base64


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
    #path_to_download_folder = (os.path.join(Path.home(), "Downloads"))
    #session['file location']="%s%c"(path_to_download_folder,session['file name'])
    session['file location']= "qr_code/%s%s"%(qr_name,qr_format)
    #img.save(path_to_download_folder+session['file name'])
    img.save(session['file location'])
    #prepre=Image.SAVE(session['file location'])
    preview=Image.open(session['file location'])
    preview.show()
    pre=session['file location']
    #preview.tobytes(encoder_name=(os.path.join(Path.home(), "Desktop")))
    return redirect("/qrcodedownload")
    #return render_template("validateQRCreation.html",submission=data)

@app.route("/qrcodedownload")
def download():
    qr_Name = str(session['file name'])
    qrImage = (session['file location'])
    #image = open(qrImage, 'rb') #open binary file in read mode
    #image_read = image.read()
    #image_64_encode = base64.b64encode(image_read)
    url="qr_code"
    #res = request.get(url, stream=True)
    #with open(os.path.join(Path.home(), "Downloads",str(session["filename"])),'wb')as f:
     #   shutil.copyfileobj(qrImage, f)
    return redirect("/downloads")

@app.route("/downloads")
def source():
    #preview=Image.open(session['file location'])
    #preview.show()
    #return render_template("succesfulQRCreation.html",preview=preview)
    return redirect("/")