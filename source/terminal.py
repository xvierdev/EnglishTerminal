from logs import read, add, add_undate, format, read_records
from main import game
import colors

username = 'bash'

print("Welcome to EnglishTerminal!")
print("well if you were scared by that black screen... well... This is only for advanced users, who want to learn in a different way, so it may not be for you. The commands are in the readme.")

print("Simple Commands:")
print("neofetch: ...")
print("logs: serves to see all your progress")
print("logs -r: warning⚠ erases all your progress")
print("game: start the game")

while True:
    
    command = input(f"{colors.RESET}{username}@englishterminal ~>{colors.CYAN} ")

    if command == 'game':
        print("GAME!!")
        game()  # Agora o jogo roda e volta ao terminal

    elif command == 'logs':
        print(read())

    elif command == 'logs -f':
        format()

    elif command == 'logs -r':
        read_records()

    elif command == 'exit':
        break  # Sai do terminal corretamente

    elif command == 'neofetch':
        print(f"{colors.RESET}|||||||||||||||||||||")
        print(f"{colors.RESET}|||{colors.MAGENTA}/{colors.BLACK}/////////////{colors.RESET}||||")
        print(f"{colors.RESET}||{colors.MAGENTA}//{colors.BLACK}//{colors.MAGENTA}//////////{colors.RESET}|||||")
        print(f"{colors.RESET}||{colors.MAGENTA}||{colors.BLACK}//{colors.MAGENTA}/{colors.RESET}||||||||||||||")
        print(f"{colors.RESET}||{colors.MAGENTA}||{colors.BLACK}//{colors.MAGENTA}/{colors.RESET}||||||||||||||")
        print(f"{colors.RESET}||{colors.MAGENTA}||{colors.BLACK}/////////////{colors.RESET}||||")
        print(f"{colors.RESET}||{colors.MAGENTA}||{colors.BLACK}//{colors.MAGENTA}//////////{colors.RESET}|||||")
        print(f"{colors.RESET}||{colors.MAGENTA}||{colors.BLACK}//{colors.MAGENTA}/{colors.RESET}||||||||||||||")
        print(f"{colors.RESET}||{colors.MAGENTA}||{colors.BLACK}//{colors.MAGENTA}/{colors.RESET}||||||||||||||")
        print(f"{colors.RESET}||{colors.MAGENTA}||{colors.BLACK}/////////////{colors.RESET}||||")
        print(f"{colors.RESET}||{colors.MAGENTA}//////////////{colors.RESET}|||||")
        print(f"{colors.RESET}|||||||||||||||||||||")
        #Imprime na tela...

    elif command == 'user -a':
        print(f"{colors.YELLOW}new user")
        username = input(f"{colors.RESET}user name:{colors.BLUE} ")
        userpassword = input(f"{colors.RESET}user password:{colors.GREEN} ")
        add_undate(f'user name: {username} and user pasword: {userpassword}')

    elif command == 'user -e':
        if read() <= 'user name: and user pasword:':
            print(f"{colors.YELLOW}there are local users, you can get more information in the log file.")

            username2 = input(f"username:{colors.BLUE} ")
            userpassword = input(f"user password:{colors.GREEN}")

            if username2 == f'user name: {username2} and user pasword: {userpassword}':
                print("access allowed")
                username = username2
            else:
                print("access not allowed")

    elif command == 'user -r':
        print("infelizmente está função não existe ainda")
        print("caso você queira remover um usuário entre no arquivo users.txt")
        print("bem se você abriu este repositório só apetando na pasta onde ele está, depois em source, o arquivo provavelmente pode estar na pasta do seu usuário em users(ou usuários)")
        print("a única coisa que dar para fazer a respeito do user -r é sentar e esperar, mas não se preocupe todo dia tem atualizações👍")

    else:
        print(f"{colors.RED}command not found")