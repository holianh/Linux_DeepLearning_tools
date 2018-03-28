#taLibs.py
import timeit,math
import pickle;
import io, json
import sys
import soundfile as sf
import numpy as np;
import os
from os.path import exists,join,expanduser
from random import shuffle
import io, json
import librosa;
from keras.preprocessing.text import Tokenizer;
import matplotlib                                    ###############
matplotlib.use('agg')
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np;
import time
import datetime as dt
import shutil

from difflib import SequenceMatcher

import warnings
warnings.filterwarnings("ignore")
import io,json

home = expanduser("~")


print ('_____from:',os.getcwd(), os.path.basename(__file__))
from augmentations import *
#from augmentations import *
#sshfs tact@10.1.58.23:/home/tact/ ~/tact
#Below test has been written to take all the files in a directory and apply all types of degradations 
#on them and create relevantly named files in the same directory. You can also apply them on single files


################################################################################
fn_char_index="char_index.pickle"
fn_index_char="index_char.pickle"

DataHome='/home/tact/AudioDBs/All_database_processed/' #  '/home/ubuntu/ChineseADB/All_DataBase/'
Wav_path='/home/tact/AudioDBs/All_database_processed/train/' #'/home/ubuntu/ChineseADB/All_DataBase/tadb100'
DataPath='/home/tact/AudioDBs/All_database_processed_augment/' #'/home/ubuntu/ChineseADB/All_database_processed/'
sNeedRemove =''   #/home/tact/AudioDBs/All_DataBase' # loại bỏ đường dẫn dư thừa. (co the khong can bo)

# Lưu CSV path tại data .wav folder
csv_path='info/' # lưu vào thư mục đang chạy.
pproject_info='info/project_info.txt'

wav_train_path=csv_path+'data_train_path.csv'
wav_test__path=csv_path+'data_test__path.csv'


DataPath_Train_npy  = DataPath      +'Train_npy/'
Train_npy_info      = DataPath      +'Train_npy_info/'
pAll_labels         = Train_npy_info+'All_labels.txt'

pWords_dic  = Train_npy_info + 'Words_dic.txt'
pchar_index = Train_npy_info + 'char_index.pkl'
pindex_char = Train_npy_info + 'index_char.pkl'
pinfo       = Train_npy_info + 'info.txt'

if not os.path.exists(DataPath):os.makedirs(DataPath)
if not os.path.exists(DataPath_Train_npy):os.makedirs(DataPath_Train_npy)
if not os.path.exists(Train_npy_info):os.makedirs(Train_npy_info)


##############################################################################

def Files_2csv_inDir(path, wav_exe='.wav'):
    count = 0
    Fis=[]
    for subdir, dirs, files in os.walk(path):
        for fi in files:
            if fi.endswith(wav_exe): # eg: '.txt'
                count += 1
                ph=subdir.replace(sNeedRemove,'')
                Fis.append(ph+'/'+fi)
    shuffle(Fis)
    Full_len=len(Fis)
    train_len= round(Full_len * 0.8)
    test_len = Full_len - train_len
    if not os.path.exists(csv_path):os.makedirs(csv_path)
    
    fn=open(wav_train_path,'w')
    ft=open(wav_test__path,'w')
    
    k=0
    for item in Fis:
        k+=1
        if(k<train_len): fn.write("%s\n" % item)
        else:            ft.write("%s\n" % item)
    fn.close()
    ft.close()
    print('Created files:')
    print(wav_train_path,train_len,'Files')
    print(wav_test__path,test_len,'Files')
    
    return train_len,test_len
# ~ Files_2csv_inDir(Wav_path)
# ~ print('Finished!!!!')
##############################################################################

def Find_longest_label_csv(wav_csv_path,extension='.ta'):  #from csv file, label file ext: '.ta'
    print('process: Find_longest_label from...',wav_csv_path)
    max_len=0; longest = ("", "")
    
    print('Find longest label...')
    with open(wav_csv_path) as fis:
        files=fis.read().split('\n')
        del files[-1]
    print('number of',extension,'files=', len(files))
    for f in files:
        with open(f+extension) as flbl:s=flbl.readline()
        s=s.replace(' ','')
        s=s.replace('\n','')
        if max_len<len(s):
            max_len=len(s)
            longest=(s,f)
    print('max_len label=',max_len)
    print(longest)
    return max_len,longest

# ~ max_len=Find_longest_label_csv(wav_train_path,'.ta')
# ~ print('max_len label=',max_len)
# ~ print('=====================================================================')
################################################################################

def Find_longest_label_fromDir(path,extension='.ta'): # from wav folder
    # A4_21.wav
    # A4_21.wav.ta
    print('process: Find_longest_label...')
    max_len=0; s0=''
    k=0
    ff=''
    print('find longest label...')
    for subdir, dirs, files in os.walk(path):
        if(k%10==0):print(subdir)
        k+=1
        for f in files:
            if f.endswith(extension): # eg: '.txt'
                #print(join(subdir,f))
                with open(join(subdir,f)) as flbl:s=flbl.readline()
                s=s.replace(' ','')
                if max_len<len(s):
                    max_len=len(s)
                    s0=s
                    ff=join(subdir,f)
    return max_len,s0,ff

# ~ max_len=Find_longest_label(Wav_path,'.ta')
# ~ print('max_len label=',max_len)
#=================================================================================
################################################################################

def Find_biggest_file_csv(wav_csv_path,extension='.wav'):
    print('process: Find_biggest_file...')
    biggest = ("", -1)
    with open(wav_csv_path) as fis:
        files=fis.read().split('\n')
        del files[-1]
    print('number of',extension,'files=', len(files))

    for item in files:
        f = sf.SoundFile(item)
        #print('samples = {}'.format(len(f)))
        #print('sample rate = {}'.format(f.samplerate))
        #print('seconds = {}'.format(len(f) / f.samplerate))
        if biggest[1] < len(f) / f.samplerate:
            biggest=(item,len(f) / f.samplerate)
    print('file_biggest=',biggest)
    return biggest  

# ~ file_biggest=Find_biggest_file(wav_train_path) #max_len_wav,
# ~ print('file_biggest=',file_biggest)
################################################################################

def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)
#--------------- --------------- --------------- ---------------
# Stop counting time, make a time string to print out to screen
################################################################################
def LenMFCC_1file(file_path):
    wav, sr = librosa.load(file_path, mono=True,res_type='kaiser_fast')
    b = librosa.feature.mfcc(wav, sr)
    mfcc = np.transpose(b, [1, 0]);
    lenmfcc_t=len(mfcc)
    return lenmfcc_t,mfcc
def GetLabel_1file(file_path,lbl_extension='.ta'):
    with open(file_path+lbl_extension) as flbl:s=flbl.readline()
    s=s.replace(' ','')
    s=s.replace('\n','')
    return s
            
def Read_csv_to_list(csv_path):
    with open(csv_path) as fis:
        csv_path_files=fis.read().split('\n')
        del csv_path_files[-1]
    return csv_path_files
    
def build_Words_dict():         # Run 2nd
 
    with open(pproject_info) as data_file:data_loaded = json.load(data_file)
    wav_train_path=data_loaded['wav_train_path']
    wav_test__path=data_loaded['wav_test__path']
    pchar_index=data_loaded['subpaths']['pchar_index']
    pindex_char=data_loaded['subpaths']['pindex_char']
    
    #1: read all labels words:
    def read_all_lbls(csv_path,lbl_extension='.ta'):
        csv_path_files=Read_csv_to_list(csv_path)
        sents=[]
        for item in csv_path_files:
            sents.append(GetLabel_1file(item))
        return sents
    sentences=read_all_lbls(wav_train_path)
    All_chars=[]
    for sent in sentences:
        for ch in sent:
            All_chars.append(ch)

    sentences=read_all_lbls(wav_test__path)
    for sent in sentences:
        for ch in sent:
            All_chars.append(ch) 
    All_chars.append('')
    All_chars.append(' ')
    All_chars.append('\0')
    
    tok=Tokenizer(char_level=True);tok.fit_on_texts(All_chars);
    char_index=tok.word_index;index_char=dict((char_index[i],i) for i in char_index);
    print('total ',len(char_index),'chars in dictionary.')

    with open(pchar_index, 'wb') as handle: pickle.dump(char_index,handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open(pindex_char, 'wb') as handle: pickle.dump(index_char,handle, protocol=pickle.HIGHEST_PROTOCOL)
    print('Saved char_index (index_char) into',pchar_index)
    
def update_current_pos(current_pos=0,save2File=True):
    with open(pproject_info) as data_file:data_loaded = json.load(data_file)
    curp=data_loaded['current_pos']
    if save2File:
        data_loaded['current_pos']=current_pos
        with open(pproject_info, 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data_loaded,indent=4, sort_keys=True,separators=(',', ':'), ensure_ascii=False)
            outfile.write(str_)
    return curp
    
def Get_DB_info(wav_csv_path):  # run 1st
    print('process: Get_DB_info(data_path)')
    start = timeit.default_timer()  # Start counting time
    #1: make file list...............................................
    train_len,test_len=Files_2csv_inDir(Wav_path)
    
    #2: find longest label...........................................
    longest_label,longest=Find_longest_label_csv(wav_csv_path)
    
    #3: find biggest wav file .......................................
    biggest_file =Find_biggest_file_csv(wav_csv_path)
    
    print('longest_label=',longest_label,longest)
    print('biggest_file=',biggest_file)
    
    #--------------------------------------------------------------------
    lenmfcc_t,mfcc=LenMFCC_1file(biggest_file[0])
    
    augment1file(biggest_file[0])
    lenmfcc_t2=lenmfcc_t
    for fi in os.listdir('output/'):
        if fi.endswith('.wav'):
            auFi='output/'+fi
            lenmfcc_t1,mfcc=LenMFCC_1file(biggest_file[0])
            if lenmfcc_t2<lenmfcc_t1:lenmfcc_t2=lenmfcc_t1
    for fi in os.listdir('output/'):os.unlink('output/'+fi)
    #--------------------------------------------------------------------
    f = sf.SoundFile(biggest_file[0])
    print('file samples = {}'.format(len(f)))
    print('file sample rate = {}'.format(f.samplerate))
    print('file seconds = {}'.format(len(f) / f.samplerate))
    #--------------------------------------------------------------------
    data = {"DataHome":DataHome,
            "DataPath":DataPath,
            "Max_len_MFCC":lenmfcc_t,
            'Max_len_MFCC_Augm':lenmfcc_t2,
            "Max_len_label_no_space":longest_label,
            "Wav_path":Wav_path,
            "biggest_wavfile":biggest_file[1],
            "biggest_wavfile_path":biggest_file[0],
            'wav_train_path':csv_path+'data_train_path.csv',
            'wav_test__path':csv_path+'data_test__path.csv',
            'csv_path':'info/',
            'current_pos':0,
            'subpaths':{
                        'DataPath_Train_npy':DataPath      +'Train_npy/',
                        'Train_npy_info'    :DataPath      +'Train_npy_info/',
                        'pAll_labels'       :Train_npy_info+'All_labels.txt',

                        'pWords_dic'        :Train_npy_info + 'Words_dic.txt',
                        'pchar_index'       :Train_npy_info + 'char_index.pkl',
                        'pindex_char'       :Train_npy_info + 'index_char.pkl',
                        'pinfo'             :Train_npy_info + 'info.txt',
                        },
            'train_len':train_len,
            'test_len':test_len,
            'NoAugmentfiles':5      
            # When can install SOX &  rubberband-cli then change in this and in: def augment1file(current_file)
            }
    print('data save!')
    with open(pproject_info, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,indent=4, sort_keys=True,separators=(',', ':'), ensure_ascii=False)
        outfile.write(str_)
     
    with open(pinfo, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,indent=4, sort_keys=True,separators=(',', ':'), ensure_ascii=False)
        outfile.write(str_)
    #--------------------------------------------------------------------
    stop = timeit.default_timer()
    total_time=stop-start # in seconds
    tRan=format_seconds_to_hhmmss(math.trunc(total_time))
    print('Time run=',tRan)
    
    return longest_label,biggest_file

#Get_DB_info(wav_train_path)
################################################################################

def getLbl_MFCC_1file(wavfile_path,lbl_extension='.ta'): # lbl_path=wavfile_path+lbl_extension
    lenmfcc_t,mfcc=LenMFCC_1file(wavfile_path)
    with open(wavfile_path+lbl_extension) as flbl:s=flbl.readline()
    s=s.replace(' ','')
    s=s.replace('\n','')
    lenS=len(s)
    return (lenmfcc_t,mfcc),(lenS,s)

import tarfile
def Get_Batch_MFCC_Labels(wav_csv_path,number_of_files): # Run 3rd    number_of_files=Epoch/batch
    print('===================Get_MFCC_Labels=====================')
    with open(pproject_info) as data_file:data_loaded = json.load(data_file)
    current_pos = update_current_pos(0,False)
    fin='{}_{}'.format(number_of_files,current_pos)   
    f1=join(DataPath_Train_npy,fin+'=mfcc____.npy')
    f2=join(DataPath_Train_npy,fin+'=mfcc_len.npy')
    f3=join(DataPath_Train_npy,fin+'=char_vec.npy')
    f4=join(DataPath_Train_npy,fin+'=char_len.npy')
    print()
    print('Making file:',f1+".tar.gz")
    # ~ print(f2)
    # ~ print(f3)
    # ~ print(f4)
    fnen=f1+".tar.gz"
    if exists (fnen): # giai nen
        if not exists(f1):
            os.system('nohup bash tar_npy.sh 0 ' + fnen + ' ' + DataPath_Train_npy)
        
        while not exists(f1):time.sleep(1)
        print(f1)
        mfcc_vec_out=np.load(f1)
        MFCC_len=np.load(f2)
        char_vec=np.load(f3)
        char_length=np.load(f4)

    else: # f1: exist, read back     
        with open(pchar_index,"rb") as f: char_index=pickle.load(f);
        # ~ with open(pindex_char,"rb") as f: index_char=pickle.load(f);
        
        Max_len_MFCC=data_loaded['Max_len_MFCC']
        maxlen_char=data_loaded['Max_len_label_no_space']
        MaxSample=number_of_files
        
        mfcc_vec=[[] for _ in np.arange(0,MaxSample)]; 
        
        char_length=np.zeros((MaxSample,1),dtype=np.float32);
        char_vec=np.zeros((MaxSample,maxlen_char),dtype=np.float32);
        
        Files=Read_csv_to_list(wav_csv_path) # read all file paths to list
        
        nextP=(current_pos+number_of_files)%len(Files)
        if nextP<current_pos:
            FO=Files[current_pos:]+Files[:nextP]
            current_pos=nextP
            #current_pos=0
        else:
            FO=Files[current_pos:current_pos+number_of_files]
            current_pos=current_pos+number_of_files
        
        for k,file1 in enumerate(FO):
            lenmfcc_t,mfcc=LenMFCC_1file(file1)
            mfcc_vec[k]=mfcc
            
            lbl=GetLabel_1file(file1)
            
            #char_input.append(lbl)
            char_length[k]=len(lbl)
            
            for j,ele in enumerate(lbl):
                char_vec[k,j]=char_index[ele];
            print('.',end='',flush=True)
            
        mfcc_vec_out=np.zeros((MaxSample,Max_len_MFCC,20),dtype=np.float32);
        for i in np.arange(0,len(mfcc_vec)):
            for j in np.arange(0,len(mfcc_vec[i])):
                for k,ele in enumerate(mfcc_vec[i][j]): 
                    mfcc_vec_out[i,j,k]=ele;                  
        print()
    
        MFCC_len=np.ones(MaxSample)*Max_len_MFCC
        
        np.save(f1,mfcc_vec_out)   
        np.save(f2,MFCC_len)       
        np.save(f3,char_vec)       
        np.save(f4,char_length)   
        # Nen all file *.npy 
        os.system('nohup bash tar_npy.sh 1 ' + fnen + ' ' + DataPath_Train_npy)
        
    if (current_pos+number_of_files>=data_loaded['train_len']):current_pos=0
    update_current_pos(current_pos)
    
    # Giai nen san, chuan bi cho luot ke tiep:
    fin='{}_{}'.format(number_of_files,current_pos)   
    f1=join(DataPath_Train_npy,fin+'=mfcc____.npy')
    f2=join(DataPath_Train_npy,fin+'=mfcc_len.npy')
    f3=join(DataPath_Train_npy,fin+'=char_vec.npy')
    f4=join(DataPath_Train_npy,fin+'=char_len.npy')
    fnen=f1+".tar.gz"
    if exists (fnen): # giai nen
        if not exists(f1):
            os.system('nohup bash tar_npy.sh 0 ' + fnen + ' ' + DataPath_Train_npy)
    
    return mfcc_vec_out,  MFCC_len, char_vec, char_length # last possiton in file list/batch
#return (X), next_Pos

#################################################################################################################



def augment1file(current_file):
    if not exists('tmp/'):os.makedirs('tmp')
    #print ("\nAugmenting:" + current_file)
    #random_cropping(current_file, 2)
    add_noise(current_file, 'white-noise', 20)
    convolve(current_file, 'classroom', 0.5)
    convolve(current_file, 'smartphone_mic', 0.5)
    apply_gain(current_file, 20)
    
    # require install SOX, rubberband:
    
    # ~ apply_rubberband(current_file, time_stretching_ratio=0.5)
    # ~ apply_rubberband(current_file, pitch_shifting_semitones=2)
    # ~ apply_dr_compression(current_file, 2)
    # ~ apply_eq(current_file, '500;50;30')
    
    #print(len(os.listdir('output/')), 'files created!')
    #for fi in os.listdir('output/'):
    #    print('output/'+fi)
    #print()
    
    for fi in os.listdir('tmp/'):
        os.unlink('tmp/'+fi)
    
    #print('Augmented!')


import timeit,math
def display_persent(start,Total,curr):
    k=50.0/Total
    pt=round(k*curr)

    stop = timeit.default_timer()
    total_time=stop-start # in seconds
    tRan=format_seconds_to_hhmmss(math.trunc(total_time))
    if pt==0:
        tWait=format_seconds_to_hhmmss(math.trunc(50*total_time))
    else:
        tWait=format_seconds_to_hhmmss(math.trunc(((50-pt)*total_time)/pt))
    s='{}/{} {}% [{}>{}] run:{} wait:{}   '.format(curr,Total,round(k*curr*2,1),'='*pt,'.'*(50-pt),tRan,tWait)
    print(s,end='\r',flush=True)
    return s


##################################################################################################################
def Get_Batch_MFCC_Labels_Augmentation(wav_csv_path,number_of_files): # Run 3rd    number_of_files=Epoch/batch
    start = timeit.default_timer()
    #print('===================Get_MFCC_Labels=====================')
    with open(pproject_info) as data_file:data_loaded = json.load(data_file)
    NoAugmentfiles=data_loaded['NoAugmentfiles']
    current_pos = update_current_pos(0,False)
    fin='{}x{}_{}'.format(NoAugmentfiles,number_of_files,current_pos)   
    f1=join(DataPath_Train_npy,fin+'=mfcc____.npy')
    f2=join(DataPath_Train_npy,fin+'=mfcc_len.npy')
    f3=join(DataPath_Train_npy,fin+'=char_vec.npy')
    f4=join(DataPath_Train_npy,fin+'=char_len.npy')
    print()
    print()
    fnen=f1+".tar.gz"
    if exists (fnen): # giai nen
        print('Extracting file:',f1+".tar.gz")
        if not exists(f1):
            os.system('nohup bash tar_npy.sh 0 ' + fnen + ' ' + DataPath_Train_npy)
        
        while not exists(f1):time.sleep(1)
        print(f1)
        mfcc_vec_out=np.load(f1)
        MFCC_len=np.load(f2)
        char_vec=np.load(f3)
        char_length=np.load(f4)
        current_pos=current_pos+number_of_files
        if (current_pos>=data_loaded['train_len']):current_pos=0
    else: # f1: Not exist, read back     
        print('Creating new file:',f1+".tar.gz")
        with open(pchar_index,"rb") as f: char_index=pickle.load(f);
        # ~ with open(pindex_char,"rb") as f: index_char=pickle.load(f);
        
        #TODO:
            # Cap nhat lai Max MFCC
        
        #Max_len_MFCC=data_loaded['Max_len_MFCC']
        Max_len_MFCC=data_loaded['Max_len_MFCC_Augm']
        maxlen_char =data_loaded['Max_len_label_no_space']
        MaxSample   =number_of_files*NoAugmentfiles
        
        mfcc_vec=[[] for _ in np.arange(0,MaxSample)]; 
        
        char_length=np.zeros((MaxSample,1),dtype=np.float32);
        char_vec=np.zeros((MaxSample,maxlen_char),dtype=np.float32);
        
        Files=Read_csv_to_list(wav_csv_path) # read all file paths to list
        
        nextP=(current_pos+number_of_files)%len(Files)
        if nextP<current_pos:
            FO=Files[current_pos:]+Files[:nextP]
            #current_pos=nextP
            current_pos=0
        else:
            FO=Files[current_pos:nextP]
            current_pos=nextP
        
        for k,file1 in enumerate(FO):
            lenmfcc_t,mfcc=LenMFCC_1file(file1)
            mfcc_vec[k*NoAugmentfiles]=mfcc
            lbl=GetLabel_1file(file1)
            len_lbl=len(lbl)
            char_length[k*NoAugmentfiles]=len_lbl
            for j,ele in enumerate(lbl):
                char_vec[k,j]=char_index[ele];
            s=display_persent(start,MaxSample,k*NoAugmentfiles)#display convert status
            #print(s,end=' ',flush=True)
            #---------------------------------------------------
            augment1file(file1)
            k1=1
            for fi in os.listdir('output/'):
                if fi.endswith('.wav'):
                    auFi=os.path.abspath('output/'+fi)
                    
                    #print(auFi)
                    lenmfcc_t,mfcc=LenMFCC_1file(auFi)
                    mfcc_vec   [k*NoAugmentfiles+k1]=mfcc
                    char_length[k*NoAugmentfiles+k1]=len_lbl
                    for j,ele in enumerate(lbl):
                        char_vec[k*NoAugmentfiles+k1,j]=char_index[ele];
                    k1+=1
                    #display_persent(start,MaxSample,k*NoAugmentfiles+k1)#display convert status
            for fi in os.listdir('output/'):os.unlink('output/'+fi)
            #---------------------------------------------------
            
        print()    
        print()
        mfcc_vec_out=np.zeros((MaxSample,Max_len_MFCC,20),dtype=np.float32);
        for i in np.arange(0,len(mfcc_vec)):
            for j in np.arange(0,len(mfcc_vec[i])):
                for k,ele in enumerate(mfcc_vec[i][j]): 
                    mfcc_vec_out[i,j,k]=ele;                  
        
    
        MFCC_len=np.ones(MaxSample)*Max_len_MFCC
        
        np.save(f1,mfcc_vec_out)   
        np.save(f2,MFCC_len)       
        np.save(f3,char_vec)       
        np.save(f4,char_length)   
        # Nen all file *.npy 
        os.system('nohup bash tar_npy.sh 1 ' + fnen + ' ' + DataPath_Train_npy)
        
    
    update_current_pos(current_pos)
    
    # Giai nen san, chuan bi cho luot ke tiep:
    fin='{}_{}'.format(number_of_files,current_pos)   
    f1=join(DataPath_Train_npy,fin+'=mfcc____.npy')
    f2=join(DataPath_Train_npy,fin+'=mfcc_len.npy')
    f3=join(DataPath_Train_npy,fin+'=char_vec.npy')
    f4=join(DataPath_Train_npy,fin+'=char_len.npy')
    fnen=f1+".tar.gz"
    if exists (fnen): # giai nen
        if not exists(f1):
            os.system('nohup bash tar_npy.sh 0 ' + fnen + ' ' + DataPath_Train_npy)
    
    return mfcc_vec_out,  MFCC_len, char_vec, char_length # last possiton in file list/batch
#return (X), next_Pos


def plotHistory(history,
         strNeedPlot=('loss','acc'),#,'loss'),#,'acc','loss','acc'),
         Labels=(['Training Loss'    ,'Epochs','Loss value'],
                 ['Training Accuracy','Epochs','Accuracy value'],
                 ['Label 3','X label3','Ylabel3'],
                 ['Label 4','X label4','Ylabel4'],
                 ['Label 5','X label5','Ylabel5'],
                 ['Label 6','X label6','Ylabel6'],
                 ),
          NoColumns=1,
          nb_plots_per_page = 3,               # Total number in one page to print.
          fdfName='history_training.pdf',
          sPreFix=''
         ):
    # Plot history of training in keras to pdf
    # history=model.fit(...) in keras
    # history={'loss':[1,2,3,...n],'acc':[1,2,3,...,m]}
    # strNeedPlot=('loss','acc','loss','acc','loss')
    tgian=dt.datetime.now()
    
    sTgian=str(tgian).split('.')[0].replace(':','-')
    fdfName=fdfName.replace('[]',sPreFix+'__'+sTgian)
    #fdfName=fdfName.split('.')[0]+'_'+sPreFix+'__'+sTgian+'.pdf'
    print('print(tgian):',tgian)
    print(sTgian)
    print(fdfName)
    pdf_pages = PdfPages(fdfName)
    nb_plots = len(strNeedPlot)         # Number of images
    if(nb_plots_per_page>nb_plots):nb_plots_per_page=nb_plots;
    nb_pages = int(np.ceil(nb_plots / float(nb_plots_per_page)))#No of Pages
    grid_size = (nb_plots_per_page, NoColumns)  # Number of columns
    PaperSize=A4=(8.27, 11.69)          # paper size in inch
    i=0
    for sType in strNeedPlot:
        # Create a figure instance (ie. a new page) if needed
        if i % nb_plots_per_page == 0: fig = plt.figure(figsize=PaperSize, dpi=100) 
        # Plot stuffs !
        ax=plt.subplot2grid(grid_size, (i % nb_plots_per_page, 0))
        plt.subplots_adjust(wspace=0, hspace=.5)
        plt.subplots_adjust(left=0.2)
        plt.subplots_adjust(top=0.88)
        plt.plot(history.history[sType])
        
        ax.set_title(Labels[i][0] +'  '+ sPreFix+'__'+sTgian)
        plt.xlabel(Labels[i][1], fontsize=14)
        plt.ylabel(Labels[i][2], fontsize=14)
        plt.grid()
        
        # Close the page if needed
        if (i + 1) % nb_plots_per_page == 0 or (i + 1) == nb_plots:
            #plt.tight_layout()
            pdf_pages.savefig(fig)
        i+=1
        ''' #examples
        fig = plt.figure()
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)
        ax4 = fig.add_subplot(224)
        ax1.title.set_text('First Plot')
        ax2.title.set_text('Second Plot')
        ax3.title.set_text('Third Plot')
        ax4.title.set_text('Fourth Plot')
        plt.show()
        '''
    # Write the PDF document to the disk
    pdf_pages.close()
    print("save successful! \nto view, please see at:" + os.path.abspath(fdfName))
    # How to use:
    #   history = model.fit(x_data, y_data, epochs=5000,verbose=1)
    #   plotHistory(history)

# plotHistory(history)    
# exit()


#########################
try:
    from termcolor import colored
except:
    def colored(inp,color):
        return inp

def similar(a, b):
    return SequenceMatcher(None, a, b)

def HTMLcolored(txt, color):
    return '<font color="%s">%s</font>' % (color, txt)

def HTML_FileHeader():
    return "<!DOCTYPE html> <html> <head></head> <body>"

def HTML_FileFooter():
    return "</body></html>"

def HTML_popen():
    return '<p style="font-size:16px; font-family: monospace;">'

def HTML_pclose():
    return ' </p>'

def TA_calculate_Diff(html_name='',sFilename='', APP='', Org='', skq='',writeType='a'):
    if Org == '':
        APP = '一九九三年二月二十战日上午四川从月县安源乡五村彭家公嫂无人进成更止衣服'
        Org = '一九九三年二月二十三日上午四川省安岳县岳源乡五村彭家姑嫂五人进城购置衣服'

    s = SequenceMatcher(None, Org, APP)
    accPercent=round(s.ratio()*100,3)
    
    last = 0;sta = [];stb = [];lab = []
    sa = list(Org)
    sb = list(APP)
    for m in reversed(s.get_matching_blocks()):
        sta.append(m[0])
        stb.append(m[1])
        lab.append(m[2])

    s0 = list(Org)
    sa = list(Org)
    for l, k in zip(sta, lab):
        for vt in range(l, l + k):
            sa[vt] = '﹂'

    sb0 = list(APP)
    sb = list(APP)
    for l, k in zip(stb, lab):
        for vt in range(l, l + k):
            sb[vt] = '﹂'
    maxlen = max(len(sa), len(sb))
    # So sánh, tìm từ đầu đến chỗ khác nhau:
    #    bên nào là dấu ﹂ thì đẩy ra, cho đến khi giống nhau.
    #    lặp lại từ vị trí kế  tiếp.
    def INS(ss,k):
        b = ss[:];
        b[k:k] = ['﹏'];
        ss = b[:];
        return ss
    k = 0
    flag=1

    while flag == 1:
        la=len(sa)
        lb=len(sb)
        lmin=min(la,lb)
        while (k<lmin) and (sa[k] == sb[k]): k += 1
        if (k<lmin) and (sa[k] != sb[k]):
            if (sa[k] == '﹂'):  # insert
                sa = INS(sa,k)

            if (sb[k] == '﹂'):  # insert
                sb = INS(sb,k)

        k+=1
        if k >= len(sa) or k >= len(sb): flag = 0

    k = 0
    sa1 = sa[:]
    for i, ch in enumerate(sa):
        if (ch != '﹏'):
            sa1[i] = s0[k]
            k += 1
    #######################################3
    sa4 = sa1[:]
    for i, ch in enumerate(sa1):
        if ch == '﹏': sa4[i] = HTMLcolored(sa1[i], 'white')
    sa3 = sa[:]
    for i, ch in enumerate(sa):
        if ch != '﹂': sa3[i] = HTMLcolored(sa[i], 'blue')
        if ch == '﹏': sa3[i] = HTMLcolored(sa[i], 'white')
    sb3 = sb[:]
    for i, ch in enumerate(sb):
        if ch != '﹂':
            sb3[i] = HTMLcolored(sb[i], 'red')
    ##########################################
    k = 0
    sb1 = sb[:]
    for i, ch in enumerate(sb):
        if (ch != '﹏'):
            sb1[i] = sb0[k]
            k += 1

    for i, ch in enumerate(sa):
        if ch == '﹏': sa[i] = colored(sa[i], 'grey')
        if ch != '﹂': sa[i] = colored(sa[i], 'blue')

    for i, ch in enumerate(sb):
        if ch != '﹂':
            sb[i] = colored(sb[i], 'red')

    kq = []
    kq.append('ORG=' + ''.join(sa1))
    kq.append('ORG='+''.join(sa))
    kq.append('APP=' + ''.join(sb))
    kq.append('APP='+''.join(sb1))

    shtml = HTML_FileHeader()
    sout = HTMLcolored('ORG=' + ''.join(sa4),'green') + '<br/>'
    sout+='ORG='+''.join(sa3)+'<br/>'
    sout += 'APP=' + ''.join(sb3) + '<br/>'
    sout+='APP='+''.join(sb1)+'<br/><br/>'
    sout+='Acc of this sentence: {} %'.format(accPercent)
    
    shtml_end = HTML_pclose()
    shtml_end += HTML_FileFooter()
    #if not os.path.exists(home + '/tmp/'): os.path.makedirs(home + '/tmp/')
    with open(html_name, writeType)as f:
        f.write(HTML_popen())
        f.write(sFilename + '<br/>')
        f.write(sout)
        f.write(skq + '<br/>')
        f.write(HTML_pclose())

    # print(colored('hello', 'red'), colored('world', 'green'))
    # print(colored("hello red world", 'red'))
    return shtml, sout, shtml_end, kq

def test():
    sFilename = "1.wav :"
    APP = "一九九三年二月二十三日上午川着安月线安人乡五村彭家公嫂无人进成更置一服"
    Org = "一九九三年二月二十三日上午四川省安岳县岳源乡五村彭家姑嫂五人进城购置衣服"
    kq = "xxx%"
    TA_calculate_Diff(sFilename, APP, Org, kq,writeType='w')

    sFilename = "2.wav :"
    APP = "看羊狗跑前跑后一只惊飞的山雀︾︵︵︵︶︶︸︾︾︽︽﹏﹏﹏﹏热得他王望汪咬几声嗡嗡嗡的在山间回荡"
    Org = "看羊狗跑前跑后一只惊飞的山雀惹得它汪汪汪咬几声嗡嗡嗡的在山间回荡"
    kq = "xxx%"
    TA_calculate_Diff(sFilename, APP, Org, kq)

    sFilename = "3.wav :"
    APP = "飞机穿过运层眼下一挺云害有十透过稀薄的棉物一稀可进南国冲绿的群山大地"
    Org = "飞机穿过云层眼下一片云海有时透过稀薄的云雾依稀可见南国葱绿的群山大地"
    kq = "xxx%"
    TA_calculate_Diff(sFilename, APP, Org, kq)

    sFilename = "4.wav :"
    APP = "王英汉北枪病后部肥雨孽生产起来几次维部均未抓获"
    Org = "王英汉被枪毙后部分余孽深藏起来几次围捕均未抓获"
    kq = "xxx%"
    TA_calculate_Diff(sFilename, APP, Org, kq)

    sFilename = "5.wav :"
    APP = "其中有些然远本育陈去澜关系不错早她转磨银怕要求不看森便看佛面"
    Org = "其中有些人原本与陈曲澜关系不错找他软磨硬泡要求不看僧面看佛面"
    kq = "xxx%"
    TA_calculate_Diff(sFilename, APP, Org, kq)

    sFilename = "A2_6.wav :"
    APP = "久举闹市常常忘了山之外水之外外外外身之外还有沃野平畴还有光外外外风丽日日风丽风丽"
    Org = "久居闹市常常忘了山之外水之外身之外还有沃野平畴还有光风丽日"
    kq = "xxx%"
    #TA_calculate_Diff(sFilename, APP, Org, kq)

    shtml, sout, shtml_end, kq = TA_calculate_Diff(sFilename, APP, Org, kq)
    for s in kq:
        print(s)

'''
data = {'Wav_path':path2Data,
        'fnFeature_out':fnFeature_out
        'Max_len_label_no_space':Max_len_label_no_space,
        'Max_len_MFCC'          :maxlen
        }
'''
                        
def fnSave2Json(path,data):
    with io.open(path, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,indent=4, sort_keys=True,separators=(',', ':'), ensure_ascii=False)
        outfile.write(str_)
#with open(path) as data_file:data_loaded = json.load(data_file)
#print(data_loaded['Wav_path'])




##########################













