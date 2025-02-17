# biblioteca de utilidades
from datetime import datetime

def now():
  return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def clear_console():
  """Limpa o terminal usando ANSI escape codes (Unix)."""
  print('\033[2J', end='')  # Limpa a tela
  print('\033[H', end='')  # Posiciona o cursor no início