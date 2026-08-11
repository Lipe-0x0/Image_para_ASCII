import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2


def img_ascii(path, escala_redimensionamento = 0.5):
    '''
    path = Caminho do arquivo
    escala_redimensionamento = Valor que definirá o tamanho em que a imagem será redimensionada inde de 0-1,
    sendo 0.5 padrão

    Processos Aplicados: 
    1 - Reamostragem por Interpolação (Interpolação por Área)
    2 - Fórmula ITU-R BT.601 para transformar em preto e branco
    
    Decisões: 
    Valor de pixel 0 = Preto (Utiliza caracteres robustos)
    Valor de pixel 255 = Branco (Utiliza caracteres esparsos)
    '''

    # Caracteres ASCII darker-lighter
    ascii = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'

    # Formato da imagem (Pegando o ultimo elemento do path que é justamente o formato da imagem)
    formato_img = path.split(".")[1]

    # Carregando Imagem
    array = img.imread(path, format = formato_img)

    # Opencv(cv2) com método de interpolação por área
    array_redi = cv2.resize(array, None, fx = escala_redimensionamento, fy = escala_redimensionamento,  interpolation = cv2.INTER_AREA)

    # Deixando preto e branco (Fórmula ITU-R BT.601)
    array_redi = 0.299*array_redi[:,:,0] + 0.587*array_redi[:,:,1] + 0.114*array_redi[:,:,2]

    print(np.max(array_redi))
    print(np.min(array_redi))

    return None

