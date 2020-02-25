# ------------------------------- New ------------------------------------------------
# thisModel_Name='ASR-CN_CTC_tutorial_train_test'
import glob, shutil, os 
from os.path import join, exists

try:
  import gpustat
except:
  os.system("pip install gpustat")
  import gpustat


class ASRutil():
    def __init__(self,thisModel_Name):
        self.SavingDir = "results/{}_results".format(thisModel_Name)
        if exists('/content/sample_data/anscombe.json'):
            Colab=True
            self.SavingDir = "drive/My Drive/Deeplearning/ASR---results/{}_results".format(thisModel_Name)
        if not exists('results'):os.makedirs('results')
    def help(self):
        ss="""
        startCopy_models(source,dest): 
              Remove all files in dest, copy files from source to dest
        load_model(myModel): 
              if Colab: copy from drive 2 local. Load model if esists
        save_model(myModel, comments='',loss=None, save_best_only=True): 
              Save model to 'results' then copy to gdrive
        """
        print(ss)

    def startCopy_models(self,source,dest):
        """Remove all files in dest, copy files from source to dest"""
        if source==dest: return
        if not exists(dest): os.makedirs(dest)
        files = glob.glob(os.path.join(dest,"*"))
        for f in files: os.remove(f)            
        for file in glob.glob(os.path.join(source,"*.*")):
            shutil.copy2(file,dest)

    def load_model(self,  myModel):
        """if Colab: copy from drive 2 local. Load model if esists"""
        filename='results/{}'.format(thisModel_Name)
        if Colab:
            if not exists (filename + '.model') :
                self.startCopy_models(dest = "results", source = self.SavingDir) 
                print("Copy result inner load_model from gdrive to local, done!")
        if exists(filename + '.model'):     myModel.ctc_model.load_weights(filename + '.model')
        if exists(filename + '.model.base'):myModel.model.load_weights(filename + '.model.base')
        if exists(filename + '.loss.npy'):  myModel.loss=np.load(filename + '.loss.npy')

    def save_model(self , myModel, comments='',loss=None, save_best_only=True):
        fnName='results/{}'.format(thisModel_Name)
        if save_best_only:
            if self.minloss < np.mean(loss[-10:]):
                return
        myModel.minloss = np.mean(loss[-10:])
        myModel.ctc_model.save_weights(fnName + '.model')
        myModel.model.save_weights(fnName + '.model.base')
        f = open(fnName + '_steps.txt' , 'a+')           
        f.write(fnName + comments+'\n')
        f.close()
        if loss: np.save(fnName + '.loss.npy',loss)
        self.startCopy_models(source = "results", dest=self.SavingDir) 
        print('File saved to:',self.SavingDir)
        print('-'*60) 

    def plotLoss(self,loss,thisModel_Name, bottom=0, save=False):
        if Colab:clear_output()
        loss_mean=np.zeros(len(loss))
        loss_mean[0]=loss[0]
        for k in range(1,len(loss)): loss_mean[k] = 0.95*loss_mean[k-1] + 0.05*loss[k]
        fig = plt.figure(figsize=(9,6))
        plt.plot(loss)    
        plt.plot(loss_mean)
        plt.title("Model: {}".format(thisModel_Name))
        plt.xlabel("Batch")
        plt.ylabel("Loss")
        if bottom is not None:
            plt.ylim(bottom=0)
        plt.minorticks_on()
        plt.grid(which='major', linestyle='--', linewidth='0.3', color='black')
        plt.grid(which='minor', linestyle=':', linewidth='0.1', color='black')
        if save:plt.savefig('results/{}.svg'.format(thisModel_Name))
        plt.show()

# use:-------------------------------------------------------------
# import urllib.request  
# import importlib

# url="https://github.com/holianh/Linux_DeepLearning_tools/raw/master/taLibs_ASR_utils.py"

# filename=url.split('/')[-1]
# print(filename)
# # os.remove(filename)
# filename, headers = urllib.request.urlretrieve(url,filename=filename) 
# import taLibs_ASR_utils
# importlib.reload(taLibs_ASR_utils)

# taSaveLoad=taLibs_ASR_utils.ASRutil(thisModel_Name)

# print(taSaveLoad.SavingDir) 
# taSaveLoad.help()    
