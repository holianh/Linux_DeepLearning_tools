from concurrent.futures import ThreadPoolExecutor
from Levenshtein import distance
from matplotlib.backends.backend_pdf import PdfPages
from os.path import  join,join as jj,  exists,exists as tt,  basename,basename as bname
from string import whitespace
import datetime as dt
import io
import keras
import lasagne
import librosa
import logging
import matplotlib
import matplotlib.pyplot as plt
import numpy as np;
import os;
import pandas as pd
import pickle;
import random
import re
import soundfile
import sys;
import wave
import shutil
import pypinyin







######################################################################
Installing via PIP
######################################################################
pip install pypinyin
pip install pipreqs
pip install lasagne
pip install librosa --upgrade
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
sudo apt-get install libsamplerate0 libsamplerate0-dev
pip install scikits.samplerate
pip install info



######################################################################
Installing via Anaconda
######################################################################

conda install -c anaconda anaconda-navigator
conda install scikit-learn



######################################################################
Installing Software via umake
######################################################################

sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
sudo apt-get update
sudo apt-get install ubuntu-make

$ umake ide pycharm                 # community version
$ umake ide pycharm-professional    # professional version
>>> umake -r ide pycharm              # To remove PyCharm installed via umake, use the command below:


######################################################################
Installing Software using PPA
######################################################################
Install PyCharm:
  sudo add-apt-repository ppa:mystic-mirage/pycharm
  sudo apt-get update
   
  $ sudo apt-get install pycharm-community  # community version
  $ sudo apt-get install pycharm            # professional version














