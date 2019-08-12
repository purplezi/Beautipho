# -*- coding: utf-8 -*-
import face_recognition
import cv2
import random
from PIL import Image
import Image
import time

def getface(picpath):
    image = face_recognition.load_image_file(picpath)
    face_locations = face_recognition.face_locations(image)
    return face_locations
    print("Found {} face(s) in this photograph.".format(len(face_locations)))

def draw(face_locations,hats,human_img,degree,ratew,rateh):
    index=0
    for face_location in face_locations:
        top, right, bottom, left = face_location
        #top -= 10
        hatw,hath = hats[index].size
        #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        #degree change the hat size can be 
        #ratew change the position (left-right) of the hat
        #rateh change the position (top-bottom) of the hat
        head_w = int(degree*(right-left))
        head_h=int((head_w/hatw)*hath)
        hat_img = hats[index].resize( (head_w,head_h) )#convert size of hat
        hat_region = hat_img

        human_region = ( int(left-ratew*head_w), int(top-rateh*head_h))
        human_img.paste(hat_region, human_region,mask=hat_img)
        index=index+1

    return human_img

def addChristmashat(picpath,hatpath,savepath,picname,hatname):
    try:
        print("drawhat")
        tm=time.time()
        str_tm=str(tm).replace(".","")
        imagetype=picname[picname.find('.')+1:]
        imagename=picname[:picname.find('.')]

        face_locations = getface(picpath)

        human_img = Image.open(picpath)
        human_img = human_img.convert("RGBA")

        #no human faces
        if len(face_locations) != 0:
            hats=[]
            if len(face_locations)==0:
                path=hatpath+hatname+".png"
                im=Image.open(path)
                for i in range(0,len(face_locations)):   #having one hats
                    hats.append(im)#use append instead of hats[i]
                    hats[i] = hats[i].convert("RGBA")
            elif len(face_locations)==1:
                path=hatpath+hatname+".png" #having one hats
                hats.append(Image.open(path))#use append instead of hats[i]
                hats[0] = hats[0].convert("RGBA")
            else:
                num=hatname[hatname.find('t')+1:]
                num=int(num)
                for i in range(0,len(face_locations)):   #having n hats
                    path=hatpath+"hat"+str((num+i)%6)+".png"
                    hats.append(Image.open(path))#use append instead of hats[i]
                    hats[i] = hats[i].convert("RGBA")
            
            #degree change the hat size can be 
            #ratew change the position (left-right) of the hat
            #rateh change the position (top-bottom) of the hat
            human_img=draw(face_locations,hats,human_img,1,0,1.25)
                
            #human_img.show()
            #OSError: cannot write mode RGBA as JPEG we must save as png because jpg is RGB and png is RGBA
        
        savepath=savepath+hatname+imagename+str_tm+'1.png'
        proname=hatname+imagename+str_tm+'1.png'
        human_img.save(savepath,quality=95, subsampling=0)
    except:
        proname=picname
    return proname

def addDrawhat_0(picpath,hatpath,savepath,picname):
    try:
        imagetype=picname[picname.find('.')+1:]
        imagename=picname[:picname.find('.')]

        face_locations = getface(picpath)

        human_img = Image.open(picpath)
        human_img = human_img.convert("RGBA")

        if len(face_locations) != 0:
            hats=[]
            hat_img=Image.open(hatpath+"drawhat0.png")
            hat_img=hat_img.convert("RGBA")
            for i in range(0,len(face_locations)):
                hats.append(hat_img)#use append instead of hats[i]
            
            #degree change the hat size can be 
            #ratew change the position (left-right) of the hat
            #rateh change the position (top-bottom) of the hat
            human_img=draw(face_locations,hats,human_img,2,0.15,0.95)

            #human_img.show()
            #OSError: cannot write mode RGBA as JPEG we must save as png because jpg is RGB and png is RGBA
        savepath=savepath+"drawhat0"+imagename+str_tm+'.png'
        proname="drawhat0"+imagename+str_tm+'.png'
        human_img.save(savepath,quality=95, subsampling=0)
        return proname
    except:
        return picname

def addDrawhat_1(picpath,hatpath,savepath,picname):
    try:
        print("drawhat")
        tm=time.time()
        str_tm=str(tm).replace(".","")

        imagetype=picname[picname.find('.')+1:]
        imagename=picname[:picname.find('.')]

        face_locations = getface(picpath)

        human_img = Image.open(picpath)
        human_img = human_img.convert("RGBA")

        if len(face_locations) != 0:
            hats=[]
            hat_img=Image.open(hatpath+"drawhat1.png")
            hat_img=hat_img.convert("RGBA")
            for i in range(0,len(face_locations)):
                hats.append(hat_img)#use append instead of hats[i]
            
            #degree change the hat size can be 
            #ratew change the position (left-right) of the hat
            #rateh change the position (top-bottom) of the hat
            human_img=draw(face_locations,hats,human_img,2.25,0.315,0.45)

            #human_img.show()
            #OSError: cannot write mode RGBA as JPEG we must save as png because jpg is RGB and png is RGBA
        savepath=savepath+"drawhat1"+imagename+str_tm+'.png'
        proname="drawhat1"+imagename+str_tm+'.png'
        human_img.save(savepath,quality=95, subsampling=0)
        return proname
    except:
        return picname

def adddrawhat(picpath,hatpath,savepath,picname,hatname,degree,ratew,rateh):
    try:
        print("drawhat")
        tm=time.time()
        str_tm=str(tm).replace(".","")

        imagetype=picname[picname.find('.')+1:]
        imagename=picname[:picname.find('.')]

        face_locations = getface(picpath)

        human_img = Image.open(picpath)
        human_img = human_img.convert("RGBA")

        if len(face_locations) != 0:
            hats=[]
            hat_img=Image.open(hatpath)
            hat_img=hat_img.convert("RGBA")
            for i in range(0,len(face_locations)):
                hats.append(hat_img)#use append instead of hats[i]
            
            #degree change the hat size can be 
            #ratew change the position (left-right) of the hat
            #rateh change the position (top-bottom) of the hat
            human_img=draw(face_locations,hats,human_img,degree,ratew,rateh)

            #human_img.show()
            #OSError: cannot write mode RGBA as JPEG we must save as png because jpg is RGB and png is RGBA
        savepath=savepath+hatname+imagename+str_tm+'.png'
        proname=hatname+imagename+str_tm+'.png'
        human_img.save(savepath,quality=95, subsampling=0)
    except:
        proname=picname
    return proname

if __name__=="__main__":
    #text('zhaoliying.jpg','image/hats/hat0.png')
    #addChristmashat('5.jpg','image/hats/','image/')
    #addDrawhat_0('5.jpg','image/hats/','image/')
    #addDrawhat_1('trump.jpg','image/hats/','image/')
    proname=adddrawhat('./static/upload/anne.jpg','./static/hats/drawhat0.png','./static/upload','anne.jpg','drawhat0',2,0.15,0.95)
    print(proname)