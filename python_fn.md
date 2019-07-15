# Mục lục
[Date time](#date-time)

-   [Get time of file to make filename](#Get-time-of-file-to-make-filename)










# Date time 
## Get time of file to make filename

Result: '2019-07-14---12-35-40'

```python
import time,os,re
def getTimeofFile(fn):
    m={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
       'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12',
       '01':'01','02':'02','03':'03','04':'04','05':'05','06':'06',
       '07':'07','08':'08','09':'09','10':'10','11':'11','12':'12'}
    fTime=time.ctime(os.path.getmtime(fn))
    fTime=re.sub(' +', ' ',fTime)#    print(fTime)
    tof=fTime.split(' ')#;    print(tof)
    hms=tof[3].split(':')
    t="_{}-{}-{:>02}---{:>02}-{:>02}-{:>02}".format(tof[4],m[tof[1]],tof[2],hms[0],hms[1],hms[2])
    return t
# fn='/home/u/darknet/data/yolov3-tiny-videos.weights'
# ss=getTimeofFile(fn)
# print(ss)
```


