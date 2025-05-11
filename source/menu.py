# applications menu
import keyboard
import os
from user import User


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def getch():
    """Lê um único evento de tecla e retorna o caractere (usando a biblioteca keyboard)."""
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name not in ["1", "2", "3", "4", "5", "6", "m", "q", "esc"]:
                continue
            elif event.name in ["q", "esc"]:
                quit()
            return event.name


def login():
    nick = ""
    while nick.strip() == "":
        nick = input("Digite seu nick:")
    user = User(nick, 0)
    return user


def main_menu():
    """
    Menu Principal da aplicação.

    Returns:
        chr: A opção escolhida pelo usuário
    """
    print("╔" + 54 * "═" + "╗")
    print("║" + 19 * " " + "English Terminal" + 19 * " " + "║")
    print("╚" + 54 * "═" + "╝")
    print("[1] Jogar  [2] Recordes  [3] Login  [4] Sobre  [q] Sair")
    op = getch()
    clear_screen()
    return op


def game_menu():
    """
    Menu dos jogos.

    Returns:
        chr: A opção escolhida pelo usuário
    """
    print("╔" + 111 * "═" + "╗")
    print("║" + 49 * " " + "Menu de Jogos" + 49 * " " + "║")
    print("╚" + 111 * "═" + "╝")
    print(
        "Escolha um jogo: [1] Vocabulário  [2] Dias da Semana  [3] Meses  [4] Pronomes  [5] Números  [m] Voltar  [q] Sair"
    )
    op = getch()
    clear_screen()
    return op


def records(user=None):
    if user is not None:
        clear_screen()
        print("user: ", user.get_nick())
        print("record: ", user.get_points())


def invalid_option(op):
    print()
    print(f'"{op}" é uma opção inválida.')
    print()
    input("Pressione Enter para continuar...")  # Usar input aqui para pausar
    clear_screen()


def quit(user=User("noName", 0)):
    print(f"Tchau {user.get_nick()}! Até a próxima ... :D")
    print()
    exit()
