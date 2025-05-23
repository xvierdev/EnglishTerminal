import sqlite3
import logging
import db.connect as connect

# SQL queries to create database and tables.
create_table = """
CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nick TEXT UNIQUE NOT NULL,
        record INTEGER
);"""

create_words = """
CREATE TABLE IF NOT EXISTS Words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english TEXT UNIQUE NOT NULL,
    portuguese TEXT NOT NULL,
    category TEXT NOT NULL
);"""

user_index = "CREATE INDEX IF NOT EXISTS idx_users_nick ON Users (nick);"
words_index = "CREATE INDEX IF NOT EXISTS idx_words_english ON Words (english);"


def create_tables(db_file):
    """
    Cria as tabelas necessárias no banco de dados SQLite se elas não existirem.

    Este método estabelece uma conexão com o arquivo de banco de dados especificado
    e executa comandos SQL para criar as tabelas 'users' e 'words', juntamente
    com seus respectivos índices.

    Args:
        db_file (str): O caminho para o arquivo do banco de dados SQLite.

    Raises:
        sqlite3.Error: Se ocorrer algum erro durante a operação do banco de dados.

    Returns:
        None
    """
    try:
        conn = connect.connect()
        with conn:
            cursor = conn.cursor()
            cursor.execute(create_table)
            cursor.execute(user_index)
            logging.info("Table Users has been created successfully.")
            cursor.execute(create_words)
            cursor.execute(words_index)
            logging.info("Table Words has been created successfully.")
    except sqlite3.Error:
        raise


def populate_words(db_file, word_list):
    """
    Popula a tabela 'Words' no banco de dados SQLite com dados de um arquivo de texto.

    Este método lê um arquivo de texto linha por linha, esperando que cada linha contenha
    palavras em inglês e português, possivelmente com uma categoria, separadas por espaços.
    As linhas que começam com '#' ou estão vazias são ignoradas. Os dados processados
    são então inseridos na tabela 'Words', substituindo qualquer conteúdo existente.

    Args:
        db_file (str): O caminho para o arquivo do banco de dados SQLite.
        word_list (str): O caminho para o arquivo de texto contendo a lista de palavras.
                         Espera-se que cada linha contenha 'categoria english portuguese',
                         'english portuguese' ou apenas 'english portuguese'.

    Raises:
        FileNotFoundError: Se o arquivo especificado em `word_list` não for encontrado.
        sqlite3.Error: Se ocorrer algum erro durante a operação do banco de dados.

    Returns:
        None
    """
    try:
        with open(word_list, "r", encoding="utf-8") as wordlist:
            data_to_insert = []
            for line in wordlist:
                line_clean = line.strip()
                if not line_clean or line_clean.startswith("#"):  # ignore these lines
                    continue

                parts = line_clean.split(" ", 2)  # Split into three parts
                if len(parts) == 3:
                    category, en_word, br_word = parts
                    data_to_insert.append((en_word, br_word, category))
                else:
                    logging.info(f"Skipping line due to incorrect format: {line_clean}")
            with sqlite3.connect(db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Words")
                cursor.executemany(
                    "INSERT OR IGNORE INTO Words (english, portuguese, category) VALUES (?, ?, ?)",
                    data_to_insert,
                )
                logging.info(f"{cursor.rowcount} Words inserted/ignored.")
    except FileNotFoundError:
        raise FileNotFoundError(f"{word_list} not found.")
    except sqlite3.Error:
        raise


def create_user(user, db_file):
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Users (nick, record) VALUES (?, ?)",
                (user.get_nick(), user.get_points()),
            )
            logging.info(f"User {user.get_nick()} created successful.")
    except sqlite3.Error:
        raise
