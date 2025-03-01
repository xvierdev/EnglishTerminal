# Script de transformação do arquivo txt em database de palavras
import sqlite3
from os import path

def insert_words():
    try:
        file_path = path.join(path.dirname(__file__), 'wordlist.txt')
        db_path = path.join(path.dirname(__file__), 'words.db')
        with sqlite3.connect(db_path) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS words (
                    id INTEGER PRIMARY KEY,
                    en_word TEXT UNIQUE,
                    br_word TEXT
                );''')
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS header (
                    count_words INTEGER
                );
                '''
            )

            with open(file_path, 'r', encoding='utf-8') as wordlist:
                count = 0
                for linha in wordlist:
                    linha_limpa = linha.strip()  # Remove espaços e quebras de linha
                    if not linha_limpa or linha_limpa.startswith('#'):
                        continue  # Ignora linhas vazias ou comentários
                    en_word = linha_limpa.split(' ')[0]
                    br_word = ' '.join(linha_limpa.split(' ')[1:])
                    print(en_word, br_word)
                    cursor.execute("INSERT OR IGNORE INTO words (en_word, br_word) VALUES (?, ?)", (en_word, br_word))
                    count += 1
                cursor.execute(f"INSERT INTO header (count_words) VALUES ({count})")

            conexao.commit()
            print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao inserir dados: {erro}")

insert_words()