# biblioteca de utilidades
import hashlib
import base64

from datetime import datetime

def now():
  return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def clear_console():
  """Limpa o terminal usando ANSI escape codes (Unix)."""
  print('\033[2J', end='')  # Limpa a tela
  print('\033[H', end='')  # Posiciona o cursor no início

def calcular_hash(arquivo):
    with open(arquivo, 'rb') as f:
        hash = hashlib.sha256()
        while chunk := f.read(4096):
            hash.update(chunk)
    return hash.hexdigest()

def criptografar_hash(hash, senha):
    senha_bytes = senha.encode()
    hash_bytes = hash.encode()
    criptografado = base64.b64encode(hash_bytes + senha_bytes)
    return criptografado.decode()

def descriptografar_hash(criptografado, senha):
    criptografado_bytes = criptografado.encode()
    senha_bytes = senha.encode()
    hash_bytes = base64.b64decode(criptografado_bytes)[:-len(senha_bytes)]
    return hash_bytes.decode()