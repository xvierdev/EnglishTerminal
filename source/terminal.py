from logs import read
from main import game

# Códigos de cores
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLACK = "\033[30m"
RESET = "\033[0m"

while True:
    command = input(f"{RESET}bash@englishterminal ~>{CYAN} ")
    if command == 'game':
        print("GAME!!")
        game()  # Agora o jogo roda e volta ao terminal

    elif command == 'logs':
        read()

    elif command == 'exit':
        break  # Sai do terminal corretamente

    elif command == 'neofetch':
        print(f"{RESET}|||||||||||||||||||||")
        print(f"{RESET}|||{MAGENTA}/{BLACK}/////////////{RESET}||||")
        print(f"{RESET}||{MAGENTA}//{BLACK}//{MAGENTA}//////////{RESET}|||||")
        print(f"{RESET}||{MAGENTA}||{BLACK}//{MAGENTA}/{RESET}||||||||||||||")
        print(f"{RESET}||{MAGENTA}||{BLACK}//{MAGENTA}/{RESET}||||||||||||||")
        print(f"{RESET}||{MAGENTA}||{BLACK}/////////////{RESET}||||")
        print(f"{RESET}||{MAGENTA}||{BLACK}//{MAGENTA}//////////{RESET}|||||")
        print(f"{RESET}||{MAGENTA}{MAGENTA}||{BLACK}//{MAGENTA}/{RESET}||||||||||||||")
        print(f"{RESET}||{MAGENTA}||{BLACK}//{MAGENTA}/{RESET}||||||||||||||")
        print(f"{RESET}||{MAGENTA}||{BLACK}/////////////{RESET}||||")
        print(f"{RESET}||{MAGENTA}//////////////{RESET}|||||")
        print(f"{RESET}|||||||||||||||||||||")
        #Imprime na tela...
        
    else:
        print("command not found")
