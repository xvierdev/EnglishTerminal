# biblioteca de utilidades
def limpar_terminal():
  """Limpa o terminal usando ANSI escape codes (Unix)."""
  print('\033[2J', end='')  # Limpa a tela
  print('\033[H', end='')  # Posiciona o cursor no início