import sqlite3
from os import path

def inserir_palavras():
    """Insere palavras do arquivo wordlist.txt no banco de dados main.db."""
    try:
        file_path = path.join(path.dirname(__file__), 'wordlist.txt')
        db_path = path.join(path.dirname(__file__), 'main.db')

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            try:
                with open(file_path, 'r', encoding='utf-8') as wordlist:
                    data_to_insert = []
                    for line in wordlist:
                        line_clean = line.strip()
                        if not line_clean or line_clean.startswith('#'):
                            continue
                        parts = line_clean.split(' ')
                        en_word = parts[0]
                        br_word = ' '.join(parts[1:])
                        data_to_insert.append((en_word, br_word))

                    cursor.executemany("INSERT OR IGNORE INTO Words (english, portuguese) VALUES (?, ?)", data_to_insert)
                    conn.commit()
                    print("Palavras inseridas com sucesso!")

            except FileNotFoundError:
                print(f"Erro: Arquivo '{file_path}' não encontrado.")
                return

    except sqlite3.Error as e:
        print(f"Erro ao inserir palavras: {e}")

inserir_palavras()