import sqlite3
import sql, logging, os

def get_path(filename):
    '''Gets the path of the filename file in the %APPDATA% Windows directory.'''
    appdata_dir = os.getenv('APPDATA')
    database_path = os.path.join(appdata_dir, 'EnglishTerminal', filename)
    os.makedirs(os.path.dirname(database_path), exist_ok=True)
    return database_path

# logging base config
logging.basicConfig(level=logging.INFO, filename=get_path('logs.log'), format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
module_name = os.path.basename(__file__)

DB_FILE = get_path('main.db')
WORDLIST_FILE = get_path('wordlist.txt')

def create_tables():
    '''Creates the necessary tables if they don't exist.'''
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute(sql.create_table)
            cursor.execute(sql.user_index)            
            logging.info(f"Table Users has been created successfully. (module: {module_name})")
            cursor.execute(sql.create_words)
            cursor.execute(sql.words_index)
            logging.info(f"Table Words has been created successfully. (module: {module_name})")
    except sqlite3.Error:
        raise

def populate_words():
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
                    logging.info(f"Skipping line due to incorrect format: {line_clean}")
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Words')
                cursor.executemany("INSERT OR IGNORE INTO Words (english, portuguese, category) VALUES (?, ?, ?)", data_to_insert)
                logging.info(f"{cursor.rowcount} Words inserted/ignored.")
    except FileNotFoundError:
        raise FileNotFoundError(f'{WORDLIST_FILE} not found.')
    except sqlite3.Error:
        raise

if __name__ == "__main__":
    # util.get_word_list('https://english-terminal.vercel.app/wordlist.txt') # obtain list for online application
    create_tables()
    # populate_words()
