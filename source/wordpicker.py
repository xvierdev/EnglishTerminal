from os import path # Import para caminho
from random import choice # Import para escolher a string

def strings():
    # Define o caminho completo para o arquivo usando o diretório atual do script
    file_path = path.join(path.dirname(__file__), 'wordlist.txt')
    
    try:
        # Abre o arquivo para leitura
        with open(file_path, 'r', encoding='utf-8') as arquivo:
            # Lê todas as linhas, ignorando comentários e espaços em branco
            strings = []
            for linha in arquivo:
                linha_limpa = linha.strip()  # Remove espaços e quebras de linha
                if not linha_limpa or linha_limpa.startswith('#'):
                    continue  # Ignora linhas vazias ou comentários
                strings.append(linha_limpa)
        # Verifica se há strings e imprime a primeira (ou outra posição)
        if strings:
            return choice(strings)
        else:
            print("Nenhuma string válida encontrada no arquivo.")
            
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")