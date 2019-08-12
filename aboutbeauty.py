# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageEnhance
import cv2
import numpy as np
import time


#亮度增强：brightness在（0-1）之间，新图像较原图暗，在（1-~）新图像较原图亮 ,
def BrightnessEnhancement(brightness,filepath,savepath,picname):
    try:
        print("brighten")
        tm=time.time()
        str_tm=str(tm).replace(".","")
        image = Image.open(filepath)
        enh_bri = ImageEnhance.Brightness(image)
        image_brightened = enh_bri.enhance(brightness)
        #image_brightened.show()
        picname=picname[:picname.find(".")]
        savepath = savepath + "brighten"+ picname+str_tm + ".png"
        proname="brighten"+ picname+str_tm + ".png"
        image_brightened.save(savepath)
        return proname
    except:
        return picname

#对比度增强 亮的更亮，暗的更暗
def ContrastEnhancement(contrast,filepath,savepath,picname):
    try:
        print("contrast")
        tm=time.time()
        str_tm=str(tm).replace(".","")
        image = Image.open(filepath)
        enh_con = ImageEnhance.Contrast(image)
        image_contrasted = enh_con.enhance(contrast)
        #image_contrasted.show()
        picname=picname[:picname.find(".")]
        savepath = savepath + "contrast"+ picname + str_tm+".png"
        proname="contrast"+ picname +str_tm+ ".png"
        image_contrasted.save(savepath)
        return proname
    except:
        return picname

#色度增强 : 饱和度  color=1,保持原图像不变
def ColorEnhancement(color,filepath,savepath,picname):
    try:
        print("color")
        tm=time.time()
        str_tm=str(tm).replace(".","")
        image = Image.open(filepath)
        enh_col = ImageEnhance.Color(image)
        image_colored = enh_col.enhance(color)
        #image_colored.show()
        picname=picname[:picname.find(".")]
        savepath = savepath + "color"+ picname +str_tm+ ".png"
        proname="color"+ picname + str_tm+".png"
        image_colored.save(savepath)
        return proname
    except:
        return picname

#锐度增强: 清晰度  sharpness=1,保持原图像不变
def SharpnessEnhancement(sharpness,filepath,savepath,picname):
    try:
        print("sharpen")
        tm=time.time()
        str_tm=str(tm).replace(".","")
        image = Image.open(filepath)
        enh_sha = ImageEnhance.Sharpness(image)
        #sharpness = 2
        image_sharped = enh_sha.enhance(sharpness)
        #image_sharped.show()
        picname=picname[:picname.find(".")]
        savepath = savepath + "sharpen"+ picname+str_tm + ".png"
        proname="sharpen"+ picname+str_tm + ".png"
        image_sharped.save(savepath)
        return proname
    except:
        return picname

#磨皮
#色彩窗的半径
#图像将呈现类似于磨皮的效果
#image：输入图像，可以是Mat类型，图像必须是8位或浮点型单通道、三通道的图像
#0：表示在过滤过程中每个像素邻域的直径范围，一般为0
#后面两个数字：空间高斯函数标准差，灰度值相似性标准差
def Blur(filepath,savepath,picname):
    try:
        print("blur")
        tm=time.time()
        str_tm=str(tm).replace(".","")
        image =cv2.imread(filepath)
        #双边滤波  src:original image d:像素邻域的直径范围 
        #sigmaColor:颜色空间的标准方差，一般尽可能大 
        # sigmaSpace:坐标空间的标准方差(像素单位)，一般尽可能小
        Remove=cv2.bilateralFilter(image,9,75,75)
        picname=picname[:picname.find(".")]
        savepath = savepath + "blur"+ picname+str_tm + ".png"
        proname="blur"+picname+ str_tm + ".png"
        cv2.imwrite(savepath,Remove)
        return proname
    except:
        return picname

#美白
def WhiteBeauty(whi,filepath,savepath,picname):
    try:
        tm=time.time()
        str_tm=str(tm).replace(".","")
        print("white")
        image =cv2.imread(filepath)
        white = np.uint8(np.clip((whi * image + 10), 0, 255))
        picname=picname[:picname.find(".")]
        savepath=savepath+"whitebeauty"+picname+str_tm+ ".png"
        proname="whitebeauty"+picname+ str_tm + ".png"
        print(picname)
        cv2.imwrite(savepath,white)
        print(proname)
        return proname
    except:
        proname=picname
        return proname

def BeautyProcess(processname,picpath,savepath,picname):
    try:
        if processname == "WhiteBeauty":
            whitedegree=1.25
            proname=WhiteBeauty(whitedegree,picpath,savepath,picname)
        elif processname =="Blur":
            proname=Blur(picpath,savepath,picname)
        elif processname =="SharpnessEnhancement":
            sharpendegree=4
            proname=SharpnessEnhancement(sharpendegree,picpath,savepath,picname)
        elif processname == "ColorEnhancement":
            colordegree=2
            proname=ColorEnhancement(colordegree,picpath,savepath,picname)
        elif processname =="ContrastEnhancement":
            contrastdegree=3
            proname=ContrastEnhancement(contrastdegree,picpath,savepath,picname)
        elif processname=="BrightnessEnhancement":
            brightendegree=2
            proname=BrightnessEnhancement(brightendegree,picpath,savepath,picname)
        else:
            return picname
        return proname
    except:
        return picname

if __name__ =="__main__":
    #BeautyProcess("WhiteBeauty","linzhi.jpg","./static/aboutbeauty/whitebeauty/")
    BeautyProcess("Blur","linzhi.png","./static/aboutbeauty/blur/")
    #BeautyProcess("SharpnessEnhancement","1.jpg","./static/aboutbeauty/sharpen/")
    #BeautyProcess("ColorEnhancement","1.jpg","./static/aboutbeauty/color/")
    #BeautyProcess("ContrastEnhancement","1.jpg","./static/aboutbeauty/contrast/")
    #BeautyProcess("BrightnessEnhancement","1.jpg","./static/aboutbeauty/brighten/")



