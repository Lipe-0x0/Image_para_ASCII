import numpy as np
import matplotlib.pyplot as plt
import matplotlib.imagem as img

# Caracteres ASCII darker-lighter
ascii = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'

# Carregando Imagem
image = img.imread("path", format = "jpg")

# Deixando preto e branco (Fórmula ITU-R BT.709)
array = 0.2125*image[:,:,0] + 0.7153*image[:,:,1] + 0.0721*image[:,:,2]


