import os, urllib.request as request
import write_log as log

def get_path(filename):
    '''Gets the path of the filename file in the same directory as the executable.'''
    appdata_dir = os.getenv('APPDATA')
    database_path = os.path.join(appdata_dir, 'EnglishTerminal', filename)
    os.makedirs(os.path.dirname(database_path), exist_ok=True)
    return database_path

DB_FILE = get_path('main.db')
WORD_LIST = get_path('wordlist.txt')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word_list(url):
    '''Baixa um arquivo da URL fornecida usando urllib e o salva no caminho de destino.'''
    try:
        request.urlretrieve(url, WORD_LIST)
        log.write_log('Word list downloaded successfully.', 'INFO', module=__name__)
    except Exception as e:
        log.write_log(e, 'ERROR', module=__name__)

if __name__ == '__main__':
    get_word_list('https://english-terminal.vercel.app/wordlist.txt')
