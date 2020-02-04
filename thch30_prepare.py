%%writefile /content/data_thchs30/thch30_prepare.py
# run this code in /content/
# Purpose:
#    1. download THCH30 from web to Colab
#    2. Extract
#    save to /content/data_thchs30/thchs30:
#        3. list .wav file: dev.wav.lst:               A11_124 dev/A11_124.wav
#        4. list pingyin  : dev.syllable.txt:          A11_124 ling4 wai4 nv3 dan1 zhong1 guo2 dui4 hai2 you3 han2 jing1 na4 he2 yao2 yan4 ao4 yun4 pai2 ming2 di4 liu4 qi1 wei4 ye3 ke3 yu3 gao1 shou3 yi1 bo2
#        5. list Mandarin : dev.syllable.mandarin.txt: A11_124 另外 女单 中国队 还有 韩晶 娜 和 尧 燕 奥运 排名 第六 七位 也 可 与 高手 一 搏

#--------------------------------------------------------------------------------------

# # Ipython code:
# import os
# if not os.path.exists("data_thchs30"):
#     !wget http://www.openslr.org/resources/18/data_thchs30.tgz
#     !tar zxf data_thchs30.tgz
#     !rm data_thchs30.tgz
#--------------------------------------------------------------------------------------

import os
import shutil
def copyLabels(path="data_thchs30/train"):
    cnt=0
    for d,j,ff in os.walk(path):
        for fn in ff:
            if fn.endswith('.trn'):
                scr="data_thchs30/data/"+fn
                shutil.copy(scr, path) 
                cnt+=1
    print(cnt, path)

copyLabels(path="data_thchs30/train")
copyLabels(path="data_thchs30/dev")
copyLabels(path="data_thchs30/test")

shutil.rmtree('/content/data_thchs30/lm_phone')
shutil.rmtree('/content/data_thchs30/lm_word')
shutil.rmtree('/content/data_thchs30/data')

# !ls -la -h /content/data_thchs30

#--------------------------------------------------------------------------------------
import os
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size
def human(size):
    UNITS = ["B", "KB" , "MB", "GB", "TB"]
    HUMANFMT = "%f %s"
    HUMANRADIX = 1024.
    for u in UNITS[:-1]:
        if size < HUMANRADIX : return HUMANFMT % (size, u)
        size /= HUMANRADIX
    return HUMANFMT % (size,  UNITS[-1])
print(human(get_size()))

#--------------------------------------------------------------------------------------
# import IPython
# !cat "/content/data_thchs30/dev/A11_101.wav.trn"
# IPython.display.Audio("/content/data_thchs30/dev/A11_101.wav")
#--------------------------------------------------------------------------------------

# list train/dev/test files to text
from os.path import join , exists
import codecs,  os

def getFnlist(path):
    FIS=[]
    for D, r, ff in os.walk(path):
        for fn in ff:
            if fn.endswith(".wav"):
                FIS.append(join(D,fn))
    print('getFnlist={:>5} {}'.format(len(FIS),path))
    return FIS

def write2file(my_list, txtPath):
    with codecs.open(txtPath, 'w', encoding='utf-8') as f:
        for item in my_list:
            f.write("%s\n" % item)

pSave    ="data_thchs30/thchs30/"
if not exists(pSave):os.makedirs(pSave)

pTrain   ="data_thchs30/train"
lstTrain =getFnlist(pTrain)
write2file(lstTrain,pSave + "train.txt")

pDev   ="data_thchs30/dev"
lstDev =getFnlist(pDev)
write2file(lstDev,pSave + "dev.txt")

pTest   ="data_thchs30/test"
lstTest =getFnlist(pTest)
write2file(lstTest,pSave + "test.txt")

#--------------------------------------------------------------------------------------

# Prepare labels:
import os
import codecs
from os.path import join 
 
def PrepareLabels(wave_path, save_path="data_thchs30/thchs30/train"): #train/dev/test
    fMand  = codecs.open(save_path + ".syllable.mandarin.txt", "w", encoding="utf-8") 
    fpinyin= codecs.open(save_path + ".syllable.txt", "w", encoding="utf-8")     
    fwav   = open(save_path + ".wav.lst",'w')  
    cnt=0
    for d, r, ff in os.walk(wave_path):
        for fn in ff:
            if fn.endswith(".wav"):
                fID=fn.replace(".wav","")
                with codecs.open(join(d,fn+'.trn'), encoding="utf-8") as lbl: content = lbl.readlines()                     
                fwav.write   ("{} {}".format(fID, save_path.split('/')[-1] +'/'+fn +'\n'))
                fMand.write  ("{} {}".format(fID, content[0] ))
                fpinyin.write("{} {}".format(fID, content[1] ))
                cnt+=1
    print('PrepareLabels={:>5}, wave_path: {:<30}, save to:{}'.format(cnt,wave_path,save_path))
    fMand.close()
    fpinyin.close()
    fwav.close()

PrepareLabels(wave_path="data_thchs30/train", save_path="data_thchs30/thchs30/train" )
PrepareLabels(wave_path="data_thchs30/dev"  , save_path="data_thchs30/thchs30/dev" )
PrepareLabels(wave_path="data_thchs30/test" , save_path="data_thchs30/thchs30/test" )

print("done!")

#--------------------------------------------------------------------------------------
# copy to gdrive:
# !zip -r -qq thch30_train_dev_test.zip /content/data_thchs30/
# !cp "thch30_train_dev_test.zip" "/content/drive/My Drive/Deeplearning"

#--------------------------------------------------------------------------------------

