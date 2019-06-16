# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageEnhance
import cv2
import numpy as np


#亮度增强：brightness在（0-1）之间，新图像较原图暗，在（1-~）新图像较原图亮 ,
def BrightnessEnhancement(brightness,filepath,savepath):
    image = Image.open(filepath)
    enh_bri = ImageEnhance.Brightness(image)
    image_brightened = enh_bri.enhance(brightness)
    image_brightened.show()
    filename=filepath[:filepath.find(".")]
    savepath = savepath + "brighten"+ filename + ".png"
    image_brightened.save(savepath)

#对比度增强 亮的更亮，暗的更暗
def ContrastEnhancement(contrast,filepath,savepath):
    image = Image.open(filepath)
    enh_con = ImageEnhance.Contrast(image)
    image_contrasted = enh_con.enhance(contrast)
    image_contrasted.show()
    filename=filepath[:filepath.find(".")]
    savepath = savepath + "contrast"+ filename + ".png"
    image_contrasted.save(savepath)

#色度增强 : 饱和度  color=1,保持原图像不变
def ColorEnhancement(color,filepath,savepath):
    image = Image.open(filepath)
    enh_col = ImageEnhance.Color(image)
    image_colored = enh_col.enhance(color)
    image_colored.show()
    filename=filepath[:filepath.find(".")]
    savepath = savepath + "color"+ filename + ".png"
    image_colored.save(savepath)

#锐度增强: 清晰度  sharpness=1,保持原图像不变
def SharpnessEnhancement(sharpness,filepath,savepath):
    image = Image.open(filepath)
    enh_sha = ImageEnhance.Sharpness(image)
    #sharpness = 2
    image_sharped = enh_sha.enhance(sharpness)
    image_sharped.show()
    filename=filepath[:filepath.find(".")]
    savepath = savepath + "sharpen"+ filename + ".png"
    image_sharped.save(savepath)

#磨皮
#色彩窗的半径
#图像将呈现类似于磨皮的效果
#image：输入图像，可以是Mat类型，图像必须是8位或浮点型单通道、三通道的图像
#0：表示在过滤过程中每个像素邻域的直径范围，一般为0
#后面两个数字：空间高斯函数标准差，灰度值相似性标准差
def Blur(filepath,savepath):
    image =cv2.imread(filepath)
    #双边滤波  src:original image d:像素邻域的直径范围 sigmaColor:颜色空间的标准方差，一般尽可能大 sigmaSpace:坐标空间的标准方差(像素单位)，一般尽可能小
    Remove=cv2.bilateralFilter(image,9,75,75)
    cv2.imshow('filter',Remove)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    filename=filepath[:filepath.find(".")]
    savepath = savepath + "blur"+ filename + ".png"
    cv2.imwrite(savepath,Remove)

#美白
def WhiteBeauty(whi,filepath,savepath):
    image =cv2.imread(filepath)
    white = np.uint8(np.clip((whi * image + 10), 0, 255))
    cv2.imshow('bai',white)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    filename=filepath[:filepath.find(".")]
    savepath=savepath+"whitebeauty"+filename+ ".png"
    cv2.imwrite(savepath,white)

def BeautyProcess(processname,picpath,savepath):
    if processname == "WhiteBeauty":
        whitedegree=1.25
        WhiteBeauty(whitedegree,picpath,savepath)
    elif processname =="Blur":
        Blur(picpath,savepath)
    elif processname =="SharpnessEnhancement":
        sharpendegree=3
        SharpnessEnhancement(sharpendegree,picpath,savepath)
    elif processname == "ColorEnhancement":
        colordegree=2
        ColorEnhancement(colordegree,picpath,savepath)
    elif processname =="ContrastEnhancement":
        contrastdegree=2
        ContrastEnhancement(contrastdegree,picpath,savepath)
    elif processname=="BrightnessEnhancement":
        brightendegree=2
        BrightnessEnhancement(brightendegree,picpath,savepath)
    else:
        return 0

if __name__ =="__main__":
    #BeautyProcess("WhiteBeauty","linzhi.jpg","./static/aboutbeauty/whitebeauty/")
    BeautyProcess("Blur","linzhi.png","./static/aboutbeauty/blur/")
    #BeautyProcess("SharpnessEnhancement","1.jpg","./static/aboutbeauty/sharpen/")
    #BeautyProcess("ColorEnhancement","1.jpg","./static/aboutbeauty/color/")
    #BeautyProcess("ContrastEnhancement","1.jpg","./static/aboutbeauty/contrast/")
    #BeautyProcess("BrightnessEnhancement","1.jpg","./static/aboutbeauty/brighten/")



