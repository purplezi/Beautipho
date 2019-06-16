import numpy as np
import cv2
import Image

def addborder(picpath,savepath,borderpath):
    imagename=picpath[:picpath.find('.')]

    human_img = Image.open(picpath)
    human_img = human_img.convert("RGBA")

    border_img=Image.open(borderpath)
    border_img=border_img.convert("RGBA")

    picw,pich=human_img.size
    border_img=border_img.resize((picw,pich))

    human_img.paste(border_img,(0,0),mask=border_img)

    savepath=savepath+"border0"+imagename+'.png'
    human_img.show()
    human_img.save(savepath,quality=95, subsampling=0)

if __name__=="__main__":
    addborder('anne.jpg','./image/borders/','./image/borders/border0.png')
