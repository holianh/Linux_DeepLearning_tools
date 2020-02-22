# %%writefile Copy_THCH30_From_GoogleDrive_2_Local.py
Colab=True
import shutil
import os
os.system('apt install pv')
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# if not os.path.exists("/content/DeepSpeechRecognition"):
#   !git clone https://github.com/audier/DeepSpeechRecognition.git
#   !git clone https://github.com/zw76859420/ASR_Syllable.git

#-------------------------------------------------------------------------------
import zipfile
from tqdm import tqdm
def taLibs_Unzip_progress(src='thch30_train_dev_test.zip', target_path='.'):
  with zipfile.ZipFile(src) as zf:
      for member in tqdm(zf.infolist(), desc='Extracting '):
          try:
              zf.extract(member, target_path)
          except zipfile.error as e:
              pass

#-------------------------------------------------------------------------------
import glob, shutil
import os
from os.path import join, exists
def startCopy_models(source,dest):
    if not exists(dest): os.makedirs(dest)
    files = glob.glob(os.path.join(dest,"*"))
    for f in files: os.remove(f)            
    for file in glob.glob(os.path.join(source,"*.*")):
        shutil.copy2(file,dest)

#-------------------------------------------------------------------------------
def fn_copy_data_thchs30():
  if not os.path.exists ('/content/drive'):
    from google.colab import drive
    drive.mount('/content/drive')
  if not os.path.exists("/content/data_thchs30"):
      print("start copy thch30_train_dev_test to local...")      
      ! rsync --progress "/content/drive/My Drive/Deeplearning/thch30_train_dev_test.zip"  .     
      taLibs_Unzip_progress(src='thch30_train_dev_test.zip', target_path='.')
      for file in glob.glob("./content/*"): shutil.move(file,dest)
      os.remove('thch30_train_dev_test.zip')
  print("Done copy data")
#-------------------------------------------------------------------------------
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
