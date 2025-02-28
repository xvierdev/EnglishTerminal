# Script de transformação do arquivo txt em database de palavras
import sqlite3
from os import path

def insert_words():
    try:
        file_path = path.join(path.dirname(__file__), 'wordlist.txt')
        db_path = path.join(path.dirname(__file__), 'word.db')
        with sqlite3.connect(db_path) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS words (
                    en_word TEXT PRIMARY KEY,
                    br_word TEXT
                )
            ''')

            with open(file_path, 'r', encoding='utf-8') as wordlist:
                for linha in wordlist:
                    linha_limpa = linha.strip()  # Remove espaços e quebras de linha
                    if not linha_limpa or linha_limpa.startswith('#'):
                        continue  # Ignora linhas vazias ou comentários
                    en_word = linha_limpa.split(' ')[0]
                    br_word = ' '.join(linha_limpa.split(' ')[1:])
                    print(en_word, br_word)
                    cursor.execute("INSERT OR IGNORE INTO words (en_word, br_word) VALUES (?, ?)", (en_word, br_word))

            conexao.commit()
            print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao inserir dados: {erro}")

insert_words()