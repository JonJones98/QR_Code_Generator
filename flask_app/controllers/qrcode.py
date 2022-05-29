
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
    session['filename']=request.form["filename"]
    session['formattype']=request.form["formattype"]
    qr_url=str(session['url'])
    qr_name=str(session["filename"])
    qr_format=str(session["formattype"])
    session['file name']= "%s%s"%(qr_name,qr_format)
    
    return render_template("index.html")
@app.route("/qrcodedow")
def loading():
    T1=time.sleep(20)
    return render_template("index.html",T1)

@app.route("/qrcodedownload")
def download():
    img =qrcode.make(str(session['url'])) 
    type(img)
    path_to_download_folder = (os.path.join(Path.home(), "Downloads",session['file name']))
    img.save(path_to_download_folder )
    session.clear()
    print("Download Complete")
    print(session)
    return render_template("succesfulQRCreation.html")
