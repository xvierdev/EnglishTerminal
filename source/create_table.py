import sqlite3, sql
import util, write_log as log

DB_FILE = util.get_path('main.db')
WORDLIST_FILE = util.get_path('wordlist.txt')

def create_tables(cursor):
    '''Creates the necessary tables if they don't exist.'''
    try:
        cursor.execute(sql.create_table)
        cursor.execute(sql.user_index)
        log.write_log("Table Users has been created successfully.", level="INFO", module=__file__)
        cursor.execute(sql.create_words)
        cursor.execute(sql.words_index)
        log.write_log("Table Words has been created successfully.", level="INFO", module=__file__)
        return True
    except sqlite3.Error as e:
        log.write_log(f"Error creating tables: {e}", level="ERROR", module=__file__)
        return False

def populate_words(cursor):
    '''Populates the Words table from wordlist.txt.'''
    try:
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

            cursor.execute('DELETE FROM Words')
            cursor.executemany("INSERT OR IGNORE INTO Words (english, portuguese, category) VALUES (?, ?, ?)", data_to_insert)
            log.write_log(f"{cursor.rowcount} Words inserted/ignored.", level="INFO", module=__file__)
            return True
    except FileNotFoundError:
        log.write_log(f"Error: File '{WORDLIST_FILE}' not found.", level="ERROR", module=__file__)
        return False
    except sqlite3.Error as e:
        log.write_log(f"Error inserting words: {e}", level="ERROR", module=__file__)
        return False

def main():
    '''Connects to the database, creates tables, and populates the Words table.'''
    success = False
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()

            if create_tables(cursor):
                log.write_log("Tables creation process started", level="INFO", module=__file__)
                if populate_words(cursor):
                    conn.commit()  # Commit only if words were inserted successfully
                    log.write_log("Words inserted successfully and commited.", level="INFO", module=__file__)
                    success = True
                else:
                    log.write_log("Words insertion failed", level="ERROR", module=__file__)
            else:
                log.write_log("Table creation failed", level="ERROR", module=__file__)

    except sqlite3.Error as e:
        log.write_log(f"Error connecting to the database: {e}", level="ERROR", module=__file__)

if __name__ == "__main__":
    main()