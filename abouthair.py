# -*- coding: utf-8 -*-
import face_recognition
import cv2
import random
from PIL import Image
import Image

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

def addhair(picpath,hatpath,savepath):
    imagetype=picpath[picpath.find('.')+1:]
    imagename=picpath[:picpath.find('.')]

    face_locations = getface(picpath)

    human_img = Image.open(picpath)
    human_img = human_img.convert("RGBA")

    if len(face_locations) != 0:
        hair=[]
        hat_img=Image.open(hatpath+"hair0.png")
        hat_img=hat_img.convert("RGBA")
        for i in range(0,len(face_locations)):
            hair.append(hat_img)#use append instead of hats[i]
        
        #degree change the hat size can be 
        #ratew change the position (left-right) of the hat
        #rateh change the position (top-bottom) of the hat
        human_img=draw(face_locations,hair,human_img,2.5,0.315,0.42)

        human_img.show()
        #OSError: cannot write mode RGBA as JPEG we must save as png because jpg is RGB and png is RGBA
    savepath=savepath+"hair0"+imagename+'.png'
    human_img.save(savepath,quality=95, subsampling=0)

if __name__=="__main__":
    addhair('5.jpg','image/hair/','image/')