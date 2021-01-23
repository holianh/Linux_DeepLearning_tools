# ViVo dataset preprocessing
Tải file, rồi xử lý hết tất cả các thứ, lưu vào file rồi, chỉ việc chạy 1 lần thôi, các lần sau thì load là đủ
Cách dùng:
```python
import h5py
datasetPath='/content/dataset/vivos/ViVo_Alldata_MFCCs_Labels.h5'
h5f = h5py.File(datasetPath, 'r')

MFCCs_train     =  h5f['MFCCs_train']
TrainLabels     =  h5f['TrainLabels']
Len_Labels__test=  h5f['Len_Labels__test']
Len_Labels_train=  h5f['Len_Labels_train']
Len_mfcc__test  =  h5f['Len_mfcc__test']
Len_mfcc_train  =  h5f['Len_mfcc_train']
MFCCs_test_     =  h5f['MFCCs_test_']
TestLabels      =  h5f['TestLabels']
vocab_size      =  h5f['vocab_size'][()]
MaxlenMFCC      =  h5f['MaxlenMFCC'][()]
MaxlenLabel     =  h5f['MaxlenLabel'][()]
# Define model, train:
# ............................
print('MFCCs_train:',MFCCs_train.shape)
print('TrainLabels:',TrainLabels.shape)
print('Len_Labels__test:',Len_Labels__test.shape)
print('Len_Labels_train:',Len_Labels_train.shape)
print('Len_mfcc__test:',Len_mfcc__test.shape)
print('Len_mfcc_train:',Len_mfcc_train.shape)
print('MFCCs_test_:',MFCCs_test_.shape)
print('TestLabels:',TestLabels.shape)
print('vocab_size:',vocab_size)
print('MaxlenMFCC:',MaxlenMFCC)
print('MaxlenLabel:',MaxlenLabel)

h5f.close()
```

<details>
  <summary>Vivo Full code:</summary>

```python
import csv, json, os, librosa, mmap, pickle, h5py,random
from tqdm.notebook import tqdm
from IPython.display import clear_output 
from os.path import exists, join
import matplotlib.pyplot as plt
import numpy as np

try:
  from mutagen.mp3 import MP3
  import soundfile as sf
  from python_speech_features import mfcc 
  import scipy.io.wavfile as wav
except:
  !pip install mutagen 
  !pip install soundfile
  !pip install python_speech_features
  from mutagen.mp3 import MP3
  import soundfile as sf
  from python_speech_features import mfcc 
  import scipy.io.wavfile as wav
  clear_output()

class TADataProcessing:
  def __init__(self,  dataHome     ='/content/dataset/vivos',
                      Data_GdriveID='1--lnmOwkbAyVr-3rFf-kaLqDVE7bW-bQ',
                      datasetPath=None):
      """
        datasetPath='/content/dataset/vivos/Alldata_MFCCs_Labels.h5'
      """
      self.dataHome=dataHome
      self.gdriveID=Data_GdriveID
      self.char_index = {}
      self.index_char = {} 
      # ====================
      
      self.plabel_test_ =join(dataHome,'label_test_.pickle')
      self.plabel_train =join(dataHome,'label_train.pickle')
      self.ptest_MFCC   =join(dataHome,'MFCC_test_.pickle')
      self.test_corpus  =join(dataHome,'corpus_test.json')
      self.pchar_index  =join(dataHome,'idchar_index.pickle')
      self.train_corpus =join(dataHome,'corpus_train.json')
      self.pindex_char  =join(dataHome,'idindex_char.pickle')
      self.ptrain_MFCC  =join(dataHome,'MFCC_train.pickle')
      self.Alldata      =join(dataHome,'ViVo_Alldata_MFCCs_Labels.h5')

      self.plen_vocab    =join(dataHome,'len_vocab.pickle')
      self.plen_maxMfcc  =join(dataHome,'len_maxMfcc.pickle')
      self.plen_maxLabel =join(dataHome,'len_maxLabel.pickle')

      self.pTrainText='/content/dataset/vivos/train/prompts.txt'
      
      self.MFCCs_test_=None
      self.MFCCs_train=None 

      self.MaxlenMFCC =0
      self.MaxlenLabel=0 
      self.vocab_size=0
      
      self.Len_Labels__test=[]
      self.Len_Labels_train=[]
      self.Len_mfcc__test=[]
      self.Len_mfcc_train=[]

      
      if datasetPath:
        self.fnLoad_data_final(datasetPath)
      

  def fndownload(self):
    if exists(self.dataHome):return
    print("Starting download...")
    !gdown --id 1--lnmOwkbAyVr-3rFf-kaLqDVE7bW-bQ
    # !wget https://ailab.hcmus.edu.vn/assets/vivos.tar.gz
    # !rsync --progress vivos.tar.gz  /content/drive/Shareddrives/DataSets/Speech_Vietnamese/
    !mkdir dataset 
    !tar xzf vivos.tar.gz -C ./dataset    
    !head {self.pTrainText}
    print("Downloaded!")

  def audio_duaration(self,path):
    if path.endswith('.mp3'):
      try:
          audio = MP3(path)
          length = audio.info.length
          return length
      except:
          return None
    elif path.endswith('.wav'):
      f = sf.SoundFile(path)
      length=len(f) / f.samplerate
      return length
  def fileNLines(self,fileID): return len(open(fileID).readlines())
  def PrepareData_ViVo(self,subdir,label_file,output_file):
    """
    data_org=join(self.dataHome,"test/waves/{fileID}.wav")
    1. Đọc hết file:
        label  => fileID và lbl
        fileID => pwav
        pwav   => wLength
    """
    labels = []
    durations = []
    wavPaths = []
    FLENGTH=self.fileNLines(label_file)
    with open(label_file) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=" ")
        pbar = tqdm(total=FLENGTH) # Init pbar
        for cnt,line in enumerate(tsvreader):
            # print(line)
            fileID=line[0]
            label=' '.join(line[1:])
            # print(self.dataHome,subdir,fileID[:-4],fileID)
            audio_file = join(subdir,fileID[:-4],fileID)+'.wav'
            if not exists(audio_file):continue
            if (cnt%(FLENGTH//5)==0): print (cnt, audio_file)            
            duration=self.audio_duaration(audio_file)
            if duration>0:
                if len(label)>1:
                    wavPaths.append(audio_file)
                    durations.append(duration)
                    labels.append(label)
            pbar.update(n=1)
    with open(output_file, 'w') as out_file:
        for i in range(len(wavPaths)):
            line = json.dumps({'wavPaths': wavPaths[i], 
                               'duration': durations[i],
                               'text': labels[i]})
            out_file.write(line + '\n')
  def fnMake_Descfile(self, test_subdir      ='/content/dataset/vivos/test/waves',
                            test_label_file  ="/content/dataset/vivos/test/prompts.txt",
                            train_subdir     ='/content/dataset/vivos/train/waves',
                            train_label_file ="/content/dataset/vivos/train/prompts.txt"
                            ):
    """
      Muốn có thêm dev, thì cần phải sửa thêm. đây mới chỉ có test, train
      train_corpus={
        {"wavPaths": "...", "duration": xx, "text": "..."}
        ...
        {"wavPaths": "...", "duration": xx, "text": "..."}
      }
      Output:/content/dataset/vivos/test_corpus.json
            :/content/dataset/vivos/train_corpus.json
    """    
    
    if exists(self.test_corpus):return
    print("Start fnMake_Descfile")
    self.PrepareData_ViVo(test_subdir,test_label_file,self.test_corpus)
    self.PrepareData_ViVo(train_subdir,train_label_file,self.train_corpus)
    print("Finished")

  def fnMakeVocab(self):
    """
      output: /content/dataset/vivos/idchar_index.pickle
    """    
    if exists(self.pchar_index):return
    print("Start fnMakeVocab")
    def MakeVocabs(desc_file,Vocab=set()): 
        with open(desc_file) as json_line_file:
            for line_num, json_line in enumerate(json_line_file):
                spec = json.loads(json_line)   
                Vocab.update(set(spec['text'].split()))
        return Vocab
    Vocab=MakeVocabs(self.test_corpus)
    Vocab=MakeVocabs(self.train_corpus,Vocab)    
    charslist=list(Vocab)
    charslist.sort()
    self.vocab_size=len(charslist)
    for k,ch in enumerate(charslist):
        self.char_index[ch] = k
        self.index_char[k] = ch
    self.fnSaveObject(self.pchar_index,self.char_index)
    self.fnSaveObject(self.pindex_char,self.index_char)
    self.fnSaveObject(self.plen_vocab,self.vocab_size)
    print("Done!")
  def fnLoad_Char_index(self): 
    self.char_index = pickle.load( open( self.pchar_index, "rb" ) )
    self.index_char = pickle.load( open( self.pindex_char, "rb" ) )
    self.vocab_size = pickle.load( open( self.plen_vocab, "rb" ) )

  def fnMakeLabels(self):
    """
      output: /content/dataset/vivos/traintest_label.py.npz
    """
    if exists(self.plabel_test_):
      self.TestLabels=self.fnLoadpickle(self.plabel_test_)
      self.TrainLabels=self.fnLoadpickle(self.plabel_train)
      print('Test  Label:',self.TestLabels.shape)
      print('train Label:',self.TrainLabels.shape)
      return
    print("Start fnMakeLabels")
    def MakeLabels(desc_file):
      All_Labels=[] 
      desc_file=join(self.dataHome,desc_file)
      if len(self.char_index)<1:
        self.fnLoad_Char_index()
      with open(desc_file) as json_line_file:
        for line_num, json_line in enumerate(json_line_file):
          spec = json.loads(json_line)
          label=[self.char_index[word] for word in  spec['text'].split()]
          
          All_Labels.append(label)
      return All_Labels
    self.TestLabels =MakeLabels(self.test_corpus)
    self.TrainLabels=MakeLabels(self.train_corpus)
    self.Len_Labels__test=[len(lbl) for lbl in self.TestLabels]
    self.Len_Labels_train=[len(lbl) for lbl in self.TrainLabels]   

    self.MaxlenLabel=max(self.MaxlenLabel,max(self.Len_Labels__test),len(self.Len_Labels_train)) 

    self.TestLabels =self.fnPaddingList_2D(self.TestLabels)
    self.TrainLabels=self.fnPaddingList_2D(self.TrainLabels)
    print('Test  Label:',self.TestLabels.shape)
    print('train Label:',self.TrainLabels.shape)
    self.fnSaveObject(self.plabel_test_,self.TestLabels)
    self.fnSaveObject(self.plabel_train,self.TrainLabels)
    self.fnSaveObject(self.plen_maxLabel,self.MaxlenLabel)

    print("OK!")

  def fnPlot_mfcc_feature(self,vis_mfcc_feature, title='',ylabel='',xlabel=''):
    fig = plt.figure(figsize=(12,5))
    ax = fig.add_subplot(111)
    im = ax.imshow(vis_mfcc_feature, cmap=plt.cm.jet, aspect='auto')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)   
    plt.show()
  
  def fnSaveObject(self,fileout,Object2save):
    with open(fileout, 'wb') as filehandle:
      pickle.dump(Object2save, filehandle, protocol=pickle.HIGHEST_PROTOCOL)

  def fnLoadpickle(self,file2load):
    return pickle.load( open(file2load, "rb" ))

  def fnMakeMFCC(self):
    """
      Tạo ra file json chứa list of list các MFCC (chưa padding)
    """
    
    if exists(self.ptest_MFCC):
      self.MFCCs_test_=self.fnLoadpickle(self.ptest_MFCC)
      self.MFCCs_train=self.fnLoadpickle(self.ptrain_MFCC)
      self.MFCCs_train=self.fnLoadpickle(self.ptrain_MFCC)
      print(f"MFCCs_test_:{self.MFCCs_test_.shape}\nMFCCs_train:{self.MFCCs_train.shape}")
      return
    print("Start fnMakeMFCC")
    lblpath=[ self.test_corpus,
              self.train_corpus]
    def MakeMFCC(desc_file):
        MFCCs=[]
        FLENGTH=len(open(desc_file).readlines())
        with open(desc_file) as json_line_file:
            pbar = tqdm(total=FLENGTH) # Init pbar
            for line_num, json_line in enumerate(json_line_file):
                spec = json.loads(json_line)   
                fn=spec['wavPaths']
                (rate,sig) = wav.read(fn)
                mfcc_feat = mfcc(sig,rate,numcep=80)                
                MFCCs.append(mfcc_feat)
                pbar.update(n=1)
                # if line_num>3:break
        return MFCCs
    self.MFCCs_test_=MakeMFCC(lblpath[0])
    self.Len_mfcc__test=[len(lbl) for lbl in self.MFCCs_test_]
    self.MaxlenMFCC=max(self.MaxlenMFCC,max(self.Len_mfcc__test))
    self.MFCCs_test_=self.fnPaddingList_3D(self.MFCCs_test_)
    self.fnSaveObject(self.ptest_MFCC,  self.MFCCs_test_)
    
    self.MFCCs_train=MakeMFCC(lblpath[1])
    self.Len_mfcc_train=[len(lbl) for lbl in self.MFCCs_train]
    self.MaxlenMFCC=max(self.MaxlenMFCC,max(self.Len_mfcc_train))
    self.MFCCs_train=self.fnPaddingList_3D(self.MFCCs_train)
    self.fnSaveObject(self.ptrain_MFCC, self.MFCCs_train)
    
    self.fnSaveObject(self.plen_maxMfcc , self.MaxlenMFCC)
    
    print(f"MFCCs_test_:{self.MFCCs_test_.shape}\nMFCCs_train:{self.MFCCs_train.shape}")
    print(f"len mfcc: test={len(self.MFCCs_test_)}, train={len(self.MFCCs_train)}, \
      \nmfcc[0] shape={self.MFCCs_train[0].shape}, \nmfcc[1] shape={self.MFCCs_train[1].shape}")
    print("fnMakeMFCC done!")
  def fnShuffle (self,Xdata,Ydata):
    mylist=np.arange(len(Ydata))
    random.shuffle(mylist)
    newX=[Xdata[mylist[k]] for k in mylist]
    newY=[Ydata[mylist[k]] for k in mylist]
    return newX,newY
  def fnPaddingList_2D(self,aList,maxLengh=None):
    """
      aList[batch, lengh]
    """
    if not maxLengh:
      maxLengh = max([len(r) for r in aList])
    def PaddingList2D(SS):
        b = np.zeros([len(aList),maxLengh])
        for i,j in enumerate(SS):
            b[i][0:len(j)] = j
        return b
    return PaddingList2D(aList)

  def fnPaddingList_3D(self,aList,maxLengh=None,maxWidth=None):
    """
      aList[batch, nparray[lengh, width]]
    """
    if not maxLengh:
      maxLengh = max([len(r) for r in aList])
    if not maxWidth:
      maxWidth = max([r.shape[1] for r in aList])
    def PaddingList3D(SS):
        b = np.zeros([len(aList),maxLengh,maxWidth])
        for i,j in enumerate(SS):
            b[i,0:len(j)] = j
        return b
    return PaddingList3D(aList)
    
  def fnLoad_data_final(self,datasetPath=None):
    """
      Mặc định khi lưu: datasetPath='Alldata_MFCCs_Labels.h5'
      Load cách này chỉ dùng để đưa vào .fit
      Khi nào dùng xong, thì gọi hàm:  `fnLoad_data_final_close` để đóng dataset lại.
    """    
    if not datasetPath:
      datasetPath=self.Alldata
    self.h5f = h5py.File(datasetPath, 'r')   
    self.MFCCs_train     =  self.h5f['MFCCs_train']
    self.TrainLabels     =  self.h5f['TrainLabels']
    self.Len_Labels__test=  self.h5f['Len_Labels__test']
    self.Len_Labels_train=  self.h5f['Len_Labels_train']
    self.Len_mfcc__test  =  self.h5f['Len_mfcc__test']
    self.Len_mfcc_train  =  self.h5f['Len_mfcc_train']
    self.MFCCs_test_     =  self.h5f['MFCCs_test_']
    self.TestLabels      =  self.h5f['TestLabels']
    self.vocab_size      =  self.h5f['vocab_size'][()]
    self.MaxlenMFCC      =  self.h5f['MaxlenMFCC'][()]
    self.MaxlenLabel     =  self.h5f['MaxlenLabel'][()]
    
  def fnLoad_data_final_close(self):    
    self.h5f.close()

  def fnVivoData_processing(self):
    datasetPath=self.Alldata
    if exists(datasetPath):return
    print("Start fnVivoData_processing...")
    # Downlaod data:----------------------------------------
    self.fndownload()
    # Step 2: Chuẩn hoá file đầu vào:-----------------------
    self.fnMake_Descfile()
    # Step 3: Tạo từ điển từ vựng:-----------------------
    self.fnMakeVocab()
    # Step 4: Tạo Test, Train Labels:-----------------------
    self.fnMakeLabels()
    #Step 5: Make MFCC
    self.fnMakeMFCC()

    h5f = h5py.File(datasetPath, 'w')
    h5f.create_dataset('MFCCs_train', data=self.MFCCs_train)
    h5f.create_dataset('TrainLabels', data=self.TrainLabels)
    
    h5f.create_dataset('Len_Labels__test', data=self.Len_Labels__test)
    h5f.create_dataset('Len_Labels_train', data=self.Len_Labels_train)
    h5f.create_dataset('Len_mfcc__test', data=self.Len_mfcc__test)
    h5f.create_dataset('Len_mfcc_train', data=self.Len_mfcc_train)

    h5f.create_dataset('MFCCs_test_', data=self.MFCCs_test_)
    h5f.create_dataset('TestLabels', data=self.TestLabels)
    h5f.create_dataset('vocab_size', data=self.vocab_size)
    h5f.create_dataset('MaxlenMFCC', data=self.MaxlenMFCC)
    h5f.create_dataset('MaxlenLabel',data=self.MaxlenLabel)
    
    h5f.close()
    # !rsync --progress {datasetPath} '/content/drive/Shareddrives/DataSets/Speech_Vietnamese/'
    print("Done!")

if __name__ == '__main__':
  Vivo=TADataProcessing()  
  Vivo.fnVivoData_processing()
  # !rsync --progress "/content/dataset/vivos/ViVo_Alldata_MFCCs_Labels.h5" '/content/drive/Shareddrives/DataSets/Speech_Vietnamese/'
  # Vivo.fnLoad_data_final()
  # print('Vivo.MFCCs_test_.shape:',Vivo.MFCCs_test_.shape)
  # Vivo.fnLoad_data_final_close()

  # Download file: ViVo_Alldata_MFCCs_Labels.h5 from gdrive:
  # !gdown --id 1APS-lUzQ_iBepXwe-sMNh3bbVeogUhz4 
  import h5py
  datasetPath='/content/dataset/vivos/ViVo_Alldata_MFCCs_Labels.h5'
  h5f = h5py.File(datasetPath, 'r')

  MFCCs_train     =  h5f['MFCCs_train']
  TrainLabels     =  h5f['TrainLabels']
  Len_Labels__test=  h5f['Len_Labels__test']
  Len_Labels_train=  h5f['Len_Labels_train']
  Len_mfcc__test  =  h5f['Len_mfcc__test']
  Len_mfcc_train  =  h5f['Len_mfcc_train']
  MFCCs_test_     =  h5f['MFCCs_test_']
  TestLabels      =  h5f['TestLabels']
  vocab_size      =  h5f['vocab_size'][()]
  MaxlenMFCC      =  h5f['MaxlenMFCC'][()]
  MaxlenLabel     =  h5f['MaxlenLabel'][()]
  # Define model, train:
  # ............................
  print('MFCCs_train:',MFCCs_train.shape)
  print('TrainLabels:',TrainLabels.shape)
  print('Len_Labels__test:',Len_Labels__test.shape)
  print('Len_Labels_train:',Len_Labels_train.shape)
  print('Len_mfcc__test:',Len_mfcc__test.shape)
  print('Len_mfcc_train:',Len_mfcc_train.shape)
  print('MFCCs_test_:',MFCCs_test_.shape)
  print('TestLabels:',TestLabels.shape)
  print('vocab_size:',vocab_size)
  print('MaxlenMFCC:',MaxlenMFCC)
  print('MaxlenLabel:',MaxlenLabel)
 
  h5f.close()
```

</details>


# Cách dùng HDF5 để lưu/store large dataset 
https://github.com/tflearn/tflearn
```python
"""
Example on how to use HDF5 dataset with TFLearn. HDF5 is a data model,
library, and file format for storing and managing data. It can handle large
dataset that could not fit totally in ram memory. Note that this example
just give a quick compatibility demonstration. In practice, there is no so
real need to use HDF5 for small dataset such as CIFAR-10.
"""

from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.layers.core import *
from tflearn.layers.conv import *
from tflearn.data_utils import *
from tflearn.layers.normalization import *
from tflearn.layers.estimator import regression

# CIFAR-10 Dataset
from tflearn.datasets import cifar10
(X, Y), (X_test, Y_test) = cifar10.load_data()
Y = to_categorical(Y)
Y_test = to_categorical(Y_test)

# Create a hdf5 dataset from CIFAR-10 numpy array
import h5py
h5f = h5py.File('data.h5', 'w')
h5f.create_dataset('cifar10_X', data=X)
h5f.create_dataset('cifar10_Y', data=Y)
h5f.create_dataset('cifar10_X_test', data=X_test)
h5f.create_dataset('cifar10_Y_test', data=Y_test)
h5f.close()

# Load hdf5 dataset
h5f = h5py.File('data.h5', 'r')
X = h5f['cifar10_X']
Y = h5f['cifar10_Y']
X_test = h5f['cifar10_X_test']
Y_test = h5f['cifar10_Y_test']

# Build network
network = input_data(shape=[None, 32, 32, 3], dtype=tf.float32)
network = conv_2d(network, 32, 3, activation='relu')
network = max_pool_2d(network, 2)
network = conv_2d(network, 64, 3, activation='relu')
network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 2)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, 10, activation='softmax')
network = regression(network, optimizer='adam',
                     loss='categorical_crossentropy',
                     learning_rate=0.001)

# Training
model = tflearn.DNN(network, tensorboard_verbose=0)
model.fit(X, Y, n_epoch=50, shuffle=True, validation_set=(X_test, Y_test),
          show_metric=True, batch_size=96, run_id='cifar10_cnn')

h5f.close()
```


# Tensorflow: Modern way to load large data
https://stackoverflow.com/questions/57717004/tensorflow-modern-way-to-load-large-data

```python
# Developed using python 3.6, tensorflow 1.14.0.
# This code writes data (pairs (label, image) where label is int64 and image is np.ndarray) into .tfrecord files and
# uses them for training a simple neural network. It is meant as a minimal working example of how to use tfrecords. This
# solution is likely not optimal. If you know how to improve it, please comment on
# https://stackoverflow.com/q/57717004/9988487. Refer to links therein for further information.
import tensorflow as tf
import numpy as np
from tensorflow.python import keras as keras


# Helper functions (see also https://www.tensorflow.org/tutorials/load_data/tf_records)
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def write_tfrecords_file(out_path: str, images: np.ndarray, labels: np.ndarray) -> None:
    """Write all image-label pairs into a single .tfrecord file.
    :param out_path: File path of the .tfrecord file to generate or overwrite.
    :param images: array with first dimension being the image index. Every images[i].tobytes() is
        serialized and written into the file as 'image': wrap_bytes(img_bytes)
    :param labels: 1d array of integers. labels[i] is the label of images[i]. Written as 'label': wrap_int64(label)"""
    assert len(images) == len(labels)
    with tf.io.TFRecordWriter(out_path) as writer:  # could use writer_options parameter to enable compression
        for i in range(len(labels)):
            img_bytes = images[i].tobytes()  # Convert the image to raw bytes.
            label = labels[i]
            data = {'image': _bytes_feature(img_bytes), 'label': _int64_feature(label)}
            feature = tf.train.Features(feature=data)  # Wrap the data as TensorFlow Features.
            example = tf.train.Example(features=feature)  # Wrap again as a TensorFlow Example.
            serialized = example.SerializeToString()  # Serialize the data.
            writer.write(serialized)  # Write the serialized data to the TFRecords file.


def parse_example(serialized, shape=(256, 256, 1)):
    features = {'image': tf.io.FixedLenFeature([], tf.string), 'label': tf.io.FixedLenFeature([], tf.int64)}
    # Parse the serialized data so we get a dict with our data.
    parsed_example = tf.io.parse_single_example(serialized=serialized, features=features)
    label = parsed_example['label']
    image_raw = parsed_example['image']  # Get the image as raw bytes.
    image = tf.io.decode_raw(image_raw, tf.float32)  # Decode the raw bytes so it becomes a tensor with type.
    image = tf.reshape(image, shape=shape)
    return image, label  # this function will be called once (to add it to tf graph; then parse images individually)


# create some arbitrary data to play with: 1000 images sized 256x256 with one colour channel. Use your custom np-arrays
IMAGE_WIDTH, NUM_OF_IMAGES, NUM_OF_CLASSES, COLOUR_CHANNELS = 256, 10_000, 10, 1
# using float32 to save memory. Must match type in parse_example(), tf.decode_raw(image_raw, tf.float32)
features_train = np.random.sample((NUM_OF_IMAGES, IMAGE_WIDTH, IMAGE_WIDTH, COLOUR_CHANNELS)).astype(np.float32)
labels_train = np.random.randint(low=0, high=NUM_OF_CLASSES, size=NUM_OF_IMAGES)  # one random label for each image
features_eval = features_train[:200]  # use the first 200 images as evaluation data for simplicity.
labels_eval = labels_train[:200]
write_tfrecords_file("train.tfrecord", features_train, labels_train)  # normal: split the data files of several GB each
write_tfrecords_file("eval.tfrecord", features_eval, labels_eval)  # this may take a while. Consider a progressbar
# The files are complete. Now define a model and use datasets to feed the data from the .tfrecord files into the model.
model = keras.Sequential([keras.layers.Flatten(input_shape=(256, 256, 1)),
                          keras.layers.Dense(128, activation='relu'),
                          keras.layers.Dense(10, activation='softmax')])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
# Check docs for parameters (compression, buffer size, thread count. Also www.tensorflow.org/guide/performance/datasets

train_dataset = tf.data.TFRecordDataset("train.tfrecord")  # specify a list (or dataset) of file names for large data
train_dataset = train_dataset.map(parse_example)  # parse tfrecords. Parameter num_parallel_calls may help performance.
train_dataset = train_dataset.shuffle(buffer_size=1024).batch(64)

validation_dataset = tf.data.TFRecordDataset("eval.tfrecord")
validation_dataset = validation_dataset.map(parse_example).batch(64)

model.fit(train_dataset, epochs=3)
# evaluate the results
results = model.evaluate(validation_dataset)
print('\n\nvalidation loss, validation acc:', results)
```

#  Python fastest way to get mp3 length
https://dev.to/konyu/how-to-get-mp3-file-s-durations-with-python-42p
```python
# !pip install mutagen 
from mutagen.mp3 import MP3

def mutagen_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None

# length = mutagen_length(wav_path)
# print("duration sec: " + str(length))
# print("duration min: " + str(int(length/60)) + ':' + str(int(length%60)))
```


