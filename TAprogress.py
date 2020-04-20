
from datetime import datetime
import time,shutil
#from sklearn.model_selection import train_test_split
#from keras.utils import to_categorical
#import numpy as np
import os 
from os.path import join,exists
os.system("clear")
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
    

# Lớp này dùng để tính thời gian đã chạy và phải đợi đến khi chạy xong.
# Vào: nếu có Ntotal (tổng số vòng sẽ lặp) thì in ra sẽ có time chờ
class TAtimming():
    def __init__(self, Ntotal=0): # Tổng số cần chạy
        self.cnt=0
        self.Ntotal=Ntotal
        self.start=datetime.now()        
    def update(self, npass=0, return_cnt=False):     
        """ input:
                npass: Đã chạy được, mặc định là 1
            output: 
                [TRan]: time đã chạy
                [TRan,Twait]: nếu Ntotal>0
                [TRan,...,cnt]: nếu return_cnt=True 
        """
        self.cnt+=1+npass         
        TRan=datetime.now()-self.start
        Twait=((self.Ntotal-self.cnt)/self.cnt)*TRan
        rent=[TRan]
        if self.Ntotal>0: rent+=[Twait]
        if return_cnt:  rent+=[self.cnt]
        return rent
        
    def print(self,npass=0):
        TRan=self.update(npass)
        if self.Ntotal>0: 
              print("T.ran:{} - T.wait:{}".format(TRan[0], TRan[1]))
        else: print("T.ran:{}".format(TRan))
def TA_Count(mydir):
    cnt=0
    for D,_,F in os.walk(mydir): cnt+=len(F)
    return cnt
taTime=TAtimming(Ntotal) # or ta=TAtimming()
printProgressBar(0, Ntotal, prefix = 'Progress:', suffix = 'Complete', autosize = True)



exts=['.jpg','.bmp']

mydir='Dataset/NoHand'; Ntotal=TA_Count(mydir)

for D,_,F in os.walk(mydir):
    for fn in F:
        if fn[-4:] in exts:
            ffn=join(D,fn);             
            #..............................
            #..............................
            # do sth:
            
            #..............................
            #..............................
            
            TRan, Twait,cnt=taTime.update(return_cnt=True)
            printProgressBar(cnt, Ntotal, prefix = 'Progress:', suffix = 'Complete! (T.ran:{} - T.wait={})'.format(TRan, Twait), autosize = True)


