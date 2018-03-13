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

import timeit
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
tWait=format_seconds_to_hhmmss(math.trunc(((Max_samples-k)*total_time)/k))

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
    vt1=-1
    vt2=-1
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



            
