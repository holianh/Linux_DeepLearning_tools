'''
Nguyen Tuan Anh, 2018-01-19
usful python functions
--------------------------
'''
########################################################################
# dirs / files --------------------------------------------------
########################################################################
import io, json
data = {'DataHome':DataHome,
        'Wav_path':Wav_path,
        'DataPath':Wav_path
        }
with io.open(pproject_info, 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,indent=4, sort_keys=True,separators=(',', ':'), ensure_ascii=False)
    outfile.write(str_)
#uses:
#with open(pproject_info) as data_file:data_loaded = json.load(data_file)
#print(data_loaded['DataPath'])
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




            

