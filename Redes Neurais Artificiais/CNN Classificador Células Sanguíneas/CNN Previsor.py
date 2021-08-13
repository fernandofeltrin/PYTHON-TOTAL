from keras.preprocessing import image
from keras.models import Sequential, load_model
import numpy as np

model = Sequential()
model = load_model('model.h5')

img_teste = image.load_img('C:/Users/Fernando/Desktop/CNN_TORAX/dataset/amostra_teste/Tuberculosis.jpg',
                           target_size = (300, 300))
img_teste = image.img_to_array(img_teste)
img_teste = np.expand_dims(img_teste,
                           axis = 0)

resultado_teste = model.predict(img_teste)
print(resultado_teste)

resultado_final = resultado_teste
print(resultado_final[0,3])

if resultado_final[0,0].any() > 0.5:
    print('Eosinófilo.')
if resultado_final[0,1].any() > 0.5:
    print('Linfócito')
if resultado_final[0,2].any() > 0.5:
    print('Monócito')
if resultado_final[0,3].any() > 0.5:
    print('Neutrófilo')
else:
    print('A imagem fornecida não cumpre os requisitos mínimos para ser processada,')
    print('ou o resultado do processamento da mesma é inconclusivo.')
