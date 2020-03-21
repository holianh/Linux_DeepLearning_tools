from IPython.display import clear_output, Image
import base64,cv2
from google.colab.patches import cv2_imshow
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

#%matplotlib inline
import shutil
import numpy as np

from matplotlib import animation, rc
from IPython.display import HTML
import os,glob
import random

from PIL import Image
# img = Image.open('image.png').convert('LA')
# img.save('greyscale.png')

from skimage import color
from skimage import io
import skimage
# img = color.rgb2gray(io.imread('image.png'))
import sys
import numpy as np
import skimage.io
import skimage.filters


sss="""
!wget -O taLibs_imports.py  https://github.com/holianh/Linux_DeepLearning_tools/raw/master/taLibs_imports.py
!wget -O DarkLabel_ConvertTools.py  https://github.com/holianh/Linux_DeepLearning_tools/raw/master/DarkLabel_ConvertTools.py

clear_output()
exec(open('taLibs_imports.py').read())
exec(open('DarkLabel_ConvertTools.py').read())

"""
print(sss)


