# List file và thư mục, hiển thị size, duration, length của ảnh, video, audio

```python
P='/content/drive/My Drive'


moviext =[".mp4",".avi",".mov",".flv",".wmv"]
AudioExt=['.mp3','.wav']
ImgExt  =['.jpg','.png','.bmp']

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

