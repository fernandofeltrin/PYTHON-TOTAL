import os
import time
import numpy as np
import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.
x_test = x_test / 255.

x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

os.environ.pop('TF_CONFIG', None)

%%time

model1 = Sequential()
model1.add(Dense(units = 128, input_shape = (784,), activation = 'relu'))
model1.add(Dropout(rate = 0.2))
model1.add(Dense(units = 128, activation = 'relu'))
model1.add(Dropout(rate = 0.2))
model1.add(Dense(units = 128, activation = 'relu'))
model1.add(Dropout(rate = 0.2))
model1.add(Dense(units = 128, activation = 'relu'))
model1.add(Dropout(rate = 0.2))
model1.add(Dense(units = 10, activation = 'softmax'))
model1.compile(optimizer = 'Adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['sparse_categorical_accuracy'])
model1.fit(x_train, y_train,
           steps_per_epoch = 100,
           epochs = 500,
           verbose = 1)

os.environ.pop('TF_CONFIG', None)

dist = tf.distribute.MirroredStrategy()

%%time

with dist.scope():
  model2 = Sequential()
  model2.add(Dense(units = 128, input_shape = (784,), activation = 'relu'))
  model2.add(Dropout(rate = 0.2))
  model2.add(Dense(units = 128, activation = 'relu'))
  model2.add(Dropout(rate = 0.2))
  model2.add(Dense(units = 128, activation = 'relu'))
  model2.add(Dropout(rate = 0.2))
  model2.add(Dense(units = 128, activation = 'relu'))
  model2.add(Dropout(rate = 0.2))
  model2.add(Dense(units = 10, activation = 'softmax'))
  model2.compile(optimizer = 'Adam',
                loss = 'sparse_categorical_crossentropy',
                metrics = ['sparse_categorical_accuracy'])
  model2.fit(x_train, y_train,
             steps_per_epoch = 100,
             epochs = 500,
             verbose = 1)

os.environ.pop('TF_CONFIG', None)

dist2 = tf.distribute.MultiWorkerMirroredStrategy()

%%time

with dist2.scope():
  model2 = Sequential()
  model2.add(Dense(units = 128, input_shape = (784,), activation = 'relu'))
  model2.add(Dropout(rate = 0.2))
  model2.add(Dense(units = 128, activation = 'relu'))
  model2.add(Dropout(rate = 0.2))
  model2.add(Dense(units = 128, activation = 'relu'))
  model2.add(Dropout(rate = 0.2))
  model2.add(Dense(units = 128, activation = 'relu'))
  model2.add(Dropout(rate = 0.2))
  model2.add(Dense(units = 10, activation = 'softmax'))
  model2.compile(optimizer = 'Adam',
                loss = 'sparse_categorical_crossentropy',
                metrics = ['sparse_categorical_accuracy'])
  model2.fit(x_train, y_train,
             steps_per_epoch = 100,
             epochs = 500,
             verbose = 1)
