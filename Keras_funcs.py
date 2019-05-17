########################################################################
# Keras: save model + weight to files                      -------------
########################################################################
#history = model.fit(x=...
Client_Model_json=Train_npy_info+tadb2xxx_npy+Client_ID+'.Model.json' # name of model  file 
Client_weigh_json=Train_npy_info+tadb2xxx_npy+Client_ID+'.weight.json'# name of weight file 

# serialize model to JSON
model_json = model.to_json()
with open(Client_Model_json, "w") as json_file:json_file.write(model_json)
# serialize weights to HDF5
model.save_weights(Client_weigh_json)
print("Saved model + weight to disk")
# Ref:https://machinelearningmastery.com/save-load-keras-deep-learning-models/

########################################################################
# Keras: load model + weight from files to numpy array     -------------
########################################################################
import os, io, json
from keras.models import model_from_json
import numpy as np

def myGet_weight(fnName_model,fmName_weight):
    # Ref:https://machinelearningmastery.com/save-load-keras-deep-learning-models/
    # load json and create model
    json_file = open(fnName_model, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(fmName_weight)
    
    WW = loaded_model.get_weights()
    print("Loaded model from disk:",fmName_weight)
    return np.asarray(WW)
#use: 
#W=myGet_weight("(ta1072.npy_1080ti-3).model.json","(ta1072.npy_1080ti-3).w.json")
# then can calculate: W_all=W_all+W*0.5
    
    
##############################################################
Tensorboard: local and remote 
##############################################################
from keras.callbacks import TensorBoard
tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0,
                          write_graph=True, write_images=False)

h=model.fit(x=[ mfcc_vec, np.ones(Max_samples)*maxlen_AllMfcc,    word_vec, char_length ],
            y=np.ones(Max_samples),
            validation_split=0.2,
            batch_size=10,
            epochs=30,
            callbacks=[tensorboard]
          )
          
Tensorboard remote: ref: https://stackoverflow.com/questions/37987839/how-can-i-run-tensorboard-on-a-remote-server
Remote: tensorboard --logdir=. --host=0.0.0.0 --port=6006
Local (win/ubuntu): http://10.1.53.1:6006   (http://<IP server>:<port> 
https://stackoverflow.com/questions/37987839/how-can-i-run-tensorboard-on-a-remote-server
                                             
##############################################################
Keras: parallel GPUs Model training
##############################################################
'''
f01_filegen.py
/run/user/1000/gvfs/sftp:host=10.1.58.23,user=tact/home/tact/ta/asr_sp2t

database:    sftp://tact@10.1.58.23/home/tact/AudioDBs/All_database_processed/train

database out:sftp://tact@10.1.58.23/home/tact/AudioDBs/All_database_processed_augment

. Find the longest label        => maxlen_char
. Find the longest wav
. Make MFCC = get longest MFCC  => MFCC_shape
'''


import os;
GPUs="0,1,2"
gpus=3
os.environ["CUDA_VISIBLE_DEVICES"]=GPUs#"3" #"0,1,2"
import json
import taLibs as ta
import numpy as np
from os.path import exists
import pickle;
from keras.models import Model;
from keras import backend as K;
from keras.layers.embeddings import Embedding;
#from keras.utils.vis_utils import plot_model;
from keras.models import Sequential, load_model,save_model;
from keras.optimizers import rmsprop, adam, adagrad, SGD;
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau;
from keras.preprocessing.text import text_to_word_sequence, one_hot, Tokenizer;
from keras.layers import Input, Dense, merge, Dropout, BatchNormalization, Activation, Conv1D, Lambda;
#from Levenshtein import distance
import matplotlib                                    ###############
matplotlib.use('agg')
import matplotlib.pyplot as plt   
from matplotlib.backends.backend_pdf import PdfPages ###############
import datetime as dt
from os.path import exists
import time,math
import fnmatch
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")
import pprint as pp

print()
print('########################################################################################################')
print('Start...')
 


pproject_info='info/project_info.txt'

### INITTIAL VARIABLE ######################################################
### INITTIAL VARIABLE WITH NEW TRAINING SECTION ############################

recreate_data_____table=0


### BECAREFULL:    DELETE ALL FILES   #######################################
Clean_All_Files_Created=0
### CALL FUNCTIONS     ######################################################
csv_path='info/' # lưu vào thư mục đang chạy.
pproject_info='info/project_info.txt'
wav_train_path=csv_path+'data_train_path.csv'

if not exists(wav_train_path) or recreate_data_____table==1:
    if Clean_All_Files_Created==1:ta.Clean_AllFilesCreated()    # <<<< Becareful
    ta.Get_DB_info(wav_train_path)
    ta.build_Words_dict()
    with open(pproject_info) as data_file:data_loaded = json.load(data_file)
    pp.pprint (data_loaded) 
    #============================================================================
else:
    with open(pproject_info) as data_file:data_loaded = json.load(data_file)
    
    pp.pprint (data_loaded) 
    print()
import timeit
start = timeit.default_timer()  # Start counting time

csv_path='info/'
wav_train_path=data_loaded['wav_train_path']
wav_test__path=data_loaded['wav_test__path']

Max_len_MFCC=data_loaded['Max_len_MFCC']
maxlen_char =data_loaded['Max_len_label_no_space']

DataPath=data_loaded['DataPath']
DataPath_Train_npy  = data_loaded['subpaths']['DataPath_Train_npy']
Train_npy_info      = data_loaded['subpaths']['Train_npy_info']
pchar_index         = data_loaded['subpaths']['pchar_index']
 

print('####### initial finished! #####################################################################################')
print('###############################################################################################################')


# ~ import taLibs as ta
# ~ ta.RemakeLabels(wav_train_path)
# ~ exit()

with open(pchar_index,"rb") as f: char_index=pickle.load(f);    



#X_data, next_Pos=ta.Get_Batch_MFCC_Labels(wav_csv_path=wav_train_path,number_of_files=3,current_pos=0)

######################################################################################################
######################################################################################################
from keras.layers import Lambda, concatenate
from keras import Model
import tensorflow as tf

def multi_gpu_model(model, gpus):
  if isinstance(gpus, (list, tuple)):
    num_gpus = len(gpus)
    target_gpu_ids = gpus
  else:
    num_gpus = gpus
    target_gpu_ids = range(num_gpus)

  def get_slice(data, i, parts):
    shape = tf.shape(data)
    batch_size = shape[:1]
    input_shape = shape[1:]
    step = batch_size // parts
    if i == num_gpus - 1:
      size = batch_size - step * i
    else:
      size = step
    size = tf.concat([size, input_shape], axis=0)
    stride = tf.concat([step, input_shape * 0], axis=0)
    start = stride * i
    return tf.slice(data, start, size)

  all_outputs = []
  for i in range(len(model.outputs)):
    all_outputs.append([])

  # Place a copy of the model on each GPU,
  # each getting a slice of the inputs.
  for i, gpu_id in enumerate(target_gpu_ids):
    with tf.device('/gpu:%d' % gpu_id):
      with tf.name_scope('replica_%d' % gpu_id):
        inputs = []
        # Retrieve a slice of the input.
        for x in model.inputs:
          input_shape = tuple(x.get_shape().as_list())[1:]
          slice_i = Lambda(get_slice,
                           output_shape=input_shape,
                           arguments={'i': i,
                                      'parts': num_gpus})(x)
          inputs.append(slice_i)

        # Apply model on slice
        # (creating a model replica on the target device).
        outputs = model(inputs)
        if not isinstance(outputs, list):
          outputs = [outputs]

        # Save the outputs for merging back together later.
        for o in range(len(outputs)):
          all_outputs[o].append(outputs[o])

  # Merge outputs on CPU.
  with tf.device('/cpu:0'):
    merged = []
    for name, outputs in zip(model.output_names, all_outputs):
      merged.append(concatenate(outputs,
                                axis=0, name=name))
    return Model(model.inputs, merged)
######################################################################################################d
# ~ def data_generator():
    # ~ while 1:
        # ~ X_data=ta.Get_Batch_MFCC_Labels(wav_csv_path=wav_train_path,number_of_files=10)
        # ~ yield X_data
with tf.device('/cpu:0'):
    input_tensor=Input(shape=(Max_len_MFCC,20));

    x=Conv1D(kernel_size=1,filters=192,padding="same")(input_tensor);
    x=BatchNormalization(axis=-1)(x);
    x=Activation("tanh")(x);

    def res_block(x,size,rate,dim=192):
        x_tanh=Conv1D(kernel_size=size,filters=dim,dilation_rate=rate,padding="same")(x);
        x_tanh=BatchNormalization(axis=-1)(x_tanh);
        x_tanh=Activation("tanh")(x_tanh);
        
        #x_tanh=Dropout(0.2)(x_tanh)
        
        x_sigmoid=Conv1D(kernel_size=size,filters=dim,dilation_rate=rate,padding="same")(x);
        x_sigmoid=BatchNormalization(axis=-1)(x_sigmoid);
        x_sigmoid=Activation("sigmoid")(x_sigmoid);
        
        #x_sigmoid=Dropout(0.2)(x_sigmoid)
        
        out=merge([x_tanh,x_sigmoid],mode="mul");
        out=Conv1D(kernel_size=1,filters=dim,padding="same")(out);
        out=BatchNormalization(axis=-1)(out);
        out=Activation("tanh")(out);
        
        out=Dropout(0.2)(out)
        x=merge([x,out],mode="sum");
        return x,out;

    skip=[]
    for i in np.arange(0,6):#3
        for r in [1,2,4,8,16]:
            x,s=res_block(x,size=7,rate=r);
            skip.append(s);

    def ctc_lambda_function(args):
        logit, logit_length_input, y_true_input, y_true_length_input=args;
        return K.ctc_batch_cost(y_true_input,logit,logit_length_input,y_true_length_input);

    #with tf.device('/device:GPU:0'):
    skip_tensor=merge([s for s in skip],mode="sum");
    logit=Conv1D(kernel_size=1,filters=192,padding="same")(skip_tensor);
    logit=BatchNormalization(axis=-1)(logit);
    logit=Activation("tanh")(logit);
    logit=Conv1D(kernel_size=1,filters=len(char_index)+1,padding="same",activation="softmax")(logit);
    
    base_model=Model(inputs=input_tensor,outputs=logit);
    logit_length_input =Input(shape=(1,),name='logit_length_input');
    y_true_input       =Input(shape=(maxlen_char,),name='y_true_input');
    y_true_length_input=Input(shape=(1,),name='y_true_length_input');

    loss_out=Lambda(ctc_lambda_function,output_shape=(1,),name="ctc")([
                    logit,
                    logit_length_input,
                    y_true_input, 
                    y_true_length_input])

    model=Model(inputs=[input_tensor,logit_length_input,y_true_input,y_true_length_input],outputs=loss_out);

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
#gpus=3
print("Using %i GPUs" %gpus)
print(dt.datetime.now())
print()
#from keras.utils.multi_gpu_utils import  multi_gpu_model 
model1 = multi_gpu_model(model, gpus=gpus)

#How to parallel_model from normal:
# 1: install update keras to newest: (should do in other envs in conda)
# 2: copy folder: ~/anaconda3/envs/kr/lib/python3.5/site-packages/keras/utils    to current using keras folder:
#                 ~/anaconda3/envs/P3/lib/python3.5/site-packages/keras/utils    (change name of old folder before paste here)
# https://stackoverflow.com/questions/47210811/can-not-save-model-using-model-save-following-multi-gpu-model-in-keras
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
#with tf.device('/cpu:0'):
model.compile(loss={'ctc': lambda y_true, y_pred: y_pred},optimizer="adam",metrics=['accuracy']);
model1.compile(loss={'ctc': lambda y_true, y_pred: y_pred},optimizer="adam",metrics=['accuracy']);
# ~ plot_model(model, to_file="info/model.png", show_shapes=True);
# ~ print('done')


Client_filepath_BestModel=Train_npy_info+'Train_on_batch.BestModel'
Client_filepath_LastModel=Train_npy_info+'Train_on_batch.LastModel'

Client_Model_json=Train_npy_info+'Train_on_batch.Model.json'
Client_weigh_json=Train_npy_info+'Train_on_batch.weight.json'

filepath=Client_filepath_BestModel
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='auto')
# ~ checkpoint = ModelCheckpoint(filepath)

lr_change  = ReduceLROnPlateau(monitor  ="loss",
                               mode     ="auto",
                               factor   =0.2,   # factor by which the learning rate will be reduced. new_lr = lr * factor
                               patience =2,     #number of epochs with no improvement after which learning rate will be reduced.
                               min_lr   =0.0)

# ~ early      = EarlyStopping(monitor="loss", # acc, accuracy, loss, val_loss
                           # ~ mode="max",    # auto, min, max
                           # ~ patience=10);  # No. epochs with no improvement after which training=>stopped.
                                                          
from keras.callbacks import TensorBoard
tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0,write_graph=False, write_images=False)

callbacks_list = [lr_change,tensorboard,checkpoint]
opt=adam(lr=0.03)#03);


try:
    model=load_model(Client_filepath_LastModel,compile=False)
    model1 = multi_gpu_model(model, gpus=gpus)
    model1.compile(loss={'ctc': lambda y_true, y_pred: y_pred},optimizer="adam",metrics=['accuracy']);
    model.compile(loss={'ctc': lambda y_true, y_pred: y_pred},optimizer="adam",metrics=['accuracy']);
    print('Continous training..... ============================== ')

except IOError:
    print('Training the first time ============================== ')




##############################################################################################
##############################################################################################
FisTrain,_ = ta.NpyFiles_2list(DataPath_Train_npy) 
L=len(FisTrain);    

# L = NEpochs * Nsteps_per_epoch = Number of samples


NEpochs= 3
Bat_step=gpus*45 #=135
tBat_step=Bat_step

Nsteps_per_epoch=(L//Bat_step)//4 #gpus*100 # = L//Bat_step =4h//4=1h
NEpochs=200

def mygen(s=''):
    #global NEpochs,Nsteps_per_epoch
    print('\ngenerator initiated:'+s)
    with open(pproject_info) as data_file:data_loaded = json.load(data_file)
    Max_len_MFCC=data_loaded['Max_len_MFCC']
    idx = 0
    #DataPath_Train_npy='/home/tact/AudioDBs/All_DB_augment_npys/Train/ta1000/'
    FisTrain,_ = ta.NpyFiles_2list(DataPath_Train_npy) 
    L=len(FisTrain);    print('L=',L)
    LB=[k for k in range(0, L, Bat_step)]
    kk=0
    print('Nsteps_per_epoch=',Nsteps_per_epoch)
    print('NEpochs=',NEpochs)
    print('len(LB)=',len(LB))
    while True:
        for idx in range(len(LB)-1):
            if (kk%Nsteps_per_epoch==0)or(idx==len(LB)-2):print('\n ********** %s d[%s],c[%s]C %s'%(L,LB[idx],LB[idx+1],kk)); 
            kk+=1
            Xtrain=ta.fnRead_Data_Labelnpys(LB[idx],LB[idx+1],Max_len_MFCC,1)
            Ytrain=np.ones(len(Xtrain[0]))
            yield Xtrain, Ytrain

Nvalidation_steps=3
def mygen_valid(s=''):
    print('\nTest initiated:'+s)
    with open(pproject_info) as data_file:data_loaded = json.load(data_file)
    Max_len_MFCC=data_loaded['Max_len_MFCC']    
    idx = 0
    #DataPath_Train_npy='/home/tact/AudioDBs/All_DB_augment_npys/Train/ta1124/'
    _,Fis_test = ta.NpyFiles_2list(DataPath_Train_npy) 
    vL=len(Fis_test);    print('vL=',vL)    
    vLB=[k for k in range(0, vL, tBat_step)]    
    while True:
        for idx in range(len(vLB)-1):
            Xval=ta.fnRead_Data_Labelnpys(vLB[idx],vLB[idx+1],Max_len_MFCC,0)
            Yval=np.ones(len(Xval[0]))
            yield Xval, Yval
##############################################################################################        
##############################################################################################
print('Start training............................')
stop = timeit.default_timer()  
MaxLoop=1
from pprint import pprint
for k in range(0,MaxLoop):
    gen=mygen('train data')
    valli=mygen_valid('valid data')
    hist = model1.fit_generator(gen,
                        steps_per_epoch=Nsteps_per_epoch,
                        epochs=NEpochs,
                        validation_data=valli,
                        validation_steps=Nvalidation_steps,
                        callbacks=callbacks_list
                        ) 

    # ~ print(h.history)
    # ~ hist = model1.fit( [mfcc_vec_out,  mfcc_vec_out_len, char_vec, char_length] , 
                        # ~ np.ones(Nfiles_real), 
                        # ~ validation_split=0.2,
                        # ~ epochs=epochs,              # so lan lap lai trong khi training
                        # ~ batch_size=batch_size,     # 1 lan nhan
                        # ~ callbacks=callbacks_list)
    save_model(model,Client_filepath_LastModel,overwrite=True)
    print("save_model(model,Client_filepath_LastModel,overwrite=True) OK!")
    print('This epochs:   ',ta.format_seconds_to_hhmmss(math.trunc(timeit.default_timer()-stop)), 'Current loop:',k,'/',MaxLoop)
    stop = timeit.default_timer()
    total_time=stop-start # in seconds
    tRan=ta.format_seconds_to_hhmmss(math.trunc(total_time))
    tWait=ta.format_seconds_to_hhmmss(math.trunc(((MaxLoop-(k+1))*total_time)/(k+1)))
    print('Ran time:      ',tRan)
    print('Need waiting...',tWait)
    print(dt.datetime.now())
    ta.plotHistory(hist,fdfName='pdfs/history_training([]).pdf',sPreFix='')
    print('End of this round!---------------------------------------------------------------')


model_json = model.to_json();
with open(Client_Model_json, "w") as json_file:json_file.write(model_json);# serialize model to JSON
model.save_weights(Client_weigh_json);print("Saved model + weight to disk");# serialize weights to HDF5
# Ref:https://machinelearningmastery.com/save-load-keras-deep-learning-models/

save_model(model,Client_filepath_LastModel,overwrite=True)
print(dt.datetime.now())

#######################################################################
Keras python jupyter notebook: Print/display model structure
#######################################################################
# from keras.utils import plot_model
# plot_model(vqa_model, to_file='model.png')
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

SVG(model_to_dot(vqa_model,show_shapes=True).create(prog='dot', format='svg'))
    

                                             
#######################################################################
Keras python jupyter notebook: Live plot Loss accuracy when training 
#######################################################################
%matplotlib inline
from matplotlib import pyplot as plt
from IPython.display import clear_output
from datetime import datetime
class PlotLosses(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.i = 0
        self.x = []
        self.losses = []
        self.val_losses = []
        
        self.fig = plt.figure()
        self.acc=[]
        self.val_acc=[]
        self.logs = []

    def on_epoch_end(self, epoch, logs={}):        
        self.logs.append(logs)
        self.x.append(self.i)
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.acc.append(logs.get('sparse_categorical_accuracy'))
        self.val_acc.append(logs.get('val_sparse_categorical_accuracy'))
        self.i += 1
        
        clear_output(wait=True)
        fig=plt.figure(figsize=(10,8))
        plt.subplot(2, 1, 1)
        plt.plot(self.x, self.losses, label="loss")
        plt.plot(self.x, self.val_losses, label="val_loss")
        plt.legend(loc='best')
        plt.ylabel('Loss')
        plt.grid(True)
        
        plt.subplot(2, 1, 2)
        plt.plot(self.x, self.acc, label="acc")
        plt.plot(self.x, self.val_acc, label="val_acc")

        plt.title(' acc results')
        plt.legend(loc='best')
        plt.xlabel('epoch')
        plt.ylabel('Acc')
        plt.grid(True)
        plt.tight_layout()
        plt.show();
        
plot_losses = PlotLosses()
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
