import numpy as np
from PIL import Image, ImageDraw, ImageFont


# ------------------------ Funções de Geração de Arquivos --------------------------

def gera_txt(matriz, m, n, caminho_save):
    """
    matriz = Matriz MxN com elementos sendo caracteres ASCII
    m = Altura da matriz(linhas)
    n = Largura da matriz(colunas)
    caminho_save = Caminho de origem da imagem mesclado com o nome do arquivo e por fim, a tipagem TXT
    """


    # Caracteres ASCII darker-lighter
    ascii = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^`'

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
    with open(caminho_save, "w") as arquivo:
        for linha in matriz_ascii:
            for elemento in linha:

                arquivo.write(str(elemento)+'') # Adiciona cada elemento de uma linha

            arquivo.write('\n') # Quebra linha

    return matriz_ascii


def gera_bitmap(texto, largura, altura, caminho_save,  cor_fundo, cor_letra, path_font = None, font_size = 5):
    """
    texto = Matriz de caracteres ASCII
    largura = Quantidade de colunas da matriz ASCII
    altura = Quantidade de linhas da matriz ASCII
    caminho_save = Caminho onde ficará salvo a imagem ASCII, normalmente no mesmo local da imagem original
    cor_fundo = Cor do fundo da imagem (Superfície desenhada)
    cor_letra = Cor da letra
    path_font = Caminho onde a fonte da letra está localizada
    font_size = Tamanho da letra
    """

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
