import hashlib
import datetime
import os
import sqlite3
import logs_writer
import urllib

def get_path(filename):
    """Obtém o caminho do arquivo main.db no mesmo diretório do executável."""
    #Obtém o nome do sistema operacional
    SO = os.name

    # Obtém o caminho do diretório %APPDATA%
    if SO == "nt":
        appdata_dir_windows = os.getenv('APPDATA')
    else:
        appdata_dir_linux = os.path.expanduser('~/.local/share')

    # Cria o caminho completo para o arquivo do banco de dados
    if SO == "nt":
        database_path = os.path.join(appdata_dir_windows, 'EnglishTerminal', filename)

        # Cria o diretório se ele não existir
        os.makedirs(os.path.dirname(database_path), exist_ok=True)
    else:
        database_path = os.path.join(appdata_dir_linux, 'EnglishTerminal', filename)
        os.makedirs(os.path.dirname(database_path), exist_ok=True)

    return database_path

DB_FILE = get_path('main.db')
WORD_LIST = get_path('wordlist.txt')

def now():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def clear_console():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def increment_user_points(user, points):
    if user:
        try:
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT points FROM Users WHERE user = ?', (user,))
                result = cursor.fetchone()
                if result:
                    total_points = int(result[0] if result[0] else 0) + points
                    cursor.execute('UPDATE Users SET points = ? WHERE user = ?', (total_points, user))
                else:
                    print (f"Usuario {user} nao encontrado")
                conn.commit() # importante para salvar a alteração no banco de dados.
        except sqlite3.Error as e:
            print(f'Error: {e}')
            logs_writer.write_log(e, "ERROR", __file__)

def read_user_points(username):
    if username:
        points = 0
        try:
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                corrent_points = cursor.execute('SELECT points FROM Users WHERE user = ?', (username,)).fetchone()[0]
                points = int(corrent_points if corrent_points else 0)
        except sqlite3.Error as e:
            print(f'Error: {e}')
            logs_writer.write_log(e, "ERROR", __file__)
        except TypeError as e:
            print(f'Error {e}')
            logs_writer.write_log(e, "ERROR", __file__)
        finally:
            return points

import urllib.request

def get_word_list(url):
    """Baixa um arquivo da URL fornecida usando urllib e o salva no caminho de destino."""
    try:
        urllib.request.urlretrieve(url, WORD_LIST)
        msg = f"Arquivo baixado com sucesso e salvo em: {WORD_LIST}"
        print(msg)
        logs_writer.write_log(msg, "INFO", __name__)
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
        logs_writer.write_log(e, "ERROR", __name__)
