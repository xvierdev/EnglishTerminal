import sql, sqlite3
import util, write_log as log

DB_FILE = util.get_path('main.db')
WORDLIST_FILE = util.get_path('wordlist.txt')

def create_tables():
    '''Creates the necessary tables if they don't exist.'''
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor
        cursor.execute(sql.create_table)
        cursor.execute(sql.user_index)
        log.write_log("Table Users has been created successfully.", level="INFO", module=__file__)
        cursor.execute(sql.create_words)
        cursor.execute(sql.words_index)
        log.write_log("Table Words has been created successfully.", level="INFO", module=__file__)

def populate_words():
    '''Populates the Words table from wordlist.txt.'''
    with open(WORDLIST_FILE, 'r', encoding='utf-8') as wordlist:
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
                log.write_log(f"Skipping line due to incorrect format: {line_clean}", level="WARNING", module=__file__)
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor
            cursor.execute('DELETE FROM Words')
            cursor.executemany("INSERT OR IGNORE INTO Words (english, portuguese, category) VALUES (?, ?, ?)", data_to_insert)
            log.write_log(f"{cursor.rowcount} Words inserted/ignored.", level="INFO", module=__file__)

if __name__ == "__main__":
    create_tables()
    populate_words()