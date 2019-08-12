from flask import Flask, render_template, redirect, request, send_from_directory, make_response, jsonify, abort,redirect,url_for,make_response
import os
from werkzeug.utils import secure_filename
import aboutbeauty
import aboutborder
import abouthat
import abouthair
import aboutglass
import time
from numpy import unicode

app = Flask(__name__)

@app.route("/")
def ind():
    return redirect("/index")

@app.route("/index")
def index():
    return render_template("index.html")

global origin
origin="upload.jpg"
global prowhite
prowhite="upload1.jpg"
global problur
problur="upload2.jpg"
global prosharp
prosharp="upload4.jpg"
global procolor 
procolor="upload1.jpg"
global procon
procon="upload2.jpg"
global probri
probri="upload4.jpg"

@app.route("/process")
def process():
    global origin
    origin="upload.jpg"
    return render_template("process.html",picturepath=origin)
    
@app.route("/upload",methods=['POST'])
def upload():
    if request.method == 'POST':
        tm=time.time()
        str_tm=str(tm).replace(".","")
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # current path of the file
        print(basepath)
        upload_path = os.path.join(basepath, r'static/upload', secure_filename(str_tm+f.filename))
        f.save(upload_path)
        print(upload_path)
        global origin
        origin=str_tm+f.filename
        picpath="./static/upload/"+origin
        global prowhite
        prowhite=aboutbeauty.BeautyProcess("WhiteBeauty",picpath,"./static/upload/",origin)
        global problur
        problur=aboutbeauty.BeautyProcess("Blur",picpath,"./static/upload/",origin)
        global prosharp
        prosharp=aboutbeauty.BeautyProcess("SharpnessEnhancement",picpath,"./static/upload/",origin)
        global procolor
        procolor=aboutbeauty.BeautyProcess("ColorEnhancement",picpath,"./static/upload/",origin)
        global probri
        probri=aboutbeauty.BeautyProcess("BrightnessEnhancement",picpath,"./static/upload/",origin)
        global procon
        procon=aboutbeauty.BeautyProcess("ContrastEnhancement",picpath,"./static/upload/",origin)
    else:
        origin="upload.jpg"
    return render_template("process.html",picturepath=origin,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)

@app.route("/white")
def white():
    #picpath="./static/upload/"+origin
    #proname=aboutbeauty.BeautyProcess("WhiteBeauty",picpath,"./static/upload/",origin)
    #print(proname)
    #global prowhite
    #prowhite=proname
    # return render_template("process.html",picturepath=prowhite)
    return render_template("process.html",picturepath=prowhite,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)

@app.route('/static/upload/')
def sendwhiteimg():
    return send_from_directory("./static/upload/", prowhite)

@app.route("/blur")
def blur():
    # picpath="./static/upload/"+origin
    # proname=aboutbeauty.BeautyProcess("Blur",picpath,"./static/upload/",origin)
    # print(proname)
    # return render_template("process.html",picturepath=problur)
    return render_template("process.html",picturepath=problur,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)


@app.route('/static/upload/')
def sendblurimg():
    return send_from_directory("./static/upload/", problur)

@app.route("/sharpen")
def sharpen():
    # picpath="./static/upload/"+origin
    # proname=aboutbeauty.BeautyProcess("SharpnessEnhancement",picpath,"./static/upload/",origin)
    # print(proname)
    #return render_template("process.html",picturepath=prosharp)
    return render_template("process.html",picturepath=prosharp,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)


@app.route('/static/upload/')
def sendsharpimg():
    return send_from_directory("./static/upload/", prosharp)

@app.route("/saturation")
def saturation():
    # picpath="./static/upload/"+origin
    # proname=aboutbeauty.BeautyProcess("ColorEnhancement",picpath,"./static/upload/",origin)
    # print(proname)
    #return render_template("process.html",picturepath=procolor)
    return render_template("process.html",picturepath=procolor,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)


@app.route('/static/upload/')
def sendcolorimg():
    return send_from_directory("./static/upload/", procolor)

@app.route("/brighten")
def brighten():
    # process one by one, not together
    # picpath="./static/upload/"+origin
    # proname=aboutbeauty.BeautyProcess("BrightnessEnhancement",picpath,"./static/upload/",origin)
    # print(proname)
    #return render_template("process.html",picturepath=probri)
    return render_template("process.html",picturepath=probri,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)

@app.route('/static/upload/')
def sendbriimg():
    return send_from_directory("./static/upload/", probri)

@app.route("/contrast")
def contrast():
    # process one by one, not together
    # picpath="./static/upload/"+origin
    # proname=aboutbeauty.BeautyProcess("ContrastEnhancement",picpath,"./static/upload/",origin)
    # print(proname)
    #return render_template("process.html",picturepath=procon)
    return render_template("process.html",picturepath=procon,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)

@app.route('/static/upload/')
def sendconimg():
    return send_from_directory("./static/upload/", procon)

@app.route('/border/<filename>')
def border(filename):
    try:
        borderpath="./static/borders/border"+filename+'.png'
        picpath="./static/upload/"+origin
        savepath="./static/upload/"
        proname=aboutborder.addborder(picpath,savepath,borderpath,origin)
    except:
        proname=origin
    return render_template("process.html",picturepath=proname,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)

@app.route('/drawhat/<filename>')
def drawhat(filename):
    try:
        if filename=="0":
            picname="./static/upload/"+origin
            hatpath="./static/hats/drawhat0.png"
            savepath="./static/upload/"
            hatname="drawhat0"+filename
            degree=2
            ratew=0.15
            rateh=0.95
            proname=abouthat.adddrawhat(picname,hatpath,savepath,origin,hatname,degree,ratew,rateh)
        else:
            picname="./static/upload/"+origin
            hatpath="./static/hats/drawhat1.png"
            savepath="./static/upload/"
            hatname="drawhat"+filename
            degree=2.25
            ratew=0.315
            rateh=0.45
            proname=abouthat.adddrawhat(picname,hatpath,savepath,origin,hatname,degree,ratew,rateh)
    except:
        proname=origin
    print(proname)
    return render_template("process.html",picturepath=proname,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)

@app.route('/hat/<filename>')
def hat(filename):
    try:
        picname="./static/upload/"+origin
        hatpath="./static/hats/"
        savepath="./static/upload/"
        hatname="hat"+filename
        proname=abouthat.addChristmashat(picname,hatpath,savepath,origin,hatname)
    except:
        proname=origin
    return render_template("process.html",picturepath=proname,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)

@app.route('/hair/<filename>')
def hair(filename):
    try:
        if filename=="0":
            picpath="./static/upload/"+origin
            hatpath="./static/hair/hair0.png"
            savepath="./static/upload/"
            picname=origin
            hatname="hair"+filename
            degree=2.5
            ratew=0.315
            rateh=0.42
            proname=abouthair.addhair(picpath,hatpath,savepath,picname,hatname,degree,ratew,rateh)
        else:
            picpath="./static/upload/"+origin
            hatpath="./static/hair/hair1.png"
            savepath="./static/upload/"
            picname=origin
            hatname="hair"+filename
            degree=1
            ratew=-0.1
            rateh=1.5
            proname=abouthair.addhair(picpath,hatpath,savepath,picname,hatname,degree,ratew,rateh)
    except:
        proname=origin
    return render_template("process.html",picturepath=proname,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)

@app.route('/glass/<filename>')
def glass(filename):
    try:
        if filename=="0":
            picpath="./static/upload/"+origin
            hatpath="./static/eyes/glass0.png"
            savepath="./static/upload/"
            picname=origin
            hatname="eye"+filename+'.png'
            proname=aboutglass.addGlasses(picpath,hatpath,savepath,picname,hatname)
        else:
            picpath="./static/upload/"+origin
            hatpath="./static/eyes/glass1.png"
            savepath="./static/upload/"
            picname=origin
            hatname="eye"+filename+'.png'
            proname=aboutglass.addGlasses(picpath,hatpath,savepath,picname,hatname)
    except:
        proname=origin
    return render_template("process.html",picturepath=proname,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)

@app.route('/moustache/<filename>')
def moustache(filename):
    try:
        if filename=="0":
            picpath="./static/upload/"+origin
            bearpic="./static/moustache/m0.png"
            savepath="./static/upload/"
            picname=origin
            bearname="m"+filename+".png"
            lrdegree=8
            tbdegree=-5
            proname=aboutglass.addbbb(picpath,bearpic,savepath,picname,bearname,lrdegree,tbdegree)
        elif filename=="1":
            picpath="./static/upload/"+origin
            bearpic="./static/moustache/m1.png"
            savepath="./static/upload/"
            picname=origin
            bearname="m"+filename+".png"
            degree=1
            bratew=0.4
            brateh=1.2
            proname=aboutglass.addbear(picpath,bearpic,savepath,picname,bearname,degree,bratew,brateh)
        elif filename=="2":
            picpath="./static/upload/"+origin
            bearpic="./static/moustache/m2.png"
            savepath="./static/upload/"
            picname=origin
            bearname="m"+filename+".png"
            lrdegree=4.75
            tbdegree=4
            proname=aboutglass.addbbb(picpath,bearpic,savepath,picname,bearname,lrdegree,tbdegree)
        else:
            picpath="./static/upload/"+origin
            bearpic="./static/moustache/m3.png"
            savepath="./static/upload/"
            picname=origin
            bearname="m"+filename+".png"
            lrdegree=8
            tbdegree=30
            proname=aboutglass.addbbb(picpath,bearpic,savepath,picname,bearname,lrdegree,tbdegree)
    except:
        proname=origin
    return render_template("process.html",picturepath=proname,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)
  
@app.route("/download/<filename>",methods=['GET'])
def download(filename):
    diretory=os.getcwd()
    print(diretory)
    diretory=diretory+"/static/upload"
    response=make_response(send_from_directory(diretory,filename,as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('utf8'))
    return response

@app.route("/save/<filename>")
def save(filename):
    global origin
    origin=filename
    return render_template("process.html",picturepath=origin,prowhite=prowhite,problur=problur,probri=probri,procolor=procolor,prosharp=prosharp,procon=procon)


if __name__ == "__main__":
    app.run(host="192.168.1.208",port=5001,debug=True)
