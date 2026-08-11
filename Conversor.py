import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2

# Caracteres ASCII darker-lighter
ascii = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'

# Defina o caminho de onde está a imagem
path = str(input("Defina o caminho de onde a imagem está: "))

# Defina o formato da imagem
formato_img = str(input("Formato da imagem (jpeg, png, ...): "))

# Carregando Imagem
array = img.imread(path, format = formato_img)

# Redimensionando imagem para tamanho desejável utilizando processos de reamostragem(Interpolação)
escala = float(input("Defina a escala que a imagem possuíra (0.5, 0.6, ..., 1): "))

# Opencv(cv2) com método de interpolação por área
array_redi = cv2.resize(array, None, fx = escala, fy = escala,  interpolation = cv2.INTER_AREA)

# Deixando preto e branco (Fórmula ITU-R BT.709)
array_redi_709 = 0.2125*array_redi[:,:,0] + 0.7153*array_redi[:,:,1] + 0.0721*array_redi[:,:,2]

# Deixando preto e branco (Fórmula ITU-R BT.601)
array_redi_601 = 0.299*array_redi[:,:,0] + 0.587*array_redi[:,:,1] + 0.114*array_redi[:,:,2]

# Salvando Imagem redimensioanada
nome = "action1." + formato_img
plt.imsave(nome, array_redi_709)

nome = "action2." + formato_img
plt.imsave(nome, array_redi_601)
