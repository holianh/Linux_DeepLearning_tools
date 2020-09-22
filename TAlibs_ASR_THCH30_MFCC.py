from pprint import pprint as pp
from itertools import islice
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import pickle
from os.path import exists
import shutil
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', autosize = True):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        autosize    - Optional  : automatically resize the length of the progress bar to the terminal window (Bool)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    styling = '{} |{}| {} {}: {}/{}' .format(prefix, fill, percent, suffix,iteration,total)
    if autosize:
        cols, _ = shutil.get_terminal_size(fallback = (length, 1))
        length = cols - len(styling)
        
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength) 
    
    print('\r{}'.format(styling.replace(fill, bar)), end = '', flush=True) 
    if iteration==total:print()
import sys
def print_first_n_dict(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])    
    return size
# print("TAlibs_getsize.py")    
# print("var=get_size(THCH30) ")
get_size(THCH30),    
class THCH_Data_PreProcessing():
    def __init__(self, datahome, BackupPath='/content/drive/My Drive/Deeplearning/ASR_dataset/THCHs30', nMax=-1, force_recreate_data=False):
        """datahome='data_thchs30'
            nMax: Maximum sample process, using for debug if nMax>0
        """     
        if not exists(BackupPath): 
            raise Exception(f'BackupPath={BackupPath} Không tồn tại, đề nghị cấp đúng đường dẫn!')
        self.Dev_Xs  ={}
        self.Test_Xs ={}
        self.Train_Xs={}
        self.nMax=nMax
        self.datahome=datahome
        self.BackupPath=BackupPath
        if not exists(f'{BackupPath}/Dev_Xs.pickle') or force_recreate_data:
            pTrain_wav=f'{datahome}/thchs30/train.wav.lst'
            pTrain_lbl=f'{datahome}/thchs30/train.syllable.mandarin.txt'
            self.ind_Train_wav=self.Read_wav_path(pTrain_wav)
            ind_Train_lbl     =self.Read_Label_path(pTrain_lbl)

            pTest_wav=f'{datahome}/thchs30/test.wav.lst'
            pTest_lbl=f'{datahome}/thchs30/test.syllable.mandarin.txt'
            self.ind_Test_wav=self.Read_wav_path(pTest_wav)
            ind_Test_lbl     =self.Read_Label_path(pTest_lbl)

            pDev_wav=f'{datahome}/thchs30/dev.wav.lst'
            pDev_lbl=f'{datahome}/thchs30/dev.syllable.mandarin.txt'
            self.ind_Dev_wav=self.Read_wav_path(pDev_wav)
            ind_Dev_lbl     =self.Read_Label_path(pDev_lbl)

            self.word2ind, self.ind2word = self.ind_word([ ind_Train_lbl,ind_Test_lbl,ind_Dev_lbl ])

            self.Dev_lbl  =self.idx_Labelling(ind_Dev_lbl  , self.word2ind)
            self.Test_lbl =self.idx_Labelling(ind_Test_lbl , self.word2ind)
            self.Train_lbl=self.idx_Labelling(ind_Train_lbl, self.word2ind)
        else:
            self.LoadAll()
    def Read_wav_path(self,fn):
        """ Đọc hết wav id và path vào ind. Cấu trúc file txt: fileid path"""
        n=0
        ind={}
        with open(fn) as ff:
            for line1 in ff:
                line1=line1.strip()
                id,txt=line1.split()
                ind[id]=f'{self.datahome}/{txt}'                
                if self.nMax>0:
                    if n<self.nMax:n+=1
                    else: break
        print('Read_wav_path done!', fn)
        return ind
    # ret=Read_wav_path('data_thchs30/thchs30/train.wav.lst')
    # pp(ret)

    def Read_Label_path(self,fn):
        ''' file txt label có dạng: fileid w w w w ww w (với w là word, cách nhau bởi dấu cách, mỗi fileid 1 dòng) '''
        n=0
        ind={}
        with open(fn) as ff:
            for line1 in ff:
                line1=line1.strip()
                id,*txt=line1.split(' ')
                ind[id]=txt
                if self.nMax>0:
                    if n<self.nMax:n+=1
                    else: break
        print('Read_Label_path done!',fn)
        return ind
    # ind =Read_Label_path('data_thchs30/thchs30/train.syllable.mandarin.txt')

    def ind_word(self,args):
        """Inp:[d1,d2,d3], All dictionary of texts: {txt-id:[values],...}"""
        Ws=sorted(list( set([w  for d in args for L in d.values() for w in L]) ))
        word2ind={w:k+1 for k,w in enumerate(Ws)}
        ind2word={k+1:w for k,w in enumerate(Ws)}
        print('ind_word done!')
        return word2ind, ind2word
    # ind_word([ind_train_lbl,ind_test_lbl,ind_dev_lbl])

    def idx_Labelling(self,ind, word2ind):
        d={}
        for key,value in ind.items():
            v2=[word2ind[it] for it in value]
            d[key]=v2
        print('idx_Labelling done!')
        return d
    def MFCC_1dict(self,dict1):
        N=len(dict1)
        Dev_Xs={}
        for cnt, (key, value) in enumerate(dict1.items()):  # 'A11_124': 'data_thchs30/dev/A11_124.wav',
            (rate,sig) = wav.read(value)
            Dev_Xs[key]=mfcc(sig,rate)
            printProgressBar(cnt+1,N)
        return Dev_Xs
    def Feature_gen(self,Ftype='MFCC'):
        self.Dev_Xs  =self.MFCC_1dict(self.ind_Dev_wav)
        self.Test_Xs =self.MFCC_1dict(self.ind_Test_wav)
        self.Train_Xs=self.MFCC_1dict(self.ind_Train_wav)
        print('Feature_gen done!')
        
    def SaveAll(self):  
        p=self.BackupPath      
        with open(f'{p}/Dev_Xs.pickle', 'wb')   as f: pickle.dump(self.Dev_Xs, f, pickle.HIGHEST_PROTOCOL)
        with open(f'{p}/Test_Xs.pickle', 'wb')  as f: pickle.dump(self.Test_Xs, f, pickle.HIGHEST_PROTOCOL)
        with open(f'{p}/Train_Xs.pickle', 'wb') as f: pickle.dump(self.Train_Xs, f, pickle.HIGHEST_PROTOCOL)        
        with open(f'{p}/word2ind.pickle', 'wb')  as f: pickle.dump(self.word2ind, f, pickle.HIGHEST_PROTOCOL)
        with open(f'{p}/ind2word.pickle', 'wb')  as f: pickle.dump(self.ind2word, f, pickle.HIGHEST_PROTOCOL)
        with open(f'{p}/Dev_lbl.pickle', 'wb')   as f: pickle.dump(self.Dev_lbl, f, pickle.HIGHEST_PROTOCOL)
        with open(f'{p}/Test_lbl.pickle', 'wb')  as f: pickle.dump(self.Test_lbl, f, pickle.HIGHEST_PROTOCOL)
        with open(f'{p}/Train_lbl.pickle', 'wb') as f: pickle.dump(self.Train_lbl, f, pickle.HIGHEST_PROTOCOL)
        
        with open(f'{p}/THCH30_Huong_dan.txt', 'w')    as f:
            f.write('Dev_Xs.pickle, Test_Xs.pickle and Train_Xs.pickle co cau truc:\n')
            f.write('dictionary: key:value, voi key= file-id, value= python_speech_features.mfcc\n\n')

            f.write('word2ind, ind2word: dict, convert word 2 index va nguoc lai:\n\n')
            f.write('*_lbl, dictionary: key:value, voi key= file-id, value= label numbers belong to word2ind\n')
        print('Data Saved!',p)

    def LoadAll(self):  
        p=self.BackupPath  
        with open(f'{p}/Dev_Xs.pickle', 'rb')   as input_file: self.Dev_Xs=pickle.load(input_file)
        with open(f'{p}/Test_Xs.pickle', 'rb')  as input_file: self.Test_Xs=pickle.load(input_file)
        with open(f'{p}/Train_Xs.pickle', 'rb') as input_file: self.Train_Xs=pickle.load(input_file)
        with open(f'{p}/word2ind.pickle', 'rb')  as input_file: self.word2ind=pickle.load(input_file)
        with open(f'{p}/ind2word.pickle', 'rb')  as input_file: self.ind2word=pickle.load(input_file)
        with open(f'{p}/Dev_lbl.pickle', 'rb')   as input_file: self.Dev_lbl=pickle.load(input_file)
        with open(f'{p}/Test_lbl.pickle', 'rb')  as input_file: self.Test_lbl=pickle.load(input_file)
        with open(f'{p}/Train_lbl.pickle', 'rb') as input_file: self.Train_lbl=pickle.load(input_file)
        print('Data loaded! from',p)
print("""
datahome='data_thchs30'
THCH30=THCH_Data_PreProcessing(datahome=datahome,nMax=-1,force_recreate_data=False)
""")
