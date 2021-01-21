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




