import numpy as np
import matplotlib.pyplot as plt
import matplotlib.imagem as img

# Caracteres ASCII darker-lighter
ascii = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'

# Carregando Imagem
image = img.imread("path", format = "jpg")

# Deixando preto e branco
array = 0.299*image[:,:,0] + 0.587*image[:,:,1] + 0.144*image[:,:,2]


