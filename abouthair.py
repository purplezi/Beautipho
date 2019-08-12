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

def draw(face_locations,hair,human_img,degree,ratew,rateh):
    index=0
    for face_location in face_locations:
        top, right, bottom, left = face_location
        #top -= 10
        hatw,hath = hair[index].size
        #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        #degree change the hat size can be 
        #ratew change the position (left-right) of the hat
        #rateh change the position (top-bottom) of the hat
        head_w = int(degree*(right-left))
        head_h=int((head_w/hatw)*hath)
        hat_img = hair[index].resize( (head_w,head_h) )#convert size of hat
        hat_region = hat_img

        human_region = ( int(left-ratew*head_w), int(top-rateh*head_h))
        human_img.paste(hat_region, human_region,mask=hat_img)
        index=index+1

    return human_img

def addhair(picpath,hatpath,savepath,picname,hatname,degree,ratew,rateh):
    try:
        print("hair")
        tm=time.time()
        str_tm=str(tm).replace(".","")
        
        imagename=picname[:picname.find('.')]
        imagetype=picname[picname.find('.')+1:]

        face_locations = getface(picpath)

        human_img = Image.open(picpath)
        human_img = human_img.convert("RGBA")

        if len(face_locations) != 0:
            hair=[]
            hat_img=Image.open(hatpath)
            hat_img=hat_img.convert("RGBA")
            for i in range(0,len(face_locations)):
                hair.append(hat_img)#use append instead of hats[i]
            
            #degree change the hat size can be 
            #ratew change the position (left-right) of the hat 增大 左移
            #rateh change the position (top-bottom) of the hat 增大 上移
            human_img=draw(face_locations,hair,human_img,degree,ratew,rateh)

            #human_img.show()
            #OSError: cannot write mode RGBA as JPEG we must save as png because jpg is RGB and png is RGBA
        savepath=savepath+hatname+imagename+str_tm+'.png'
        proname=hatname+imagename+str_tm+'.png'
        print(proname)
        human_img.save(savepath,quality=95, subsampling=0)
    except:
        proname=picname
    return proname


if __name__=="__main__":
    proname=addhair('./static/upload/obama.jpg','./static/hair/hair1.png','./static/upload/','obama.jpg','hair1',1,-0.1,1.5)
    print(proname)