#Este script é responsável pela gravação e recuperação dos logs de informação e de erro durante a execução do programa.

from util import now

# definição dos nomes padrão dos arquivos de log.
DEFAULT_LOG_FILE = 'log.txt'
DEFAULT_ERROR_LOG_FILE = 'error_log.txt'

# Operadores de log

def read_log():
    """Lê o conteúdo do arquivo de log."""
    try:
        with open(DEFAULT_LOG_FILE, 'r', encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        with open(DEFAULT_LOG_FILE, 'w', encoding="utf-8") as log_file:
            pass
    except Exception as e:
        report_bug(e)
        return f"Erro ao ler arquivo de log: {e}"

def add_log_info(message):
    """Adiciona uma mensagem ao arquivo de log."""
    try:
        with open(DEFAULT_LOG_FILE, 'a', encoding="utf-8") as file:
            file.write(f'{now()} {message}\n')
    except Exception as e:
        report_bug(e)
        print(f"Erro ao adicionar log: {e}")

def clear_log():
    """Limpa o conteúdo do arquivo de log."""
    try:
        with open(DEFAULT_LOG_FILE, 'w', encoding="utf-8"):
            pass
    except Exception as e:
        report_bug(e)

# Log específico para reportar bugs

def report_bug(error_msg):
    """Registra uma mensagem de erro no arquivo de log de erros e informa o usuário."""
    try:
        with open(DEFAULT_ERROR_LOG_FILE, 'a', encoding="utf-8") as file:
            file.write(f'{now()} {error_msg}\n')
            print(f'Error: {error_msg}')
    except Exception as e:
        print(f"Erro ao reportar bug: {e}")