'''
Nguyen Tuan Anh, 2018-01-19
usful python functions
--------------------------
'''
########################################################################
# Extract N end lines contain "Key to find" from files  ----------------
########################################################################
def LastNlines(NLs=15,LineContainKey="Key to Fine"):
    #lss=glob.glob(clayPath+"*.txt")
    #newestFileindir = max(lss, key=os.path.getctime)
    newestFileindir ="/Path/to/file.txt"
    #print(newestFileindir)
    f = open(newestFileindir, 'rb'); strData = f.read().decode('utf8', 'ignore')
    
    data=strData.split('\n')
    Ndata=len(data)
    print('Ndata=',Ndata)
    Lines=[]
    NumberLine=0
    flag=True
    while flag:
        if NumberLine==NLs:
            return Lines
        if(data[Ndata-1].find(LineContainKey)>0):
            Lines.append(data[Ndata-1])
            NumberLine+=1
        if(Ndata>1):
            Ndata=Ndata-1
        else:
            return Lines
#Liness=LastNlines() 
#for s in Liness:print(s)
#exit()
    

########################################################################
# Plot history and accuray when training with Keras to PDF -------------
########################################################################
import matplotlib                                    ###############
matplotlib.use('agg')
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages

def hist(history,
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
          fdfName='history_training.pdf'
         ):
    # Plot history of training in keras to pdf
    # history=model.fit(...) in keras
    # history={'loss':[1,2,3,...n],'acc':[1,2,3,...,m]}
    # strNeedPlot=('loss','acc','loss','acc','loss')

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
        
        ax.set_title(Labels[i][0])
        plt.xlabel(Labels[i][1], fontsize=14)
        plt.ylabel(Labels[i][2], fontsize=14)
        
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
    print(fdfName + " - already save successful!")
    print("to view, please see at:" + os.getcwd())
    # How to use:
    #   history = model.fit(x_data, y_data, epochs=5000,verbose=1)
    #   hist(history)

# hist(history)    
# exit()

########################################################################
# Save data to json file -----------------------------------------------
########################################################################
FnSave='test.txt'
import io, json
data = {'DataHome':DataHome,
        'Wav_path':Wav_path,
        'DataPath':Wav_path
        }
with io.open(FnSave, 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,indent=4, sort_keys=True,separators=(',', ':'), ensure_ascii=False)
    outfile.write(str_)
#uses:
#with open(FnSave) as data_file:data_loaded = json.load(data_file)
#print(data_loaded['DataPath'])
#import pprint
#pprint.pprint(data_loaded)
########################################################################

########################################################################
# Files_2csv_inDir -----------------------------------------------------
# Find and Add All wav & label files to *.CSV
########################################################################
import os
from random import shuffle
Wav_path='/home/tact/AudioDBs/All_DataBase/'#
sNeedRemove='/home/tact/AudioDBs/All_DataBase' # loại bỏ đường dẫn dư thừa.
# .....
#--------------- --------------- --------------- ---------------
def Files_2csv_inDir(path, wav_ext, lbl_ext):
    count = 0
    Fis=[]
    for subdir, dirs, files in os.walk(path):
        for fi in files:
            if fi.endswith(wav_ext): # eg: '.txt'
                count += 1
                ph=subdir.replace(sNeedRemove,'')
                Fis.append(ph+'/'+fi)
    shuffle(Fis)
    Full_len=len(Fis)
    train_len= round(Full_len * 0.8)
    test_len = Full_len - train_len
    
    print(train_len,test_len)
    fn=open(csv_path+'data_train_path.csv','w')
    ft=open(csv_path+'data_test__path.csv','w')
    
    k=0
    for item in Fis:
        k+=1
        if(k<train_len): fn.write("%s\n" % item)
        else:            ft.write("%s\n" % item)
    fn.close()
    ft.close()
    return count
''' #--------------- --------------- --------------- ---------------
/home/tact/ta/asr_ta_2018_01/info
|===data_test__path.csv
        /home/tact/AudioDBs/All_DataBase/tadb106/BAC009S0059W0246.wav
        /home/tact/AudioDBs/All_DataBase/tadb128/BAC009S0663W0453.wav
        /home/tact/AudioDBs/All_DataBase/tadb169/BAC009S0745W0291.wav
|===data_train_path.csv
'''
########################################################################
# Timing ------------ ------------------- ------------------- ---------
# Calculate running time 
########################################################################

import timeit,math
start = timeit.default_timer()  # Start counting time
#--------------- --------------- --------------- ---------------
def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)
#--------------- --------------- --------------- ---------------

 # Stop counting time, make a time string to print out to screen
stop = timeit.default_timer()
total_time=stop-start # in seconds
tRan=format_seconds_to_hhmmss(math.trunc(total_time))
print(tRan)
#tWait=format_seconds_to_hhmmss(math.trunc(((Max_samples-k)*total_time)/k))

########################################################################
# post (upload) file/string to PHP webpage
##########################################################################    
#import datetime
#import requests
#tenmay="/path/to/file/will/upload.txt"
#LastNlines(): function to get last n line with keyword of file.
# replace 'xxxxxxxx' to real path on server
t=0
def Upload2Server():
        global t
    #try:
        with open(tenmay,'r') as f: ND=f.read();
        tgian=datetime.datetime.now()
        sTgian=str(tgian).split('.')[0].replace(':','-')
        ND=ND+sTgian+'\n\r'
        Liness=LastNlines() 
        for s in Liness:
            ND=ND+s
        
        r = requests.post("http://anh.000webhostapp.com/xxxxxxxx/index.php?machineName="+tenmay+'&contents='+ND)
        print('upload:',r.status_code, r.reason)
        t+=1
    #except:
    #    print ('Upload status errors')
#uses: Upload2Server()
#exit()

########################################################################
# Run a system Ubuntu command:
##########################################################################    
def runCMD(sudopass,cmd):
    os.system('echo '+sudopass+' | sudo -S '+cmd)
########################################################################
# Substring: Copy contends from txt file, add string of time, add 
# substring from 1st '\n' to 3nd '\n' add
# text from run system command line then
# write al to text file.
##########################################################################    
''' 
string input:
PING bing.com (13.107.21.200) 56(84) bytes of data.\n
64 bytes from 13.107.21.200: icmp_seq=1 ttl=108 time=12.1 ms\n
64 bytes from 13.107.21.200: icmp_seq=2 ttl=108 time=11.9 ms\n
64 bytes from 13.107.21.200: icmp_seq=3 ttl=108 time=13.4 ms\n\n

--- bing.com ping statistics ---\n
3 packets transmitted, 3 received, 0% packet loss, time 2003ms\n
rtt min/avg/max/mdev = 11.964/12.509/13.465/0.689 ms\n

Copy from first '\n' to third '\n', result:
string output:
64 bytes from 13.107.21.200: icmp_seq=2 ttl=108 time=12.0 ms\n
64 bytes from 13.107.21.200: icmp_seq=3 ttl=108 time=12.3 ms
Some extra: 
tenmay='/path/to/file/to/add.txt'
''' 
def MinutelyAction_mm():
    fntxt=open(tenmay,'w')  
    fntxt.write('May:'+tenmay+'\n')
    fntxt.write(("%s"%datetime.datetime.now()).split('.')[0])
    S = os.popen("ping bing.com -c 3").read();
    vt1=-1;    vt2=-1
    pos=0
    k=0
    for s in S:
        k+=1
        if s=="\n":pos+=1
        if pos==1: vt1=k+1
        if pos==3: vt2=k
    S=S[vt1:vt2]        
    fntxt.write(S+'\n')
    Stmp = os.popen("nvidia-smi --format=csv,noheader --query-gpu=index,name,temperature.gpu,fan.speed,pstate,power.draw,clocks.current.graphics").read();
    fntxt.write(Stmp+'\n\n')
    fntxt.close() 
########################################################################
# Get date time, month, day, hour, minute,...
##########################################################################    
import datetime
now = datetime.datetime.now()
print (now.year,'-', now.month,'-', now.day,'   ', now.hour,':', now.minute,':', now.second)

########################################################################
# Move, Copy, delete file from Python
##########################################################################    
import shutil
import os
def MoveFile2Folder(fileNeed2move,dest_dir):
    if not os.path.exists(dest_dir):os.makedirs(dest_dir)
    shutil.copy2(fileNeed2move, dest_dir)
    
    if os.path.exists(fileNeed2move):
        try:
            os.remove(fileNeed2move)
        except PermissionError as exc:
            os.chmod(fileNeed2move, stat.S_IWUSR)
            os.remove(fileNeed2move)


########################################################################
# Delay, sleep in python
##########################################################################    
import time
time.sleep(60) # in second

########################################################################
# Pass arguments to program, call commandline args
##########################################################################    
import sys;
for arg in sys.argv[1:]:  
  #try:
    nam=arg.split('=')[0]
    val=arg.split('=')[1]
    print(nam,':',val)
    if(nam=='Client_ID'):        Client_ID     =val
    elif (nam=='Nbatch_size'):   Nbatch_size   =int(float(val)) #int
    elif (nam=='Nepochs'):       Nepochs       =int(float(val)) #int
    elif (nam=='path2_npyData'): path2_npyData =val
    elif (nam=='noGPU'):         os.environ["CUDA_VISIBLE_DEVICES"]=val
    else:
        print('')
        print("Can't recognize name of parameter:",arg)
        print("Calling examples:")
        print("python Client_train_GPU.py 'Client_ID=1080ti-3' noGPU=3 'path2_npyData=/path/to/npy/feature/file.npy' [Nepochs=32] [Nbatch_size=64]")
        print('------------------------------------------------------------------')
  #except:
  #  print("err:",arg)

###########################################################
# Load json with multiple json lines
###########################################################
def _read_data_json(file_name):
    with open(file_name, 'r') as fid:
        return [json.loads(l) for l in fid]

# use: 
# data_jsons = ['olivia_train.json',...]paths of json files, in each json files can have lines json format
olivia_train.json:
{"duration": 0.7894784580498866, "text": "olivia", "key": "data/olivia_train/1429.wav"}
{"duration": 1.1145578231292517, "text": "olivia", "key": "data/olivia_train/1430.wav"}
{"duration": 1.253877551020408, "text": "olivia", "key": "data/olivia_train/1431.wav"}

data = []
for dj in data_jsons:
    data.extend(_read_data_json(dj))
data = sorted(data, key=lambda x : x['duration'])


###########################################################
# Make model run in Multiple GPUs
###########################################################
#input: model: model already create before using, like this:
with tf.device('/device:CPU:0'):
    mfcc_input=np.load(fileDB); #print(mfcc_input.shape[1],mfcc_input.shape[2]);exit()
    input_tensor=Input(shape=(mfcc_input.shape[1],mfcc_input.shape[2]));
    x=Conv1D(kernel_size=1,filters=192,padding="same")(input_tensor);
    x=BatchNormalization(axis=-1)(x);
    x=Activation("tanh")(x);
    # -----------------------------------------------------------------------------------
    def res_block(x,size,rate,dim=192):
        x_tanh=Conv1D(kernel_size=size,filters=dim,dilation_rate=rate,padding="same")(x);
        x_tanh=BatchNormalization(axis=-1)(x_tanh);
        x_tanh=Activation("tanh")(x_tanh);
        x_sigmoid=Conv1D(kernel_size=size,filters=dim,dilation_rate=rate,padding="same")(x);
        x_sigmoid=BatchNormalization(axis=-1)(x_sigmoid);
        x_sigmoid=Activation("sigmoid")(x_sigmoid);
        out=merge([x_tanh,x_sigmoid],mode="mul");
        out=Conv1D(kernel_size=1,filters=dim,padding="same")(out);
        out=BatchNormalization(axis=-1)(out);
        out=Activation("tanh")(out);
        x=merge([x,out],mode="sum");
        return x,out;
    # -----------------------------------------------------------------------------------
    skip=[];
    for i in np.arange(0,1):#3
        for r in [1,2]:#,4,8,16
            x,s=res_block(x,size=7,rate=r);
            skip.append(s);
    skip_tensor=merge([s for s in skip],mode="sum");
    # -----------------------------------------------------------------------------------
    logit=Conv1D(kernel_size=1,filters=192,padding="same")(skip_tensor);
    logit=BatchNormalization(axis=-1)(logit);
    logit=Activation("tanh")(logit);
    logit=Conv1D(kernel_size=1,filters=len(char_index)+1,padding="same",activation="softmax")(logit);
    base_model=Model(inputs=input_tensor,outputs=logit);
    # -----------------------------------------------------------------------------------
logit_length_input =Input(shape=(1,));
y_true_input       =Input(shape=(maxlen_char,));
y_true_length_input=Input(shape=(1,));
loss_out=Lambda(ctc_lambda_function,output_shape=(1,),name="ctc")([y_true_input,logit,logit_length_input,y_true_length_input])
model=Model(inputs=[input_tensor,logit_length_input,y_true_input,y_true_length_input],outputs=loss_out);
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
gpus=4
print("Using %i GPUs" %gpus)
from keras.utils.multi_gpu_utils import  multi_gpu_model 
model = multi_gpu_model(model, gpus=gpus)
#How to parallel_model from normal:
# 1: install update keras to newest: (should do in other envs in conda)
# 2: copy folder: ~/anaconda3/envs/kr/lib/python3.5/site-packages/keras/utils    to current using keras folder:
#                 ~/anaconda3/envs/P3/lib/python3.5/site-packages/keras/utils    (change name of old folder before paste here)
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
model.compile(loss={'ctc': lambda y_true, y_pred: y_pred},optimizer="adam",metrics=['accuracy']);



###########################################################
# Python: Print json file out to screen:
###########################################################

print()
print('########################################################################################################')
print('Start...')
pproject_info='info/project_info.txt'
with open(pproject_info) as data_file:data_loaded = json.load(data_file)
import pprint as pp
pp.pprint (data_loaded)
# ~ for item in data_loaded:print ("{0:<25s} {1}".format(item, data_loaded[item]))
print()


###########################################################
# Python: Many date time, unique file names  
###########################################################
# giờ thật hiện tại là 11:05:20
from time import strftime
stime=strftime("%H:%M:%S")
print('2, ', stime) # 2,  2018-08-31 11:05:20

from datetime import datetime
stime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('1, ', stime) #1,  2018-08-31 11:05:20

from time import gmtime, strftime
stime=strftime("%Y-%m-%d %H:%M:%S", gmtime())
print('2, ', stime) # 2,  2018-08-31 03:05:20

from datetime import datetime
stime=str(datetime.now())
stime1=str(datetime.now())
print('3.1, ', stime)#3.1,  2018-08-31 11:05:20.884790
print('3.2, ',stime1)#3.2,  2018-08-31 11:05:20.884790

fname=str(datetime.now())
replace_from=[' ',':','.']
replace_to  =['_','-','_']
for a,b in zip(replace_from,replace_to):
    fname=fname.replace(a,b)
print('3.3, ',fname)#3.3,  2018-08-31_11-05-20_884790

import time
stime=time.strftime("%F_%T ")
print('4, ', stime)#4,  2018-08-31_11:05:20 

import time
stime=time.strftime("%F_%H%M%S%T")
print('5, ', stime)#5,  2018-08-31_11052011:05:20

from time import strftime
stime=strftime("%m/%d/%Y %H:%M")
print('6, ', stime)#6,  08/31/2018 11:05
 
from datetime import datetime
dt = datetime.now()
dt1 = datetime.now()
print('7.1, ', dt.microsecond)#7.1,  885290
print('7.2, ', dt1.microsecond)#7.2,  885290

import random
print(random.random()) #0.8495695896891915
uniqName=str(random.random()).replace('.','') 
uniqName #08495695896891915

###########################################################
# Python: Padding a vector/matrix enlarge/make bigger
###########################################################
#             ( (Tren, duoi), (trai,phai) )
mfcc_vec=np.pad(mfcc,((0,Max_len_MFCC-len(mfcc)),(0,0)), mode='constant', constant_values=0)
print(mfcc_vec.shape)


###########################################################
# Python: Run ubuntu command without display with subprocess.Popen
###########################################################
def ChangeSpeed(infile, tempo, outfile='ChangeSpeed'):
    import subprocess
    cmd='ffmpeg -i "{}" -filter:a  "atempo={}" "{}" -y'.format(infile,tempo,outfile)
    
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #p = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate() 
    p_status = p.wait()
    
    return output



###########################################################
Python: Compress folders at current folder to tar.gz
###########################################################
import os
import os.path 
import shutil
import datetime as dt
for fi in os.listdir('./'):
    if os.path.isdir(fi):
        print (fi)
        print (dt.datetime.now())
        os.system('tar -zcpf {} {}'.format(fi+'.tar.gz', fi))
        print('Xong ',fi)
        shutil.rmtree(fi)
        print (dt.datetime.now())
        #exit()

        
###########################################################
Python: Padding list 2D:
###########################################################
input:
    SS=[ [5, 6, 7, 8, 30, 31, 1, 3],
         [11, 12, 13, 2, 1, 32],
         [14, 15, 16, 33, 17, 18, 4, 3, 19],
         [20, 2, 21, 22, 23],
         [24, 34, 1, 26, 27]
       ]
outout:
    [[ 5,  6,  7,  8, 30, 31, 1, 3,  0],
     [11, 12, 13,  2,  1, 32, 0, 0,  0],
     [14, 15, 16, 33, 17, 18, 4, 3, 19],
     [20,  2, 21, 22, 23,  0, 0, 0,  0],
     [24, 34,  1, 26, 27,  0, 0, 0,  0]
    ]
pp(SS)
def PaddingList2D(SS):
    MaxCols=max([len(r) for r in SS])
    for k,S in enumerate(SS):
        S += [0] * (MaxCols - len(S))
    return SS
SS=PaddingList2D(SS)
pp(SS)
---------------------------------------------------
a = [[1, 2, 3], 
     [4, 5], 
     [6, 7, 8, 9]]
import numpy as np

b = np.zeros([len(a),len(max(a,key = lambda x: len(x)))])
for i,j in enumerate(a):
    b[i][0:len(j)] = j
a
b        
        
        
        
.
###########################################################
Python: Convert list of 2D array to 3D array:
###########################################################
MFs=np.zeros((len(MFCCs),Max_len_MFCC,20),dtype='float')
for k in range(len(MFCCs)):
    MFs[k]=MFCCs[k]
MFs.shape  



###########################################################
Python: paralell CPUs, tính toán song song
###########################################################

from multiprocessing import Pool
from time import sleep
from sys import exit

def slowly_square(i):
    sleep(1)
    return i*i

def go():
    pool = Pool(8)
    try:
        results = pool.map_async(slowly_square, range(40)).get(9999999)
        for value in results:
            print(value)
        
    except KeyboardInterrupt:
        pool.terminate()
        print "You cancelled the program!"
        sys.exit(1)
    print('Finished!')
if __name__ == "__main__":
    go()
# --------------------------------------------------------------------
if not exists(pSave_test_+'.npz'):
    starttime=strftime("%H:%M:%S")
    Nfiles,files=List_count_file(pPTest)
    files=natsorted(files)
    print('len(files)=',len(files))
    args=[[file,cnt,Nfiles] for cnt,file in enumerate(files)]
    pool = Pool(16)
    try:
        data = pool.map_async(processtest, args).get(9999999) #       data.sort(key=lambda tup: tup[1])  # sorts in place
        X = [data[i][0] for i in range(len(data))]
        X = np.asarray(X)
        fname = [data[i][1] for i in range(len(data))]
        labels = [data[i][2] for i in range(len(data))]
        np.savez(pSave_test_, X=X, fname=fname,labels=labels)
    except KeyboardInterrupt:                ##### doan nay de bam Ctr_C khi muon dung ctrinh, ket hop voi try/except trong processtest
        print ('parent received control-c')
        pool.terminate()
    pool.terminate()
    #--------------------------------------    
    print('Done!')
# --------------------------------------------------------------------
    

###########################################################
Github markdown: auto make table of content:
###########################################################
# Input: ss : copy all content of Github markdown
s='{} [{}]({}#{})  '
mark=['-','*','+','-']
Link2otherPage= '' #'README.md?'

for line in ss.split('\n'):
#     line='# Đại học'
    L=line.strip()
    L1=L
    if L[:1]=='#':
        link=line.lower().replace('#','').replace(':','').replace('?','').replace(',','')
        link=link.strip().replace(' ','-')
        if L1.replace('#','')[:1]=='Đ':
            L1='Đ'
        start=''
        n=0
        for ch in L:
            if n==0:n=1;continue;
            if ch=='#':n+=1;start=start+' '*3;
            if ch!='#':break
        start+=mark[n-1]
        name=line.replace('#','') 
        name=name.strip()
        if link[0]=='đ':
            link='Đ'+link[1:]
        print(s.format(start,name,Link2otherPage, link) )
#     break
print('---')        




###########################################################
Python Notebook parallel CPUs:
###########################################################
with open('util.py','w') as ff:
    ff.write('def binh_phuong(x):return x ** 2')

import multiprocessing as mp
import util
import numpy as np

# a = [1, 2, 3, 4, 5]
a = np.random.rand(2000,3000)
pool = mp.Pool(mp.cpu_count())
r = pool.map(util.binh_phuong, a)
print(len(r))



