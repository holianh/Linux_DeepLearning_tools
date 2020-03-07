# Plot multiple images, In một lần, 1 list ảnh, chạy trong Colab 

```python
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

#Use:----------------------------------------------
import cv2
from IPython.display import clear_output
!wget -O test.jpg "https://img2.thuthuatphanmem.vn/uploads/2019/01/04/hinh-anh-hot-girl-dep_025104603.jpg"
clear_output()
fn="test.jpg"
img1 = cv2.imread(fn)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
TA_Imshow_imgs([img1,img2],Title="Anh goc, Anh da muc xam",)
#========================================================
```


