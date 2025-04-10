import logging, os, urllib.request as request
import db.create_table as dbmanager

def get_path(filename):
    '''Gets the path of the filename file in same directory as the executable.'''
    # appdata_dir = os.getenv('APPDATA')
    # if not appdata_dir:
    appdata_dir = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(appdata_dir, 'EnglishTerminal', filename)
    os.makedirs(os.path.dirname(database_path), exist_ok=True)
    return database_path

DB_FILE = get_path('main.db')
WORD_LIST = get_path('wordlist.txt')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word_list(url='https://english-terminal.vercel.app/wordlist.txt'):
    '''Baixa um arquivo da URL fornecida usando urllib e o salva no caminho de destino.'''
    try:
        request.urlretrieve(url, WORD_LIST)
        logging.info('Word list downloaded successfully.')
    except Exception as e:
        logging.error(str(e))

def make_database():
    dbmanager.create_tables(DB_FILE)
    dbmanager.populate_words(DB_FILE, WORD_LIST)

if __name__ == '__main__':
    get_word_list()
    make_database()
