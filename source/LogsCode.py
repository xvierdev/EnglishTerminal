def ler_arquivo(nome_arquivo='logs.txt'):
    """
    Lê o conteúdo de um arquivo de texto e retorna como uma string.
    Se nenhum nome de arquivo for fornecido, usa o nome padrão.
    
    :param nome_arquivo: O nome do arquivo a ser lido (opcional).
    :return: O conteúdo do arquivo como uma string.
    """
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def adicionar_dado(nome_arquivo='logs.txt', dado=''):
    """
    Adiciona um dado ao final do arquivo de texto.
    Se nenhum nome de arquivo for fornecido, usa o nome padrão.
    
    :param nome_arquivo: O nome do arquivo a ser escrito (opcional).
    :param dado: O dado a ser adicionado ao arquivo.
    """
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(dado + '\n')
