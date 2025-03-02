import sqlite3
from os import path

def insert_words():
    """
    Transforma o arquivo wordlist.txt em um banco de dados SQLite, removendo a tabela 'header'.
    """
    try:
        file_path = path.join(path.dirname(__file__), 'wordlist.txt')
        db_path = path.join(path.dirname(__file__), 'words.db')

        with sqlite3.connect(db_path) as conexao:
            cursor = conexao.cursor()

            # Cria a tabela 'words' se não existir
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS words (
                    en_word TEXT UNIQUE,
                    br_word TEXT
                );
            ''')

            try:
                with open(file_path, 'r', encoding='utf-8') as wordlist:
                    data_to_insert = []
                    for linha in wordlist:
                        linha_limpa = linha.strip()
                        if not linha_limpa or linha_limpa.startswith('#'):
                            continue
                        en_word = linha_limpa.split(' ')[0]
                        br_word = ' '.join(linha_limpa.split(' ')[1:])
                        data_to_insert.append((en_word, br_word))

                    # Insere os dados em lote
                    cursor.executemany("INSERT OR IGNORE INTO words (en_word, br_word) VALUES (?, ?)", data_to_insert)

            except FileNotFoundError:
                print(f"Erro: Arquivo '{file_path}' não encontrado.")
                return

            conexao.commit()
            print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao inserir dados: {erro}")

insert_words()