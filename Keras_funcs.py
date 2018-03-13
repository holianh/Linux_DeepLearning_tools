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

