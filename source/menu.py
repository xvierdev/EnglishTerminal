# applications menu
import keyboard
import os
from user import User

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def getch():
    """Lê um único evento de tecla e retorna o caractere (usando a biblioteca keyboard)."""
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name not in ['1', '2', '3', '4', '5', '6', 'm', 'q', 'esc']:
                continue
            elif event.name in ['q', 'esc']:
                quit()
            return event.name

def login():
    nick = ''
    while(nick.strip()==''):
        nick = input('Digite seu nick:')
    user = User(nick, 0)
    return user

def main_menu():
    """
    Menu Principal da aplicação.

    Returns:
        chr: A opção escolhida pelo usuário
    """
    print('╔═══════════════════════════════════════════════════════╗')
    print('║                   English Terminal                    ║')
    print('╚═══════════════════════════════════════════════════════╝')
    print('[1] Jogar  [2] Recordes  [3] Login  [4] Sobre  [q] Sair')
    op = getch()
    clear_screen()
    return op

def game_menu():
    """
    Menu dos jogos.

    Returns:
        chr: A opção escolhida pelo usuário
    """
    print('╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗')
    print('║                                              Menu de Jogos                                                   ║')
    print('╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝')
    print('Escolha um jogo: [1] Vocabulário  [2] Dias da Semana  [3] Meses  [4] Pronomes  [5] Números  [m] Voltar  [q] Sair')
    op = getch()
    clear_screen()
    return op

def records(user=None):
    if user!= None:
        clear_screen()
        print('user: ', user.get_nick())
        print('record: ', user.get_points())

def invalid_option(op):
    print()
    print(f'"{op}" é uma opção inválida.')
    print()
    input("Pressione Enter para continuar...") # Usar input aqui para pausar
    clear_screen()

def quit(user = User('noName', 0)):
    print(f'Tchau {user.get_nick()}! Até a próxima ... :D')
    print()
    exit()



# FIM DO MENU

# if __name__ == '__main__':
#     """TESTE DOS MENUS"""
    # while True:
    #     op_main = main_menu()
    #     if op_main == '1':
    #         while True:
    #             op_game = game_menu()
    #             if op_game == '1':
    #                 print("Iniciando jogo de Vocabulário...")
    #                 input("Pressione Enter para continuar...")
    #                 if os.name == 'nt':
    #                     os.system('cls')
    #                 else:
    #                     os.system('clear')
    #                 # Chamar a função vocabulary.game() aqui
    #             elif op_game == '2':
    #                 print("Iniciando jogo de Dias da Semana...")
    #                 input("Pressione Enter para continuar...")
    #                 if os.name == 'nt':
    #                     os.system('cls')
    #                 else:
    #                     os.system('clear')
    #                 # Chamar a função weekdays.weekday_translation_game() aqui
    #             elif op_game == '3':
    #                 print("Iniciando jogo de Meses...")
    #                 input("Pressione Enter para continuar...")
    #                 if os.name == 'nt':
    #                     os.system('cls')
    #                 else:
    #                     os.system('clear')
    #                 # Chamar a função months.month_translation_game() aqui
    #             elif op_game == '4':
    #                 print("Iniciando jogo de Pronomes...")
    #                 input("Pressione Enter para continuar...")
    #                 if os.name == 'nt':
    #                     os.system('cls')
    #                 else:
    #                     os.system('clear')
    #                 # Chamar a função pronoun.translate_pronouns() aqui
    #             elif op_game == '5':
    #                 print("Iniciando jogo de Números...")
    #                 input("Pressione Enter para continuar...")
    #                 if os.name == 'nt':
    #                     os.system('cls')
    #                 else:
    #                     os.system('clear')
    #                 # Chamar a função numbers.number_translation_game() aqui
    #             elif op_game == 'm':
    #                 break # Volta para o menu principal
    #             elif op_game == 'q':
    #                 quit()
    #             else:
    #                 invalid_option(op_game)
    #     elif op_main == '2':
    #         records()
    #     elif op_main == '3':
    #         print("Sobre o English Terminal...")
    #         print("Este é um aplicativo de aprendizado de inglês.")
    #         input("Pressione Enter para continuar...")
    #         if os.name == 'nt':
    #             os.system('cls')
    #         else:
    #             os.system('clear')
    #     elif op_main == 'q':
    #         quit()
    #     else:
    #         invalid_option(op_main)