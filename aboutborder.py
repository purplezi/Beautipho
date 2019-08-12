import numpy as np
import cv2
import Image
import time

def addborder(filepath,savepath,borderpath,picname):
    try:
        print(borderpath)
        print("border")
        tm=time.time()
        str_tm=str(tm).replace(".","")

        imagename=picname[:picname.find('.')]

        human_img = Image.open(filepath)
        human_img = human_img.convert("RGBA")

        border_img=Image.open(borderpath)
        border_img=border_img.convert("RGBA")

        picw,pich=human_img.size
        border_img=border_img.resize((picw,pich))

        human_img.paste(border_img,(0,0),mask=border_img)

        savepath=savepath+"border0"+imagename+str_tm+'.png'
        propath="border0"+imagename+str_tm+'.png'
        #human_img.show()
        human_img.save(savepath,quality=95, subsampling=0)
        return propath
    except:
        return picname
    

if __name__=="__main__":
    addborder('anne.jpg','./image/borders/','./image/borders/border0.png')
