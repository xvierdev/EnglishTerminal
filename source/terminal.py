import logs     # Manipulação de logs do programa.
import main     # Módulo principal do game.
import util     # Utilidades de tempo e criptografia
import records  # Modulo de gerenciamento de records.
import about    # Sobre os desenvolvedores do projeto.

util.clear_console()
util.print_multicolor("Welcome to EnglishTerminal!")

print("This is only for advanced users, who want to learn in a different way.")  # Simplifique a mensagem
print("Commands are in the readme.")  # Deixe claro onde encontrar os comandos

print(f"{util.YELLOW}Simple Commands:{util.RESET}")
print("neofetch: ...")
print("records: see current records.")  # Descrição mais concisa
print("game: start the game")
print("help: show command list")

while True:
    command = input(f"{util.RESET}englishterminal ~>{util.CYAN} ")

    if command == 'game':
        print(f"{util.YELLOW}GAME!!")
        main.game()  # Chame a função game() do módulo main

    elif command == 'logs':
        for log_line in logs.read_log():
            print(log_line, end='')

    elif command == 'records':
        for record in records.load_records():
            print(record, end='')
        print() # Adiciona uma nova linha após imprimir os records

    elif command == 'exit':
        print(f'{util.YELLOW}bye!{util.RESET}')
        break

    elif command in ('clear', 'cls'):  # Simplifique a verificação
        util.clear_console()  # Chame a função clear_console() do módulo util

    elif command == 'help':
        print("comandos:")
        print("game: start the game")
        print("records: see current records.")
        print("logs: shows everything in the logs file")
        print("neofetch: like linux's neofetch")
        print("logs -f: deletes everything from the logs file")
        print("exit: i left the terminal correctly")
        

    elif command == 'neofetch':
        about.neofetch()

    else:
        print(f"{util.RED}Command not found{util.RESET}")