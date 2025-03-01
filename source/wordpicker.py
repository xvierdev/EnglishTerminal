import sqlite3
from os import path # Import para caminho
from random import randint # Import para escolher a string
from logs import report_bug

def strings():
    file_path = path.join(path.dirname(__file__), 'words.db')
    try:
        with sqlite3.connect(file_path) as conexao:
            cursor = conexao.cursor()
            cursor.execute(f'SELECT * FROM header')
            n_words = cursor.fetchone()[0]
            cursor.execute(f'SELECT * FROM words WHERE ID = {randint(1, n_words)}')
            word = cursor.fetchone()
            return word[1:]
    except sqlite3.Error as e:
        print(f'Error: {e}')
        report_bug(e)
