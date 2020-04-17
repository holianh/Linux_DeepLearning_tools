"""Converts png, bmp and gif to jpg, removes descriptions and resizes the image to a maximum of 1920x1080."""

from PIL import Image
from glob import glob
import PIL
import sys
import os
from os.path import join,exists,dirname,basename
from tqdm import tqdm
path_new       = '/home/u/2020/Palm/Dataset'
path_originals = '/home/u/2020/Palm/Data'

outpQuality=100

if not path_new[-1:]=='/':          path_new+='/'
if not path_originals[-1:]=='/':    path_originals+='/'

def compress_image(image, infile):
    size = 1920, 1080
    width = 1920
    height = 1080
    #print(infile)
    pname = infile.split('.')
    outp  = pname[0] + '.jpg'
    outp  = outp.replace(path_originals,path_new)
    #print(outp)
    if not exists(dirname(outp)):
        os.makedirs(dirname(outp))
    
    if image.size[0] > width and image.size[1] > height:
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(outp, quality=outpQuality)
    elif image.size[0] > width:
        wpercent = (width/float(image.size[0]))
        height = int((float(image.size[1])*float(wpercent)))
        image = image.resize((width,height), PIL.Image.ANTIALIAS)
        image.save(outp,quality=outpQuality)
    elif image.size[1] > height:
        wpercent = (height/float(image.size[1]))
        width = int((float(image.size[0])*float(wpercent)))
        image = image.resize((width,height), PIL.Image.ANTIALIAS)
        image.save(outp, quality=outpQuality)
    else:
        image.save(outp, quality=outpQuality)


def processImage(listing):
    print('All files=',len(listing))            
    for k in tqdm(range(len(listing))):
        infile=listing[k]
        img = Image.open(infile)
        if img.format == "JPEG":
            image = img.convert('RGB')
            compress_image(image, infile)
            img.close()

        elif img.format == "GIF":
            i = img.convert("RGBA")
            bg = Image.new("RGBA", i.size)
            image = Image.composite(i, bg, i)
            compress_image(image, infile)
            img.close()
        elif img.format == "PNG":
            try:
                image = Image.new("RGB", img.size, (255,255,255))
                image.paste(img,img)
                compress_image(image, infile)
            except ValueError:
                image = img.convert('RGB')
                compress_image(image, infile)
            img.close()
        elif img.format == "BMP":
            image = img.convert('RGB')
            compress_image(image, infile)
            img.close()
        else:
            print('No process:',infile)
        #exit()

listing0=[]
for D,_,F in os.walk(path_originals):
    for fn in F:
        if fn[-4:].upper() in ['JPEG','.GIF','.PNG','.BMP','.JPG']:
            listing0.append(join(D,fn))
listing=listing0[:10]
processImage(listing)
