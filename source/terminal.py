from logs import read
from main import game

command = input("bash@englishterminal: ")

while True:

    if command == 'game':
        print("GAME!!")
        game()
        break

    elif command == 'logs':
        read()
        command = input("bash@englishterminal: ")

    elif command == 'exit':
        #oi eu sou um abacaxi
        break

    else:
        print("command not found")
        command = input("bash@englishterminal: ")
    
