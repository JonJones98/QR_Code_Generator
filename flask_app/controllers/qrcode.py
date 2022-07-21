
import shutil
from turtle import delay
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
import requests
import time


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
    session['name']=request.form["filename"]
    session['formattype']=request.form["formattype"]
    qr_url=str(session['url'])
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
    session.clear
    return redirect("/qrcodecreation")

#@app.route("/qrcodedownload1")
#def download1():
    img =qrcode.make(str(session['url'])) 
    type(img)
    path_to_download_folder = (os.path.join(Path.home(), "Downloads",session['file name']))
    img.save(path_to_download_folder )
    session.clear()
    print("Download Complete")
    print(session)
    return render_template("succesfulQRCreation.html")

