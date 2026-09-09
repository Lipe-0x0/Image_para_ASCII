import numpy as np
from Busca import busca_caminho, busca_fonte
from Gerador import gera_txt, gera_bitmap
from termcolor import colored
from PIL import Image



# ------------------------------- Função Principal ----------------------------

def img_ascii(name_file, name_font, size = None, background_color = "black", letter_color = "white"):
    '''
    name_file = Nome do arquivo(diferenciando maiúscula de minúscula)
    size = Variável em forma de tupla se referindo ao comprimento(x) e altura(y) da imagem
    name_font = Nome da fonte personalizada, caso não possua, o padrão será arial

    Processos Aplicados: 
    1 - Fórmula ITU-R BT.601 para transformar em preto e branco
    
    Decisões: 
    Valor de pixel 0 = Preto (Utiliza caracteres robustos)
    Valor de pixel 255 = Branco (Utiliza caracteres esparsos)
    '''

    try:
        # Retorna caminho da imagem
        caminho_imagem = busca_caminho(name_file)
    except FileNotFoundError:
        print(colored("Arquivo não encontrado nos diretórios (Downloads, Documentos, Imagens)", "red"))
        return
    
    try:
        # Retorna caminho da fonte
        caminho_fonte = busca_fonte(name_font)
    except FileNotFoundError:
        print(colored("Fonte não encontrada em /usr/share/fonts", "red"))
        return
    
    # Carregando Imagem como matriz
    array = np.array(Image.open(caminho_imagem))

    # Verificando se matriz possui shape = [x,y,4](propriedade alpha)
    if np.shape(array)[len(np.shape(array))-1] == 4:
        array = array[:,:,:3]

    # Se a matriz for RGB então deixar em preto e branco
    if np.shape(array)[len(np.shape(array))-1] == 3:
        # Deixando preto e branco (Fórmula ITU-R BT.601)
        array = 0.299*array[:,:,0] + 0.587*array[:,:,1] + 0.114*array[:,:,2]

    caminho_arq_txt = caminho_imagem.split(".")[0] + ".txt" # Pegando caminho da imagem para salvar txt na pasta da original

    caminho_img_ascii = caminho_imagem.split(".")[0] + "ASCII" + ".jpeg" # Pegando caminho da imagem para salvar bitmap redimensionado na pasta da original 

    # Gerando arquivo txt
    matriz_ascii = gera_txt(array, size[1], size[0], caminho_arq_txt)

    # Gerando imagem ASCII
    gera_bitmap(matriz_ascii, largura = size[0], altura = size[1], path_font = caminho_fonte, caminho_save = caminho_img_ascii, cor_fundo = background_color, cor_letra = letter_color)


    return None
