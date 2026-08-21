import numpy as np
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


def gera_bitmap(texto, largura, altura, caminho_save,  cor_fundo = "black", cor_letra = "white", path_font = "goonado", font_size = 5):

    try:
        font = ImageFont.truetype(path_font, size = font_size) # Fonte escolhida pelo usuário
    except:
        # Caso ele não aceite a fonte do sistema
        font = ImageFont.truetype("arial.ttf", size = font_size) # Fonte arial padrão

    # Pegando altura e largura da primeira linha pois preciso deles para encontrar o tamanho da superfície desenhada
    left, top, right, bottom  = font.getbbox("".join(texto[0,:]))
    altura_letra = bottom - top
    largura_letra = (right - left) // largura

    pos_y = 10 # Posição da linha no eixo y(cada linha de caracteres será desenhada baseada na altura da letra)

    image = Image.new("RGB", (largura * largura_letra, altura * altura_letra), cor_fundo) # Superfície onde será desenhada
    draw = ImageDraw.Draw(image) # Gerando superfície no espaço
    
    # Para cada linha em matriz_ascii desenharei uma linha na superfície
    for linha in range(altura):
        frase = "".join(texto[linha,:]) 

        draw.text((10, pos_y), frase, font = font, fill = cor_letra)

        pos_y+=altura_letra # Adicionando para a próxima linha aparecer abaixo da outra)
  
    # Redimensionando imagem ASCII para tamanho original
    image = image.resize((largura, altura), Image.LANCZOS)

    image.save(caminho_save) # Salva imagem

    return None



def img_ascii(path, path_font, size = None):
    '''
    path = Caminho do arquivo
    size = Variável em forma de tupla se referindo ao comprimento(x) e altura(y) da imagem
    path_font = Caminho de fonte personalizada, caso não possua, o padrão será arial

    Processos Aplicados: 
    1 - Fórmula ITU-R BT.601 para transformar em preto e branco
    
    Decisões: 
    Valor de pixel 0 = Preto (Utiliza caracteres robustos)
    Valor de pixel 255 = Branco (Utiliza caracteres esparsos)
    '''

    # Carregando Imagem como matriz
    array = np.array(Image.open(path))

    # Se a matriz for RGB então deixar em preto e branco
    if np.shape(array)[len(np.shape(array))-1] == 3:
        # Deixando preto e branco (Fórmula ITU-R BT.601)
        array = 0.299*array[:,:,0] + 0.587*array[:,:,1] + 0.114*array[:,:,2]

    nome_txt = path.split(".")[0] + ".txt" # Pegando caminho da imagem para salvar txt na pasta da original

    nome_imgbit = path.split(".")[0] + "ASCII" + ".jpeg" # Pegando caminho da imagem para salvar bitmap redimensionado na pasta da original 

    # Gerando arquivo txt
    matriz_ascii = gera_txt(array, size[1], size[0], nome_txt)

    # Gerando imagem ASCII
    gera_bitmap(matriz_ascii, largura = size[0], altura = size[1], path_font = path_font, caminho_save = nome_imgbit)


    return None
