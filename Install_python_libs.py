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


















