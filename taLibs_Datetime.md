# Date time +7 Vietnam time

```python
import dateutil, datetime
import dateutil.tz
def tt(): return datetime.datetime.now(dateutil.tz.tzoffset(None, 7*60*60)) 
stime=tt().strftime('%Y-%m-%d  %H:%M:%S')   #'2020-02-23  00:08:27' 
stime
```

# Class Running time, waiting time

```python
from datetime import datetime
import time
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', autosize = False):
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
    styling = '%s |%s| %s%% %s' % (prefix, fill, percent, suffix)
    if autosize:
        cols, _ = shutil.get_terminal_size(fallback = (length, 1))
        length = cols - len(styling)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s' % styling.replace(fill, bar), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

# Lớp này dùng để tính thời gian đã chạy và phải đợi đến khi chạy xong.
# Vào: nếu có Ntotal (tổng số vòng sẽ lặp) thì in ra sẽ có time chờ
class TAtimming():
    def __init__(self, Ntotal=0): # Tổng số cần chạy
        self.cnt=0
        self.Ntotal=Ntotal
        self.start=datetime.now()        
    # def restart(self, Ntotal=0):
    #     self.cnt=0
    #     self.Ntotal=Ntotal
    #     self.start=datetime.now()
    def update(self, npass=0, return_cnt=False):     
        """ input:
                npass: Đã chạy được, mặc định là 1
            output: 
                [TRan]: time đã chạy
                [TRan,Twait]: nếu Ntotal>0
                [TRan,...,cnt]: nếu return_cnt=True 
        """
        self.cnt+=1+npass         
        if npass>0: self.cnt+=npass-1  
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

#use:
mydir="Data"; Ntotal=TA_Count(mydir)
taTime=TAtimming(Ntotal) # or ta=TAtimming()
printProgressBar(0, Ntotal, prefix = 'Progress:', suffix = 'Complete', autosize = True)
# .........................................................
k=0
for D,_,F in os.walk('Data'):
    for fn in F:
        if fn.endswith('.jpg'):
            # ............ your code .......................
            k+=1
            if k%10==0:
                TRan, Twait,cnt=taTime.update(npass=k,return_cnt=True)
                printProgressBar(cnt, Ntotal, prefix = 'Progress:', suffix = 'Complete! (T.ran:{} - T.wait={})'.format(TRan, Twait), autosize = True)
                k=0


```

# Running time, waiting time:

```python
from datetime import datetime
import time
# Init:----------------------------------------
Ntotal=10    # Tổng số cần chạy
cnt=0
start=datetime.now()

#Your statements: -----------------------------
time.sleep(2.4)

# Display timing:------------------------------
cnt+=1         # Đã chạy được
TRan=datetime.now()-start
Twait=((Ntotal-cnt)/cnt)*TRan
#print(f'TRan:{str(TRan)[:-7]}-Twait:{str(Twait)[:-7]}')
print(f'Cnt:{cnt}, loss:{cnt:>0.4f}  TRan:{str(TRan)[:-7]}-Twait:{str(Twait)[:-7]}')
```
