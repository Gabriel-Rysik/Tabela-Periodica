import unicodedata #Biblioteca para manipular caracteres

def limpar_texto(texto): # Função para Remover acentos, espaços extras e padronização do texto.
    if not texto:
        return " "
    nfd = unicodedata.normalize('NFD', texto)
    return "".join(c for c in nfd if not unicodedata.combining(c)).lower().strip()
