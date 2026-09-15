import os

# ------------------------ Funções Complementares -----------------------------

def busca_caminho(nome_arquivo):
    diretorios = ["~/Imagens","~/Downloads","~/Documentos"]

    for dire in diretorios: # Para cada diretório...
        for caminho, subpastas, arqs in os.walk(os.path.expanduser(dire)): # Procurar recursivamente nas subpastas de tais

            if nome_arquivo in arqs: # Se arquivo estiver na lista de todos os arquivos daquele diretório
                return os.path.join(caminho, nome_arquivo) # Retornar caminho completo

    raise FileNotFoundError


def busca_fonte(nome_arquivo):
    for caminho, subpastas, arqs in os.walk("/usr/share/fonts"):
        if nome_arquivo in arqs:
            return os.path.join(caminho, nome_arquivo)

    raise FileNotFoundError
