import msvcrt
import util

def getch():
    """Lê um único caractere do teclado sem precisar pressionar Enter (apenas Windows)."""
    return msvcrt.getch().decode('utf-8')

def main_menu():
    print('╔════════════════════════════════════════════════════════════════╗')
    print('║                       English Terminal                         ║')
    print('╚════════════════════════════════════════════════════════════════╝')
    print('Selecione uma opção: [1] Jogar  [2] Recordes  [3] Sobre  [q] Sair')
    op = getch().lower()  # Lê um único caractere e converte para minúsculo
    print(f'\nVocê selecionou: {op}') # Adiciona uma nova linha para separar a seleção do menu
    util.clear_console() # Pode ser problemático com getch, talvez precise ajustar
    return op

def game_menu():
    print('╔═════════════════════╗')
    print('║    Menu de Jogos    ║')
    print('╚═════════════════════╝')
    print('Escolha um jogo: [1] Vocabulário  [2] Dias da Semana  [3] Meses  [4] Pronomes  [5] Números  [m] Voltar  [q] Sair')
    op = getch().lower()
    print(f'\nVocê selecionou: {op}')
    util.clear_console() # Pode ser problemático com getch, talvez precise ajustar
    return op

def records():
    print('Recurso de Recordes não implementado!')
    print()

def invalid_option(op):
    print()
    print(f'"{op}" é uma opção inválida.')
    print()

def quit():
    print('Tchau! Até a próxima ... :D')
    print()
    exit()

if __name__ == '__main__':
    op_main = main_menu()
    if op_main == '1':
        game_menu()
    elif op_main == '2':
        records()
    elif op_main == '3':
        # Lógica para 'Sobre'
        pass
    elif op_main == 'q':
        quit()
    else:
        invalid_option(op_main)