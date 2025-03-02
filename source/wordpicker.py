import sqlite3
from os import path
from random import randint
from logs import report_bug

def strings():
    """
    Retorna uma palavra aleatória do banco de dados 'words.db'.

    Retorna:
        tuple: Uma tupla contendo a palavra e sua tradução, ou None em caso de erro.
    """
    file_path = path.join(path.dirname(__file__), 'words.db')
    try:
        with sqlite3.connect(file_path) as conexao:
            cursor = conexao.cursor()
            # Obtém uma palavra aleatória diretamente da tabela 'words'
            cursor.execute('SELECT word, translation FROM words ORDER BY RANDOM() LIMIT 1')
            word = cursor.fetchone()
            if word:
                return word
            else:
                return None #Retorna none caso não encontre nenhuma palavra.

    except sqlite3.Error as e:
        print(f'Error: {e}')
        report_bug(e)
        return None # Retorna None em caso de erro.
