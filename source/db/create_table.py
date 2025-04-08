import sqlite3, logging

# SQL queries to create database and tables.
create_table = '''
CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT UNIQUE NOT NULL,
        record INTEGER
);'''

create_words = '''
CREATE TABLE IF NOT EXISTS Words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english TEXT UNIQUE NOT NULL,
    portuguese TEXT NOT NULL,
    category TEXT NOT NULL
);'''

user_index = "CREATE INDEX IF NOT EXISTS idx_users_user ON Users (user);"
words_index = "CREATE INDEX IF NOT EXISTS idx_words_english ON Words (english);"

def create_tables(db_file):
    '''Creates the necessary tables if they don't exist.'''
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table)
            cursor.execute(user_index)            
            logging.info(f"Table Users has been created successfully.")
            cursor.execute(create_words)
            cursor.execute(words_index)
            logging.info(f"Table Words has been created successfully.")
    except sqlite3.Error:
        raise

def populate_words(db_file, word_list):
    '''Populates the Words table from wordlist.txt.'''
    try:
        with open(word_list, 'r', encoding='utf-8') as wordlist:
            data_to_insert = []
            for line in wordlist:
                line_clean = line.strip()
                if not line_clean or line_clean.startswith('#'): # ignore these lines
                    continue

                parts = line_clean.split(' ', 2)  # Split into three parts
                if len(parts) == 3:
                    category, en_word, br_word = parts
                    data_to_insert.append((en_word, br_word, category))
                else:
                    logging.info(f"Skipping line due to incorrect format: {line_clean}")
            with sqlite3.connect(db_file) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Words')
                cursor.executemany("INSERT OR IGNORE INTO Words (english, portuguese, category) VALUES (?, ?, ?)", data_to_insert)
                logging.info(f"{cursor.rowcount} Words inserted/ignored.")
    except FileNotFoundError:
        raise FileNotFoundError(f'{word_list} not found.')
    except sqlite3.Error:
        raise