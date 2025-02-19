# biblioteca de utilidades utilizdas na aplicação.

import hashlib
import base64
import datetime

# retorna a data e o tempo atual.
def now():
  return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# limpa a tela do console.
def clear_console():
  print('\033[2J', end='')
  print('\033[H', end='')

# calcula o hash do arquivo especificado.
def calcular_hash(arquivo):
    with open(arquivo, 'rb') as f:
        hash = hashlib.sha256()
        while chunk := f.read(4096):
            hash.update(chunk)
    return hash.hexdigest()

# criptografa os dados de hash com a senha
def criptografar_hash(hash, senha):
    senha_bytes = senha.encode()
    hash_bytes = hash.encode()
    criptografado = base64.b64encode(hash_bytes + senha_bytes)
    return criptografado.decode()

# descriptografar dados de hash com a senha
def descriptografar_hash(criptografado, senha):
    criptografado_bytes = criptografado.encode()
    senha_bytes = senha.encode()
    hash_bytes = base64.b64decode(criptografado_bytes)[:-len(senha_bytes)]
    return hash_bytes.decode()