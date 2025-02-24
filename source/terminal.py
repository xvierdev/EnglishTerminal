import logs  # Manipulação de logs do programa.
import main  # Módulo principal do game.
import util  # Utilidades de tempo e criptografia
import source.recordS as recordS  # Modulo de gerenciamento de records.

print("Welcome to EnglishTerminal!")
print("This is only for advanced users, who want to learn in a different way.")  # Simplifique a mensagem
print("Commands are in the readme.")  # Deixe claro onde encontrar os comandos

print("Simple Commands:")
print("neofetch: ...")
print("logs: see your progress")  # Descrição mais concisa
print("game: start the game")
print("help: show command list")

while True:
    command = input(f"{util.RESET}englishterminal ~>{util.CYAN} ")

    if command == 'game':
        print(f"{util.YELLOW}GAME!!")
        main.game()  # Chame a função game() do módulo main

    elif command == 'logs':
        print(logs.read_log())  # Chame a função read() do módulo logs

    elif command == 'records':
        for record in recordS.load_records():
            print(record, end='')
        print() # Adiciona uma nova linha após imprimir os records

    elif command == 'exit':
        print(f'{util.YELLOW}bye!{util.RESET}')
        break

    elif command in ('clear', 'cls'):  # Simplifique a verificação
        util.clear_console()  # Chame a função clear_console() do módulo util

    elif command == 'help':
        print("comandos:")
        print("neofetch: like linux's neofetch")
        print("exit: i left the terminal correctly")
        print("logs -f: deletes everything from the logs file")
        print("logs: shows everything in the logs file")
        print("game: start the game")
        

    elif command == 'neofetch':
        #tivemos que voltar :(
        print(f"{util.RESET}|||||||||||||||||||||")
        print(f"{util.RESET}|||{util.MAGENTA}/{util.BLACK}/////////////{util.RESET}||||")
        print(f"{util.RESET}||{util.MAGENTA}//{util.BLACK}//{util.MAGENTA}//////////{util.RESET}|||||")
        print(f"{util.RESET}||{util.MAGENTA}||{util.BLACK}//{util.MAGENTA}/{util.RESET}||||||||||||||")
        print(f"{util.RESET}||{util.MAGENTA}||{util.BLACK}//{util.MAGENTA}/{util.RESET}||||||||||||||")
        print(f"{util.RESET}||{util.MAGENTA}||{util.BLACK}/////////////{util.RESET}||||")
        print(f"{util.RESET}||{util.MAGENTA}||{util.BLACK}//{util.MAGENTA}//////////{util.RESET}|||||")
        print(f"{util.RESET}||{util.MAGENTA}||{util.BLACK}//{util.MAGENTA}/{util.RESET}||||||||||||||")
        print(f"{util.RESET}||{util.MAGENTA}||{util.BLACK}//{util.MAGENTA}/{util.RESET}||||||||||||||")
        print(f"{util.RESET}||{util.MAGENTA}||{util.BLACK}/////////////{util.RESET}||||")
        print(f"{util.RESET}||{util.MAGENTA}//////////////{util.RESET}|||||")
        print(f"{util.RESET}|||||||||||||||||||||")

#vamos deixar isso de entrar no usuário mais tarde
#elif command == 'user -a':
#        print(f"{util.YELLOW}new user")
#        username = input(f"{util.RESET}user name:{util.BLUE} ")
#        userpassword = input(f"{util.RESET}user password:{util.GREEN} ")
#        logs.add_user(f'user name: {username} and user password: {userpassword}') # Corrigido o erro de digitação

#elif command == 'user -e':
#    if logs.read_users():
#        print(f"{util.YELLOW}There are local users. See the log file for details.")
#        username2 = input(f"{util.RESET}User name:{util.BLUE} ")
#        userpassword = input(f"{util.RESET}User password:{util.GREEN} ")
#        stored_credentials = logs.read_users() # Supondo que logs.read() retorna as credenciais armazenadas
#        if f'user name: {username2} and user password: {userpassword}' in stored_credentials:
#            print(f"{util.GREEN}Access allowed")
#            username = username2
#        else:
#            print(f"{util.RED}Access not allowed")
#    else:
#        print(f"{util.YELLOW}No users found.")


#    elif command == 'user -r':
#        print("This feature is not yet implemented.") # Mensagem mais profissional
#        print("To remove a user, edit the users.txt file directly.")
#        print("The file is likely located in your user's directory within the 'users' folder.")
#        print("Updates are frequent. Stay tuned! 👍")

    else:
        print(f"{util.RED}Command not found{util.RESET}")