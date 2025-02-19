import os
from util import now

DEFAULT_LOG_FILE = 'log.txt'
DEFAULT_ERROR_LOG_FILE = 'error_log.txt'
DEFAULT_RECORDS_FILE = 'records.txt'
DEFAULT_USERS_FILE = 'users.txt'

def read_log(log_file=DEFAULT_LOG_FILE):
    """Lê o conteúdo do arquivo de log."""
    try:
        with open(log_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Arquivo de log '{log_file}' não encontrado."
    except Exception as e:
        return f"Erro ao ler arquivo de log: {e}"

def read_records(records_file=DEFAULT_RECORDS_FILE):
    """Lê o conteúdo do arquivo de registros."""
    try:
        with open(records_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Arquivo de registros '{records_file}' não encontrado."
    except Exception as e:
        return f"Erro ao ler arquivo de registros: {e}"

def add_log(message, level="INFO", log_file=DEFAULT_LOG_FILE):
    """Adiciona uma mensagem ao arquivo de log."""
    try:
        with open(log_file, 'a') as file:
            timestamp = now()
            log_entry = f"{timestamp} [{level}] {message}\n"
            file.write(log_entry)
    except Exception as e:
        print(f"Erro ao adicionar log: {e}")


def add_user(user_data, users_file=DEFAULT_USERS_FILE):
    """Adiciona dados de usuário ao arquivo de usuários."""
    try:
        with open(users_file, 'a') as file:
            file.write(user_data + '\n')
    except Exception as e:
        print(f"Erro ao adicionar usuário: {e}")

def report_bug(error_msg, error_log_file=DEFAULT_ERROR_LOG_FILE):
    """Registra uma mensagem de erro no arquivo de log de erros e informa o usuário."""
    try:
        with open(error_log_file, 'a') as file:
            file.write(f'{now()} {error_msg}\n')
        print(f'Ocorreu um erro. Mais detalhes em \'{error_log_file}\'.')
    except Exception as e:
        print(f"Erro ao reportar bug: {e}")

def clear_log(log_file=DEFAULT_LOG_FILE):
    """Limpa o conteúdo do arquivo de log."""
    try:
        with open(log_file, 'w'):
            pass  # Abre o arquivo em modo de escrita (sobrescreve)
    except Exception as e:
        print(f"Erro ao limpar log: {e}")