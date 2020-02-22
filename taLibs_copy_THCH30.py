import glob, shutil
import os
from os.path import join, exists
def startCopy_models(source,dest):
    if not exists(dest): os.makedirs(dest)
    files = glob.glob(os.path.join(dest,"*"))
    for f in files: os.remove(f)            
    for file in glob.glob(os.path.join(source,"*.*")):
        shutil.copy2(file,dest)
def fn_copy_data_thchs30():
    if not os.path.exists("/content/data_thchs30"):
        # !cp "/content/drive/My Drive/Deeplearning/thch30_train_dev_test.zip"  "thch30_train_dev_test.zip" 
        print("Copy thch30_train_dev_test.zip to colab:")
        fnsrc="/content/drive/My Drive/Deeplearning/thch30_train_dev_test.zip"
        os.system('rsync --info=progress2 "{}"  "./thch30_train_dev_test.zip" '.format(fnsrc))
        
        print('finshed copy!\nUnzip...:')
        #!unzip -qq thch30_train_dev_test.zip
        os.system('unzip -o thch30_train_dev_test.zip -d /. | pv -l >/dev/null')
        os.system('mv content/* .')
        #os.system('rm -d content')
        shutil.rmtree('content')         
        os.remove('rm thch30_train_dev_test.zip')
        
if __name__ == '__main__':
    print("run taLibs_copy_THCH30.py file")
    fn_copy_data_thchs30()
'''
How to use?

import os
os.system('rm -rf taLibs_copy_THCH30.*')  
!wget -q https://github.com/holianh/Linux_DeepLearning_tools/raw/master/taLibs_copy_THCH30.py  
!ls -la -h taLibs*
import taLibs_copy_THCH30 as datathch30
# datathch30.fn_copy_data_thchs30()

'''
