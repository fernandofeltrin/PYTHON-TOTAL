# -*- coding: utf-8 -*-

"""
Código escrito por Fernando Feltrin
github.com/fernandofeltrin
fernando2rad@gmail.com
"""

from keras.preprocessing import image
from keras.models import Sequential, load_model
import numpy as np

model = Sequential()
model = load_model('C:/Users/Fernando/Desktop/PROJETO CNN COLUNA v1.1/classificador2.h5')

img_teste = image.load_img('C:/Users/Fernando/Desktop/PROJETO CNN COLUNA v1.1/dataset/amostras_teste/PATOLOGICA_0_8131.jpeg',
                           target_size = (128, 128))
img_teste = image.img_to_array(img_teste)
img_teste /= 255
img_teste = np.expand_dims(img_teste,
                           axis = 0)

resultado_teste = model.predict(img_teste)
print(resultado_teste)

resultado_final = resultado_teste
print(resultado_final[0])

if resultado_final[0] < 0.5:
    print('Imagem com aspecto de lesão benigna de pele.')
else:
    print('Imagem com aspecto de lesão maligna de pele.')

