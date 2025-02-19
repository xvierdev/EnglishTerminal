import logs  # Manipulação de logs do programa.
import main  # Módulo principal do game.
import colors  # Cores na saída do terminal.
import util  # Utilidades de tempo e criptografia
import records_manager  # Modulo de gerenciamento de records.

username = 'bash'

print("Welcome to EnglishTerminal!")
print("This is only for advanced users, who want to learn in a different way.")  # Simplifique a mensagem
print("Commands are in the readme.")  # Deixe claro onde encontrar os comandos

print("Simple Commands:")
print("neofetch: ...")
print("logs: see your progress")  # Descrição mais concisa
print("logs -r: WARNING! Erases all your progress")  # Destaque o aviso
print("game: start the game")
print("help: show command list")

while True:
    command = input(f"{colors.RESET}{username}@englishterminal ~>{colors.CYAN} ")

    if command == 'game':
        print("GAME!!")
        main.game()  # Chame a função game() do módulo main

    elif command == 'logs':
        print(logs.read())  # Chame a função read() do módulo logs

    elif command == 'logs -f':
        logs.format()  # Chame a função format() do módulo logs

    elif command == 'records':
        for record in records_manager.load_records():
            print(record, end='')
        print() # Adiciona uma nova linha após imprimir os records

    elif command == 'exit':
        print(f'{colors.YELLOW}bye!{colors.RESET}')
        break

    elif command in ('clear', 'cls'):  # Simplifique a verificação
        util.clear_console()  # Chame a função clear_console() do módulo util

    elif command == 'help':
        print('To be implemented.')  # Mensagem mais profissional
        # TODO: Implementar a funcionalidade help

    elif command == 'neofetch':
        # Simplifique o neofetch usando um loop ou string formatada
        lines = ["|||||||||||||||||||||",
                 "|||{}//////////////{}{}".format(colors.MAGENTA, colors.BLACK, colors.RESET),
                 "||{}/{}//{}///////////{}{}".format(colors.MAGENTA, colors.BLACK, colors.MAGENTA, colors.RESET),
                 "||{}/{}//{}/{}//{}{}".format(colors.MAGENTA, colors.BLACK, colors.MAGENTA, colors.RESET),
                 "||{}/{}//{}/{}//{}{}".format(colors.MAGENTA, colors.BLACK, colors.MAGENTA, colors.RESET),
                 "||{}//////////////{}{}".format(colors.MAGENTA, colors.BLACK, colors.RESET),
                 "||{}/{}//{}///////////{}{}".format(colors.MAGENTA, colors.BLACK, colors.MAGENTA, colors.RESET),
                 "||{}/{}//{}/{}//{}{}".format(colors.MAGENTA, colors.BLACK, colors.MAGENTA, colors.RESET),
                 "||{}/{}//{}/{}//{}{}".format(colors.MAGENTA, colors.BLACK, colors.MAGENTA, colors.RESET),
                 "||{}//////////////{}{}".format(colors.MAGENTA, colors.BLACK, colors.RESET),
                 "||{}//////////////{}{}".format(colors.MAGENTA, colors.RESET),
                 "|||||||||||||||||||||"]

        for line in lines:
            print(line)

    elif command == 'user -a':
        print(f"{colors.YELLOW}new user")
        username = input(f"{colors.RESET}user name:{colors.BLUE} ")
        userpassword = input(f"{colors.RESET}user password:{colors.GREEN} ")
        logs.add_undate(f'user name: {username} and user password: {userpassword}') # Corrigido o erro de digitação

    elif command == 'user -e':
        # Corrigido o erro de digitação na comparação e lógica mais clara
        if logs.read(): # Verifica se o arquivo não está vazio
            print(f"{colors.YELLOW}There are local users. See the log file for details.")
            username2 = input(f"{colors.RESET}Username:{colors.BLUE} ")
            userpassword = input(f"{colors.RESET}User password:{colors.GREEN} ")

            # Aqui você precisa de uma forma segura de verificar as credenciais.
            # Armazenar senhas em texto plano é extremamente inseguro.
            # Considere usar hashing de senha (bcrypt, scrypt, etc.).
            # Este exemplo é apenas ilustrativo e INSEGURO:
            stored_credentials = logs.read() # Supondo que logs.read() retorna as credenciais armazenadas
            if f'user name: {username2} and user password: {userpassword}' in stored_credentials:
                print("Access allowed")
                username = username2
            else:
                print("Access not allowed")
        else:
            print(f"{colors.YELLOW}No users found.")


    elif command == 'user -r':
        print("This feature is not yet implemented.") # Mensagem mais profissional
        print("To remove a user, edit the users.txt file directly.")
        print("The file is likely located in your user's directory within the 'users' folder.")
        print("Updates are frequent. Stay tuned! 👍")

    else:
        print(f"{colors.RED}Command not found{colors.RESET}")