from pylab import *
def TA_Imshow_imgs(imgs,figsize=(18,10),bgrImg=True,cmap=None, Title=None):
    """    
        Hàm hiển thị list các ảnh, số lượng ảnh in 1 lần là không giới hạn, 
        chỉ cần đặt nó vào 1 list: imgs
    """   
    figure(figsize=figsize)
    nImgs=len(imgs)    
    h,c,k=1,3,1
    if c<nImgs:h=nImgs//c+1
    else:      c=nImgs        
    if Title: Title=Title.split(',')
    for i,im1 in enumerate(imgs):
        subplot(h,c,k);k+=1 #xticks([]), yticks([])        
        if bgrImg:
            imshow(im1[...,::-1],cmap=cmap)     
        else:
            imshow(im1,cmap=cmap)
        if Title and i<len(Title): title(Title[i])
    show()



import cv2
#bgr = cv2.imread(imgFn)
#bgr=bgr[500:1800,1000:2200,:]

def enh_CLAHE(bgr,tileGridSize=(8,8)):
    # https://stackoverflow.com/questions/25008458/how-to-apply-clahe-on-rgb-color-images
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=tileGridSize)
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv2.merge(lab_planes)
    bgr1 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    return bgr1

# img = cv2.imread(imgFn,0)
def TA_equalizeHist(img):
    if len(img.shape)==3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    return img

def build_filters():
    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 16):
        kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
        kern /= 1.5*kern.sum()
        filters.append(kern)
    return filters
 
def Gabor(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
    return accum

def TA_Binary(img):
    if len(img.shape)==3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY,11,2)
    # th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    return th2




sss="""
#================TA_Imshow_imgs============================================================
import cv2
from IPython.display import clear_output
!wget -O test.jpg "https://img2.thuthuatphanmem.vn/uploads/2019/01/04/hinh-anh-hot-girl-dep_025104603.jpg"
clear_output()
fn="test.jpg"
img1 = cv2.imread(fn)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
TA_Imshow_imgs([img1,img2],Title="Anh goc, Anh da muc xam",figsize=(10,5))
#================enh_CLAHE============================================================
bgr1=enh_CLAHE(bgr)
TA_Imshow_imgs([bgr,bgr1])
#================TA_equalizeHist============================================================
equHis=TA_equalizeHist(bgr1)
TA_Imshow_imgs([bgr1,equHis[...,::-1]],bgrImg=True,cmap='gray')

res_His=  TA_equalizeHist(res)
filters = build_filters()
res_gabor    = Gabor(res, filters)
equHis_Gabor = Gabor(res_His, filters)
TA_Imshow_imgs([res,res_His],bgrImg=True,cmap='gray') 
TA_Imshow_imgs([res,res_gabor,equHis_Gabor],bgrImg=True,cmap='gray',figsize=(18,12)) 
#================TA_Binary============================================================
res_bin=TA_Binary(res)
TA_Imshow_imgs( [res ,res_bin],bgrImg=True,cmap='gray',figsize=(12,8),Title="res ,res_bin")

"""
print(sss)
