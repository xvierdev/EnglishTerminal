# Script de utilidades, obtenção do tempo a atual, criptografia e calculo de hash.

import hashlib
import base64
import datetime
import random

#==============COLORS==============#

BLACK = "\033[30m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

#===============UTIL===============#

# Retorna a data e hora formatadas.
def now():
  return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Limpa a tela do console.
def clear_console():
  print('\033[2J', end='')
  print('\033[H', end='')

def print_multicolor(text):
  colors = ["\033[34m", "\033[36m", "\033[32m", "\033[35m", "\033[31m", "\033[33m"]
  print(RESET, end='')
  for i in range(len(text)):
    print(f'{random.choice(colors)}{text[i]}', end='')
  print(RESET)
  

# Report de bugs

def report_bug(error_msg):
    try:
        with open('error_log.txt', 'a', encoding="utf-8") as file:
            file.write(f'{now()} {error_msg}\n')
            print(f'Error: {error_msg}')
    except Exception as e:
        print(f"Erro ao reportar bug: {e}")


#===========CRIPTOGRAFIA===========#

# Calcula o hash do arquivo informado.
def calcular_hash(arquivo):
    try:
      with open(arquivo, 'rb') as f:
          hash = hashlib.sha256()
          while chunk := f.read(4096):
              hash.update(chunk)
      return hash.hexdigest()
    except Exception as e:
       report_bug(e)

# Salva o hash criptografado no arquivo hash.txt
def criptografar_hash(hash, senha):
    try:
      senha_bytes = senha.encode()
      hash_bytes = hash.encode()
      criptografado = base64.b64encode(hash_bytes + senha_bytes)
      return criptografado.decode()
    except Exception as e:
      report_bug(e)

# Descriptografa o hash do arquivo de hash.
def descriptografar_hash(criptografado, senha):
    try:
      criptografado_bytes = criptografado.encode()
      senha_bytes = senha.encode()
      hash_bytes = base64.b64decode(criptografado_bytes)[:-len(senha_bytes)]
      return hash_bytes.decode()
    except Exception as e:
      report_bug(e)