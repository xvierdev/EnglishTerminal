import sqlite3
import db.sql as sql, logging

def create_tables(db_file):
    '''Creates the necessary tables if they don't exist.'''
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(sql.create_table)
            cursor.execute(sql.user_index)            
            logging.info(f"Table Users has been created successfully.")
            cursor.execute(sql.create_words)
            cursor.execute(sql.words_index)
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
        raise FileNotFoundError(f'{WORDLIST_FILE} not found.')
    except sqlite3.Error:
        raise
