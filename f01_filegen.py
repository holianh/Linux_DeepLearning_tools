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
os.environ["CUDA_VISIBLE_DEVICES"]="0,1,2,3"
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
### INITTIAL VARIABLE ######################################################

recreate_data_table=0

### CALL FUNCTIONS ######################################################
csv_path='info/' # lưu vào thư mục đang chạy.
pproject_info='info/project_info.txt'
wav_train_path=csv_path+'data_train_path.csv'

if not exists(wav_train_path) or recreate_data_table==1:
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
def data_generator():
    while 1:
        X_data=ta.Get_Batch_MFCC_Labels(wav_csv_path=wav_train_path,number_of_files=10)
        yield X_data
with tf.device('/cpu:0'):
    input_tensor=Input(shape=(Max_len_MFCC,20));

    x=Conv1D(kernel_size=1,filters=192,padding="same")(input_tensor);
    x=BatchNormalization(axis=-1)(x);
    x=Activation("tanh")(x);

    def res_block(x,size,rate,dim=192):
        x_tanh=Conv1D(kernel_size=size,filters=dim,dilation_rate=rate,padding="same")(x);
        x_tanh=BatchNormalization(axis=-1)(x_tanh);
        x_tanh=Activation("tanh")(x_tanh);
        
        x_tanh=Dropout(0.2)(x_tanh)
        
        x_sigmoid=Conv1D(kernel_size=size,filters=dim,dilation_rate=rate,padding="same")(x);
        x_sigmoid=BatchNormalization(axis=-1)(x_sigmoid);
        x_sigmoid=Activation("sigmoid")(x_sigmoid);
         
        x_sigmoid=Dropout(0.2)(x_sigmoid)
        
        out=merge([x_tanh,x_sigmoid],mode="mul");
        out=Conv1D(kernel_size=1,filters=dim,padding="same")(out);
        out=BatchNormalization(axis=-1)(out);
        out=Activation("tanh")(out);
        
        out=Dropout(0.2)(out)
        x=merge([x,out],mode="sum");
        return x,out;

    skip=[]
    for i in np.arange(0,3):#3
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
gpus=4
print("Using %i GPUs" %gpus)
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
# ~ checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='auto')
checkpoint = ModelCheckpoint(filepath)

lr_change  = ReduceLROnPlateau(monitor  ="loss",
                               mode     ="auto",
                               factor   =0.2,   # factor by which the learning rate will be reduced. new_lr = lr * factor
                               patience =2,     #number of epochs with no improvement after which learning rate will be reduced.
                               min_lr   =0.0)
from keras.callbacks import TensorBoard
tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0,write_graph=True, write_images=False)

callbacks_list = [lr_change,tensorboard]#,checkpoint]
opt=adam(lr=0.03)#03);


try:
    model=load_model(Client_filepath_LastModel,compile=False)
    model1 = multi_gpu_model(model, gpus=gpus)
    model1.compile(loss={'ctc': lambda y_true, y_pred: y_pred},optimizer="adam",metrics=['accuracy']);
    model.compile(loss={'ctc': lambda y_true, y_pred: y_pred},optimizer="adam",metrics=['accuracy']);

except IOError:
    print('Training the first time ============================== ')

print('Start training............................')
stop = timeit.default_timer()  
MaxLoop=200
for k in range(0,MaxLoop):
    print()
    Nfiles=gpus*32*150 # ~ gpus*10k = gpus*Batch_size* ?
    epochs=64
    batch_size=32*gpus
    #mfcc_vec_out,  mfcc_vec_out_len, char_vec, char_length=ta.Get_Batch_MFCC_Labels(wav_csv_path=wav_train_path,number_of_files=Nfiles)
    mfcc_vec_out,  mfcc_vec_out_len, char_vec, char_length=ta.Get_Batch_MFCC_Labels_Augmentation(wav_csv_path=wav_train_path,number_of_files=Nfiles)
    
    Nfiles_real=len(char_length)
    sPreFix='Nfiles={}_batch={}_epochs={}_Nfreal={}'.format(Nfiles,batch_size,epochs,Nfiles_real)
    print(sPreFix)
    
    # ~ h = model.train_on_batch([mfcc_vec_out,  mfcc_vec_out_len, char_vec, char_length] , np.ones(10))
    # ~ print(h.history)
    hist = model1.fit( [mfcc_vec_out,  mfcc_vec_out_len, char_vec, char_length] , 
                        np.ones(Nfiles_real), 
                        validation_split=0.2,
                        epochs=epochs,              # so lan lap lai trong khi training
                        batch_size=batch_size,     # 1 lan nhan
                        callbacks=callbacks_list)
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
    ta.plotHistory(hist,fdfName='pdfs/history_training[].pdf',sPreFix=sPreFix)


model_json = model.to_json();
with open(Client_Model_json, "w") as json_file:json_file.write(model_json);# serialize model to JSON
model.save_weights(Client_weigh_json);print("Saved model + weight to disk");# serialize weights to HDF5
# Ref:https://machinelearningmastery.com/save-load-keras-deep-learning-models/

save_model(model,Client_filepath_LastModel,overwrite=True)
print(dt.datetime.now())



    
