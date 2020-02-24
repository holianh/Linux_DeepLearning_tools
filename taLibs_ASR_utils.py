# ------------------------------- New ------------------------------------------------
# thisModel_Name='ASR-CNN+CTC_tutorial_train_test'
import glob, shutil
import os
from os.path import join, exists
if not exists('results'):os.makedirs('results')
try:
  import gpustat
except:
  os.system("pip install gpustat")
  import gpustat
def startCopy_models(source,dest):
    if not exists(dest): os.makedirs(dest)
    files = glob.glob(os.path.join(dest,"*"))
    for f in files: os.remove(f)            
    for file in glob.glob(os.path.join(source,"*.*")):
        shutil.copy2(file,dest)

def load_model(self, filename='results/{}'.format(thisModel_Name) ):
    if not exists (filename + '.model') :
        startCopy_models(dest = "results", source = "/content/drive/My Drive/Deeplearning/ASR---results/{}_results".format(thisModel_Name)) 
        print("Copy result inner load_model from gdrive to local, done!")
    self.ctc_model.load_weights(filename + '.model')
    if exists(filename + '.model.base'):self.model.load_weights(filename + '.model.base')
    if exists(filename + '.loss.npy'): self.loss=np.load(filename + '.loss.npy')

def save_model(self , filename='results/{}'.format(thisModel_Name) , comments='',loss=None):
    mydir="/".join(filename.split('/')[:-1])        
    if not exists(mydir): os.makedirs(mydir)        
    fnName=filename #+ comments
    self.ctc_model.save_weights(fnName + '.model')
    self.model.save_weights(fnName + '.model.base')
    f = open(fnName + '_steps.txt' , 'a+')           
    f.write(filename + comments+'\n')
    f.close()
    if loss:
        np.save(fnName + '.loss.npy',loss)
    dest="/content/drive/My Drive/Deeplearning/ASR---results/{}_results".format(thisModel_Name)
    startCopy_models(source = "results", dest=dest) 
    print('File saved to:',dest)
    print('-'*60) 

def plotLoss(loss,thisModel_Name, bottom=0):
    clear_output()
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
    plt.savefig('results/{}.svg'.format(thisModel_Name))
    plt.show()

# -----------------------------------------------------------------
# print("After Load weight:")
# load_model(am)
# batch = data_generator(batch_size, shuffle_list, wav_lst, label_data, vocab)
# test_loss=am.ctc_model.evaluate(x=batch,steps=1)
# print('Test_loss After Load weight=',test_loss)
# print("="*60)
def modulereload(modulename):
    import importlib
    importlib.reload(modulename)