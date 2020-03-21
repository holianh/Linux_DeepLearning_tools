import os

os.system("pip install imutils")
os.system("pip install bokeh")
os.system("pip install itkwidgets")
#!conda install nodejs -y
os.system("jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib jupyterlab-datawidgets itkwidgets")

from os.path import exists, join, basename,dirname

def GetList(pData,ext='.jpg'):
    fis=[]
    for D,_,F in os.walk(pData):
        for fn in F:
            if fn.endswith(ext):
                fis.append(join(D,fn))
    return fis
# fis=GetList('D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs/VID-20200315-WA0003_gt/')

def getbox(fn):
    fn=fn.replace('.jpg','.txt')
    with open(fn)as ff:dat=ff.read().strip().split()
    return int(dat[0]), [float(x) for x in dat[1:]]
# getbox('D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs/VID-20200315-WA0006_gt/VID-20200315-WA0006_gt_0000001.jpg')

def from_yolo_to_cor(box, shape):
    img_h, img_w, _ = shape
    # x1, y1 = ((x + witdth)/2)*img_width, ((y + height)/2)*img_height
    # x2, y2 = ((x - witdth)/2)*img_width, ((y - height)/2)*img_height
    x1, y1 = int((box[0] + box[2]/2)*img_w), int((box[1] + box[3]/2)*img_h)
    x2, y2 = int((box[0] - box[2]/2)*img_w), int((box[1] - box[3]/2)*img_h)
    return x1, y1, x2, y2
    
def draw_boxes(img, boxes,shape,ret_save2file):
    for box in boxes:
        x1, y1, x2, y2 = from_yolo_to_cor(box, shape)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 3)
    if ret_save2file:
        return img
    plt.imshow(img)
    plt.show()

import cv2
import matplotlib.pyplot as plt
from random import shuffle
# shuffle(fis)

 
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
# construct the argument parse and parse the arguments
def get_img_shapehw(fnimg):
    img = cv2.imread(fnimg,0)
    height, width = img.shape[:2]
    return height, width

def checkLabeledFolder(pFolder='D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs/VID-20200315-WA0003_gt/',
                      videoOutp='output.avi'):
    fis=GetList(pFolder)
    fis.sort()
    h,w=get_img_shapehw(fis[0])

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(videoOutp,fourcc, 20.0, (w,h)) #(640,480))

    for fn in fis:
        Class,box=getbox(fn)
    #     print(box)
        img=cv2.imread(fn)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=draw_boxes(img,[box],img.shape,ret_save2file=True)
        out.write(img[...,::-1])
    out.release()
    print('done')
    
# pFolder='D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs/VID-20200315-WA0004_gt/'
# checkLabeledFolder(pFolder)

###############################################################################################################
###############################################################################################################
from bokeh.plotting import figure
from bokeh.io import output_notebook, show, push_notebook
import cv2
import time
output_notebook()
def displayVideo(vidPath='output.avi',Tsleep=0.3):
    cap = cv2.VideoCapture(vidPath)
    ret, frame = cap.read()
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) # because Bokeh expects a RGBA image
    frame=cv2.flip(frame, -1) # because Bokeh flips vertically
    width=frame.shape[1]
    height=frame.shape[0]
    p = figure(x_range=(0,width), y_range=(0,height), output_backend="webgl", width=width, height=height)
    myImage = p.image_rgba(image=[frame], x=0, y=0, dw=width, dh=height)
    show(p, notebook_handle=True)
    while ret:
        frame = cv2.resize(frame, (frame.shape[0]//3,frame.shape[1]//3), interpolation = cv2.INTER_AREA)
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        frame=cv2.flip(frame, -1)
        myImage.data_source.data['image']=[frame]
        push_notebook()
        ret, frame = cap.read()
        time.sleep(Tsleep)
#displayVideo()

###############################################################################################################
###############################################################################################################
# Convert video+DarkLabel to YoLo label 
###############################################################################################################
###############################################################################################################

import cv2
import os
from os.path import exists, join, basename,dirname
def GetList(pData,ext='.jpg'):
    fis=[]
    for D,_,F in os.walk(pData):
        for fn in F:
            if fn.endswith(ext):
                fis.append(join(D,fn))
    return fis
# fis=GetList('D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs/VID-20200315-WA0003_gt/')

def Chk(x,y,Vl):
    if x<0:x=0
    if y<0:y=0
    return min(x,Vl),min(y,Vl)

def is_number(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return s

def get_img_shape(fnimg):
    if not exists(fnimg):
        print('File not exists:',fnimg)
    img = cv2.imread(fnimg,0)
    height, width = img.shape[:2]
    return height, width

def convert_labels(sizehw, x1, y1, x2, y2):
    """
    Definition: Parses label files to extract label and bounding box
        coordinates.  Converts (x1, y1, x1, y2) KITTI format to
        (x, y, width, height) normalized YOLO format.
    """
    def sorting(l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin
#     size = get_img_shape(path)
    xmax, xmin = sorting(x1, x2)
    ymax, ymin = sorting(y1, y2)
    dw = 1./sizehw[1]
    dh = 1./sizehw[0]
    x = (xmin + xmax)/2.0
    y = (ymin + ymax)/2.0
    w = xmax - xmin
    h = ymax - ymin
    x = round(x*dw,6)
    w = round(w*dw,6)
    y = round(y*dh,6)
    h = round(h*dh,6)
    return (x,y,w,h)

import cv2
def ExtractVideo(pImgsDirOut  ='D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs',
                 video_path   ='D:/tact/2020/eKYC_nhan_dang_van_tay/Dataset/Anh_Da_Den/VID-20200315-WA0003.mp4'
                 ):
    vidcap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    count = 0
    if pImgsDirOut[-1]!='/':pImgsDirOut+='/'
    if not exists(pImgsDirOut):
        os.makedirs(pImgsDirOut)
    vidName= basename(video_path)         
    fnID=vidName.split('.')[0]+'_gt'
    if not exists(pImgsDirOut+fnID):
        os.makedirs(pImgsDirOut+fnID)
    print('Begin convert video2imgs:',video_path)
    while success:
        fnimg= (pImgsDirOut+fnID+'/'+ fnID+'_{:07d}.jpg'.format(count))
        cv2.imwrite(fnimg, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1
    print('Done  convert video2imgs, save to:',fnimg)
    
def ConvertLabel_from_Frame_n_x1y1x2y2lbl__to_YOLO_format(
    pImgsDirOut  ='D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs',
    video_path   ='D:/tact/2020/eKYC_nhan_dang_van_tay/Dataset/Anh_Da_Den/VID-20200315-WA0003.mp4',
    DarkLabel_txt='D:/tact/2020/eKYC_nhan_dang_van_tay/Dataset/Anh_Da_Den/VID-20200315-WA0003_gt.txt',
    LBLs={'F':0} # Label in txt
    ):

    if not exists(video_path):
        print("Not Exists video:",video_path)
        return
    if not exists(DarkLabel_txt):
        print("Not Exists Labels gt:",DarkLabel_txt)
        return
    
    if pImgsDirOut[-1]!='/':pImgsDirOut+='/'
    lblName= basename(video_path)         
    fnID=lblName.split('.')[0]+'_gt'
    fnimg= (pImgsDirOut+fnID+'/'+ fnID+'_{:07d}.jpg'.format(1))
    print('chk exists:',exists(fnimg),fnimg)
    # ---------------- Extract video --------------------------
    if not exists(fnimg):
        ExtractVideo(pImgsDirOut,video_path)
    # ----------------------------------------------------------
    
    # print(exists(fnimg))

     # dict of obj names
    #
    #   o---------0  =>y1
    #   |         |
    #   |         |   
    #   |         |
    #   o---------0  >y2
    #   |
    #   v
    #   x1       
    # x: width
    # y: height


    height, width=get_img_shape(fnimg)
    sizehw=[height, width]
    cnt=0
    if not exists(DarkLabel_txt):
        print('File Not Exists:',DarkLabel_txt)
        return
    with open(DarkLabel_txt) as ff:
        lines=ff.readlines()
        for line in lines:
            line1=line.strip().split(',')

            Frame_boxs = [is_number(x) for x in line1]
    #         print(Frame_boxs)
            nFrame=Frame_boxs[0]
            nBox=Frame_boxs[1]
            Frame_boxs=Frame_boxs[2:]


            lblName= (pImgsDirOut+fnID+'/'+ fnID+'_{:07d}.txt'.format(nFrame))
    #         print(lblName)
            with open(lblName,'w') as fw:
                for k in range(nBox):
                    x1,y1,x2,y2,lbl=Frame_boxs[5*k:5*(k+1)]
                    x1,x2=Chk(x1,x2,width)
                    y1,y2=Chk(y1,y2,height)
                    (x,y,w,h)=convert_labels(sizehw, x1, y1, x2, y2)
    #                 print(LBLs[lbl],x,y,w,h)
                    fw.write("{} {} {} {} {}\n".format(LBLs[lbl],x,y,w,h))
    print('Finished:',lblName)            

# =============== CHANGE HERE: ===============================================================
pImgsDirOut = 'D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs'
pVidFolader = 'D:/tact/2020/eKYC_nhan_dang_van_tay/Dataset/Anh_Da_Den/'
vid_ext     = '.mp4'
LBLs={'F':0}
# =============== CHANGE HERE: ===============================================================
def Folder_ConvertLabel_from_Frame_n_x1y1x2y2lbl__to_YOLO_format(
    pImgsDirOut = 'D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs',
    pVidFolader = 'D:/tact/2020/eKYC_nhan_dang_van_tay/Dataset/Anh_Da_Den/',
    vid_ext     = '.mp4',
    LBLs={'F':0}):
    # Get video src list:
    fis=GetList(pVidFolader,vid_ext)
    print('len(fis)=',len(fis))
    for k, vidfn in enumerate(fis):
        print("Process:{}/{} =========================".format(k,len(fis)))
        ConvertLabel_from_Frame_n_x1y1x2y2lbl__to_YOLO_format( 
            pImgsDirOut  =pImgsDirOut,
            video_path   =vidfn,
            DarkLabel_txt=vidfn.replace(vid_ext,'_gt.txt'),
            LBLs=LBLs # Label in txt
            )
    print('Done')

# =========CONVERT DARKLABEL TO YOLO:====== CHANGE HERE: =====================================
pImgsDirOut = 'Video_DBs/'
pVidFolader = '/content/drive/My Drive/AiSolutions/Project_eKYC_Finger_Print_Recognition/Data_Training/Video_ChuanHoa/'
vid_ext     = '.avi'
LBLs={'F':0,0:0,'null':0}
# =============== CHANGE HERE: ===============================================================
Folder_ConvertLabel_from_Frame_n_x1y1x2y2lbl__to_YOLO_format(
    pImgsDirOut = pImgsDirOut,
    pVidFolader = pVidFolader,
    vid_ext     = vid_ext,
    LBLs=LBLs)


sss="""
#Check video label OK or not: Save to Video ==================================================
pFolder='D:/tact/2020/eKYC_nhan_dang_van_tay/Code/Video_DBs/VID-20200315-WA0004_gt/'
checkLabeledFolder(pFolder='/content/Video_DBs/HieuNQ_09_gt', videoOutp='output.avi')
#displayVideo() #local only, colab cant run

# =========CONVERT DARKLABEL TO YOLO:====== CHANGE HERE: =====================================
pImgsDirOut = 'Video_DBs/'
pVidFolader = '/content/drive/My Drive/AiSolutions/Project_eKYC_Finger_Print_Recognition/Data_Training/Video_ChuanHoa/'
vid_ext     = '.avi'
LBLs={'F':0,0:0,'null':0}
# =============== CHANGE HERE: ===============================================================
Folder_ConvertLabel_from_Frame_n_x1y1x2y2lbl__to_YOLO_format(
    pImgsDirOut = pImgsDirOut,
    pVidFolader = pVidFolader,
    vid_ext     = vid_ext,
    LBLs=LBLs)
  
#Display Image+Box:==========================================================================
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
import os,glob

def TAimread(fis,i, withLabel=True):
    fn=fis[int(i*nF/NFrames)]
    img=cv2.imread(fn)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if withLabel:
        Class,box=getbox(fn)
        img=draw_boxes(img,[box],img.shape,ret_save2file=True)
    return img
####### CHANGE THIS: #################################
pImageFolder='/content/Video_DBs/Long_00_gt' 
NFrames=10   # Number of Images to display
img_ext='.jpg'
######################################################

fis=glob.glob(pImageFolder+'/*'+img_ext)
fis.sort()
nF=len(fis)

x_values = np.linspace(0, nF, NFrames)
plt.figure(figsize=(12,8))
fig, ax = plt.subplots()
plt.close()
img=TAimread(fis,0)
im = ax.imshow(img) #, animated=True)
def animate(i):
    img=TAimread(fis,i)
    im.set_array(img)
    return (line2,im,)

anim = animation.FuncAnimation(fig, animate, init_func=None,frames=NFrames, interval=100, blit=True)
# Note: below is the part which makes it work on Colab
rc('animation', html='jshtml')
anim
"""
print(sss)



