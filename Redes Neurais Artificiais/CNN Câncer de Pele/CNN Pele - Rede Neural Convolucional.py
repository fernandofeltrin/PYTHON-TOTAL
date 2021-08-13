# -*- coding: utf-8 -*-

"""
Código escrito por Fernando Feltrin
github.com/fernandofeltrin
fernando2rad@gmail.com
"""

import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import LearningRateScheduler
from keras.optimizers import RMSprop
from keras.callbacks import ReduceLROnPlateau

gerador_treino = ImageDataGenerator(rescale = 1.0/255,
                                    rotation_range = 5,
                                    horizontal_flip = True,
                                    shear_range = 0.2,
                                    height_shift_range = 0.07,
                                    zoom_range = 0.2)
gerador_teste = ImageDataGenerator(rescale = 1.0/255)

base_treino = gerador_treino.flow_from_directory('C:/Users/Fernando/Desktop/CNN_PELE/dataset/train/',
                                                 target_size = (128,128),
                                                 batch_size = 16,
                                                 class_mode = 'binary')
base_teste = gerador_teste.flow_from_directory('C:/Users/Fernando/Desktop/CNN_PELE/dataset/test/',
                                               target_size = (128,128),
                                               batch_size = 16,
                                               class_mode = 'binary')

classificador2 = Sequential()
classificador2.add(Conv2D(32,
                         kernel_size = (3,3),
                         padding = 'same',
                         input_shape = (128,128,3),
                         activation = 'relu'))
classificador2.add(BatchNormalization())
classificador2.add(MaxPooling2D(pool_size = (2,2)))
classificador2.add(Conv2D(32,
                         (3,3),
                         activation = 'relu'))
classificador2.add(BatchNormalization())
classificador2.add(MaxPooling2D(pool_size = (2,2)))
classificador2.add(Flatten())
classificador2.add(Dense(units = 128,
                        activation = 'relu'))
classificador2.add(Dropout(0.2))
classificador2.add(Dense(units = 128,
                        activation = 'relu'))
classificador2.add(Dropout(0.2))
classificador2.add(Dense(units = 1,
                        activation = 'sigmoid'))
optimizer = RMSprop(lr=0.001,
                    rho=0.9,
                    epsilon=1e-08,
                    decay=0.0)
classificador2.compile(optimizer = optimizer,
                      loss = 'binary_crossentropy',
                      metrics = ['accuracy'])
classificador2.summary()

epochs = 100

learning_rate = ReduceLROnPlateau(monitor='accuracy', 
                                            patience=3, 
                                            verbose=1, 
                                            factor=0.5, 
                                            min_lr=0.00001)

h_2 = classificador2.fit(base_treino,
                        steps_per_epoch = 100,
                        epochs = epochs,
                        validation_data = base_teste,
                        callbacks = [learning_rate],
                        verbose = 1,
                        validation_steps = 25)

classificador2.save('C:/Users/Fernando/Desktop/CNN_PELE/classificador2.h5',
                    overwrite=True,
                    include_optimizer=True,
                    save_format=True,
                    options = True)
classificador2.save_weights('C:/Users/Fernando/Desktop/CNN_PELE/classificador2_weights.h5')

print('Precisão do treino: {0:.2f}%'.format(max(h_2.history['accuracy']) * 100))
print('Precisão da validacao: {0:.5f}'.format(max(h_2.history['val_accuracy']) * 100))
