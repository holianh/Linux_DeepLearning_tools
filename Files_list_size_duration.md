# List file và thư mục, hiển thị size, duration, length của ảnh, video, audio
## Version 2:
```python
try:
    from videoprops import get_video_properties
except:
    !pip install -U get-video-properties  
    from videoprops import get_video_properties

def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)
def getVIDEO_infor(fn):
    props = get_video_properties(fn)
    return "{:>4}x{:>4} {}".format(props['height'],props['width'],format_seconds_to_hhmmss(float(props['duration'])))

# getVIDEO_infor(fn)    
# =========================================================
from datetime import datetime
import time
# Init:----------------------------------------
# Ntotal=10    # Tổng số cần chạy
# cnt=0
start=datetime.now()
#==========================================================
P='/content/drive/My Drive/Pictures-Videos_Giadinh/Videos'
Nmax=30
Allcnt=0
moviext =[".mp4",".avi",".mov",".flv",".wmv"]
AudioExt=['.mp3','.wav']
ImgExt  =['.jpg','.png','.bmp','jpeg']

import os
# !pip install moviepy
from os.path import join, exists, basename, dirname
from moviepy.editor import VideoFileClip
import time
import librosa
from PIL import Image
from subprocess import check_output

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def getVideoInfo(file_name):
    d = str(check_output('ffprobe -i  "'+file_name+'" 2>&1 |grep "Duration:"',shell=True)) 
    Duration=d.split(": ")[1].split(".")[0]
    a = str(check_output('ffprobe -v error -show_entries stream=width,height -of default=noprint_wrappers=1:nokey=1 "{}"'.format(file_name),shell=True)) 
    a=a.replace('\\n','x')
    a=a.replace("b'",'')
    hw=a.replace("x'",'')
    return "{:>9} {}".format(hw,Duration)

fis=[]
for D, _ , F in os.walk(P):
    fis.append(['.','.', '.', D])
    for cnt,fn in enumerate(F):
        try:
        # if 1==1:
            ffn=join(D,fn)
            flen = None
            if fn[-4:].lower() in moviext:
                #   clip = VideoFileClip(ffn)
                #   flen=clip.duration
                # d = str(check_output('ffprobe -i  "'+ffn+'" 2>&1 ',shell=True)) 
                # flen=d.split("Duration: ")[1].split(".")[0]
                # framewh=d.split("Video: ")[1].split(", ")[2].split(' ')[0]
                flen=getVIDEO_infor(ffn)
            if fn[-4:].lower() in AudioExt:
                y, sr = librosa.load(librosa.util.example_audio_file())
                duration_ss=librosa.get_duration(y=y, sr=sr)
                flen=time.strftime('%H:%M:%S', time.gmtime(duration_ss))
            if fn[-4:].lower() in ImgExt:
                im = Image.open(ffn)
                width, height = im.size
                flen="{}x{}".format(width, height)
            fsize=os.path.getsize(ffn)
            fis.append([cnt,flen, fsize, ffn])
        except:
            print('err: ',ffn)
            pass
        if(Allcnt % 50)==0:
            TRan=datetime.now()-start
            print(TRan,Allcnt,ffn)
        Allcnt+=1
        if (Nmax>0) and (Allcnt>Nmax):
            break
    if (Nmax>0) and (Allcnt>Nmax):
        break
print('len fis=',len(fis))

sumsize=0
sum_all_size=0
with open('thongtin.txt', 'w') as ff:
   ff.write("P={}\n".format(P))
   for cnt,flen, fsize, ffn in fis:
      if  fsize=='.':
          ff.write(" {} \t {:>10} \t{}\n".format('-', 'Total:', sizeof_fmt(sumsize)))
          ff.write(" {} \t {:>10} \t{}\n".format('-', '-', ffn))
          sum_all_size+=sumsize
          sumsize=0
      else:
          dn=dirname(ffn)
          dn=''.join(['├── ' for x in dn.split('/') ])
          bn=basename(ffn)
          sumsize=sumsize+fsize
          fsizeh=sizeof_fmt(fsize)
          ff.write("{:>3}.[{}] [{:>10}]\t{}{}\n".format(cnt,flen, fsizeh, dn,bn))
   ff.write(" {} \t {:>10} \t{}\n".format('-', 'Total:', sizeof_fmt(sumsize)))
   ff.write(" {} \t {:>10} \t{}\n".format('-', 'Total All:', sizeof_fmt(sum_all_size)))
print(TRan)
```

## Version 1:
```python
P='/content/drive/My Drive'


moviext =[".mp4",".avi",".mov",".flv",".wmv"]
AudioExt=['.mp3','.wav']
ImgExt  =['.jpg','.png','.bmp','jpeg']

import os
# !pip install moviepy
from os.path import join, exists, basename, dirname
from moviepy.editor import VideoFileClip
import time
import librosa
from PIL import Image
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


fis=[]
for D, _ , F in os.walk(P):
    fis.append(['.','.', '.', D])
    for cnt,fn in enumerate(F):
        try:
          ffn=join(D,fn)
          flen = 0
          if fn[-4:].lower() in moviext:
              clip = VideoFileClip(ffn)
              flen=clip.duration
          if fn[-4:].lower() in AudioExt:
              y, sr = librosa.load(librosa.util.example_audio_file())
              duration_ss=librosa.get_duration(y=y, sr=sr)
              flen=time.strftime('%H:%M:%S', time.gmtime(duration_ss))
          if fn[-4:].lower() in ImgExt:
              im = Image.open(ffn)
              width, height = im.size
              flen="{}x{}".format(width, height)
          fsize=os.path.getsize(ffn)
          fis.append([cnt,flen, fsize, ffn])
        except:
            print(ffn)
            pass

sumsize=0
with open('thongtin.txt', 'w') as ff:
   for cnt,flen, fsize, ffn in fis:
      if  fsize=='.':
          ff.write(" {} \t {:>10} \t{}\n".format('-', 'Total:', sizeof_fmt(sumsize)))
          ff.write(" {} \t {:>10} \t{}\n".format('-', '-', ffn))
          sumsize=0
      else:
          dn=dirname(ffn)
          dn=''.join(['├── ' for x in dn.split('/') ])
          bn=basename(ffn)
          sumsize=sumsize+fsize
          fsizeh=sizeof_fmt(fsize)
          ff.write("{}.[{}]\t[{:>10}]\t{}{}\n".format(cnt,flen, fsizeh, dn,bn))
   ff.write(" {} \t {:>10} \t{}\n".format('-', 'Total:', sizeof_fmt(sumsize)))


```

