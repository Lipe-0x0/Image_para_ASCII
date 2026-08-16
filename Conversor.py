import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont


def gera_txt(matriz, m, n, nome_txt):
    
    # Caracteres ASCII darker-lighter
    ascii = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'
    
    # Criando cópia da matriz para substituir valores pelos caracteres  
    matriz_ascii = np.array(matriz, copy = True, dtype = str) 

    for i in range(m):
        for j in range(n):
            # Normalizando o valor do pixel para ficar entre 0-1
            pixel_normal = matriz[i,j]/255

            # Índice da string ascii
            ind = int(pixel_normal*len(ascii))

            # Se o indíce da string for 67 (limite da string) fazer ele voltar 1 para ficar 66
            if ind == len(ascii):
                ind = len(ascii) - 1

            # Substituindo pixel por caractere
            matriz_ascii[i,j] = ascii[ind]

    # Gerando arquivo txt onde receberá valores de matriz_ascii
    with open(nome_txt, "w") as arquivo:
        for linha in matriz_ascii:
            for elemento in linha:

                arquivo.write(str(elemento)+'') # Adiciona cada elemento de uma linha

            arquivo.write('\n') # Quebra linha

    return matriz_ascii


def gera_bitmap(texto, tam_x, tam_y, cor = "black", path_font = "goonado", font_size = 5):

    try:
        font = ImageFont.truetype(path_font, size = font_size) # Fonte escolhida pelo usuário
    except:
        # Caso ele não aceite a fonte do sistema
        font = ImageFont.truetype("arial.ttf", size = font_size) # Fonte arial padrão

    # Pegando altura e largura da primeira linha pois preciso deles para encontrar o tamanho da superfície desenhada
    left, top, right, bottom  = font.getbbox("".join(texto[0,:]))
    altura = bottom - top
    largura = (right - left) // tam_y

    pos_y = altura # Posição da linha no eixo y(cada linha de caracteres será desenhada baseada nesta altura)

    image = Image.new("RGB", (tam_y * largura, tam_x * altura), cor) # Superfície onde será desenhada
    draw = ImageDraw.Draw(image) # Gerando superfície no espaço
    
    # Para cada linha em matriz_ascii desenharei uma linha na superfície
    for linha in range(tam_x):
        frase = "".join(texto[linha,:]) 

        draw.text((10, pos_y), frase, font = font)

        pos_y+=altura # Adicionando para a próxima linha aparecer abaixo da outra
    

    image.save("output.jpeg") # Salva imagem

    return None


def redimen_bitmap(caminho_save, m, n):

    imagem = cv2.imread("output.jpeg") # Carregando imagem ASCII (provavelmente ultrapassa o tamanho da imagem original)

    imagem_redi = cv2.resize(imagem, (m, n) , interpolation = cv2.INTER_AREA) # Redimensionando ela para tamanho da imagem original

    cv2.imwrite(caminho_save, imagem_redi) # Salvando imagem na mesma pasta da original

    return None


def img_ascii(path, path_font, size = None,  escala_redimensionamento = None):
    '''
    path = Caminho do arquivo
    size = Variável em forma de tupla se referindo ao comprimento(x) e altura(y) da imagem
    escala_redimensionamento = Valor que definirá o tamanho em que a imagem será redimensionada indo de 0-1
    path_font = Caminho de fonte personalizada, caso não possua, o padrão será arial

    Processos Aplicados: 
    1 - Reamostragem por Interpolação (Interpolação por Área)
    2 - Fórmula ITU-R BT.601 para transformar em preto e branco
    
    Decisões: 
    Valor de pixel 0 = Preto (Utiliza caracteres robustos)
    Valor de pixel 255 = Branco (Utiliza caracteres esparsos)
    '''

    # Carregando Imagem
    array = cv2.imread(path)

    # Opencv(cv2) redimensionando  com método de interpolação por área
    array_redi = cv2.resize(array, size, fx = escala_redimensionamento, fy = escala_redimensionamento, interpolation = cv2.INTER_AREA)
    
    # Se a matriz for RGB então deixar em preto e branco
    if np.shape(array_redi)[len(np.shape(array_redi))-1] == 3:
        # Deixando preto e branco (Fórmula ITU-R BT.601)
        array_redi = 0.299*array_redi[:,:,0] + 0.587*array_redi[:,:,1] + 0.114*array_redi[:,:,2]
    
    # Tamanho da matriz redimensionada
    m, n = np.shape(array_redi) 

    nome_txt = path.split(".")[0] + ".txt" # Pegando caminho da imagem para salvar txt na pasta da original

    nome_imgbit = path.split(".")[0] + "ASCII" + ".jpeg" # Pegando caminho da imagem para salvar bitmap redimensionado na pasta da original 

    # Gerando arquivo txt
    matriz_ascii = gera_txt(array_redi, m, n, nome_txt)

    # Gerando arquivo png ASCII
    gera_bitmap(matriz_ascii, tam_x = m, tam_y = n, path_font = path_font)

    # Redimensionando Imagem bitmap caso ela esteja de tamanho diferente
    redimen_bitmap(nome_imgbit, m, n)

    return None

    


path = str(input("Path: "))

x = int(input("x: "))
y = int(input("y: "))

path_font = str(input("Caminho da fonte no sistema: "))

img_ascii(path, size = (x,y), path_font = path_font)
