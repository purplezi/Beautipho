import dlib
import numpy as np
from PIL import Image
from imutils import face_utils
import cv2
import face_recognition

def addGlasses(humanpic,glasspic,savepath):
    detector=dlib.get_frontal_face_detector()
    predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    img=Image.open(humanpic).convert('RGBA')
    glass=Image.open(glasspic).convert('RGBA')
    #为了dlib人脸识别，需要灰度
    img_gray=np.array(img.convert('L'))

    recs=detector(img_gray,0)

    if len(recs) == 0:
        print("No face found, exiting.")
        return -1
    print("%i faces found in source image"%len(recs))

    faces=[]
    for rect in recs:
        face={}
        shades_width=rect.right()-rect.left()
        #预测器用于检测当前人脸所在的位置的方位
        shape=predictor(img_gray,rect)
        shape=face_utils.shape_to_np(shape)
        #从输入的图像抓取每个眼睛的轮廓
        leftEye=shape[36:42]
        rightEye=shape[42:48]
        #计算每个眼睛的质量中心
        leftEyeCenter=leftEye.mean(axis=0).astype("int")
        rightEyeCenter=rightEye.mean(axis=0).astype("int")
        #计算眼睛质心之间的角度
        dY=leftEyeCenter[1]-rightEyeCenter[1]
        dX=leftEyeCenter[0]-rightEyeCenter[0]
        angle=np.rad2deg(np.arctan2(dY,dX))
        #调整眼镜大小以适应脸部宽度
        current_deal=glass.resize((shades_width,int(shades_width*glass.size[1]/glass.size[0])),resample=Image.LANCZOS)
        #旋转和翻转以适应眼镜中心
        current_deal=current_deal.rotate(angle,expand=True)
        current_deal=current_deal.transpose(Image.FLIP_TOP_BOTTOM)
        face['glasses_image']=current_deal
        lrdegree=4.75
        tbdegree=4
        left_eye_x=leftEye[0,0]-int(shades_width/lrdegree)
        left_eye_y=leftEye[0,1]-int(shades_width/tbdegree)
        face['final_pos']=(left_eye_x,left_eye_y)
        faces.append(face)
    
    for face in faces:
        current_x=int(face['final_pos'][0])
        current_y=int(face['final_pos'][1])
        img.paste(face['glasses_image'],(current_x,current_y),face['glasses_image'])
        
    img.show()
    imagename=humanpic[:humanpic.find('.')]
    savepath=savepath+"glass0"+imagename+'.png'
    img.save(savepath,quality=95, subsampling=0)

def addGlasses2(humanpic,glasspic,savepath):
    #First we need to load the required XML classifiers. Then load our input image (or video) in grayscale mode
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

    glass=cv2.open(glasspic).convert('RGBA')

    img=cv2.imread(humanpic)
    #灰度转换
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #image要检测的输入图像 objects检测到的目标序列 scaleFactor图像尺寸减小的比例 
    #minNeighbors 表示每一个目标至少要被检测到n次才算是真的目标 minSize目标的最小尺寸 maxSize目标的最大尺寸
    faces = face_cascade.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(50,50),(100,100))  
    #eyes=eye_cascade.detectMultiScale(gray,)
    
    if len(faces) == 0:
        print("No eyes")
    #Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h). Once we get these locations, we can create a ROI （感兴趣的区域）for the face and apply eye detection on this ROI (since eyes are always on the face !!! ).
    for (x,y,w,h) in faces:
        roi_gray=gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

def getface(picpath):
    image = face_recognition.load_image_file(picpath)
    face_locations = face_recognition.face_locations(image)
    return face_locations
    print("Found {} face(s) in this photograph.".format(len(face_locations)))

def draw(face_locations,glass,bear,human_img,degree,gratew,grateh,bratew,brateh):
    index=0
    for face_location in face_locations:
        top, right, bottom, left = face_location
        #top -= 10
        hatw,hath = glass[index].size
        bearw,bearh=bear[index].size
        #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        #degree change the hat size can be 
        #ratew change the position (left-right) of the hat
        #rateh change the position (top-bottom) of the hat
        head_w = int(degree*(right-left))
        head_h=int((head_w/hatw)*hath)
        glass_img = glass[index].resize( (head_w,head_h) )#convert size of hat
        glass_region = glass_img
        
        bear_w = int(degree*(right-left))
        bear_h=int((bear_w/bearw)*bearh)
        bear_img = bear[index].resize( (bear_w,bear_h) )#convert size of hat
        bear_region = bear_img

        human_region = ( int(left-gratew*head_w), int(top-grateh*head_h))
        human_img.paste(glass_region, human_region,mask=glass_img)

        human_region = ( int(left-bratew*head_w), int(top+brateh*head_h))
        human_img.paste(bear_region, human_region,mask=bear_region)

        index=index+1

    return human_img

def addGlassesBear(humanpic,glasspic,bearpic,savepath):
    imagetype=humanpic[humanpic.find('.')+1:]
    imagename=humanpic[:humanpic.find('.')]

    face_locations = getface(humanpic)

    human_img = Image.open(humanpic)
    human_img = human_img.convert("RGBA")

    if len(face_locations) != 0:
        glass=[]
        bear=[]
        glass_img=Image.open(glasspic+"glass0.png")
        glass_img=glass_img.convert("RGBA")
        bear_img=Image.open(bearpic+"m0.png")
        bear_img=bear_img.convert("RGBA")
        for i in range(0,len(face_locations)):
            bear.append(bear_img)
            glass.append(glass_img)#use append instead of hats[i]
        
        #degree change the glass&bear size can be 
        #ratew change the position (left-right) of the glass 减小会右移
        #rateh change the position (top-bottom) of the glass 增大会上移
        #ratew change the position (left-right) of the bear 减小会右移
        #rateh change the position (top-bottom) of the bear 增大会下移
        human_img=draw(face_locations,glass,bear,human_img,1,0.015,0.05,0.015,1.25)

        human_img.show()
        #OSError: cannot write mode RGBA as JPEG we must save as png because jpg is RGB and png is RGBA
    savepath=savepath+"glassbear"+imagename+'.png'
    human_img.save(savepath,quality=95, subsampling=0)


if __name__=="__main__":
    addGlasses('anne.jpg','./image/eyes/glass0.png','./image')
    #addGlasses2('1.jpg','./image/eyes/glass0.png','./image')
    addGlassesBear('5.jpg','./image/eyes/','./image/moustache/','./image')