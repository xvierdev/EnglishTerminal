from wordpicker import strings # Import da função de consultar wordlist
from logs import add_log, report_bug
from colors import RED, RESET, CYAN, YELLOW, GREEN # texto formatado com cores

import util, records_manager, os

"""
O script faz o seguinte:

Procura palavras no arquivo wordlist.txt
Transformas todas as palavras em um array
Aplica uma palavra do array aleatóriamente na var "word"
Pede a resposta da palavra em português de forma literal
Caso acerte, incrementa um ponto
Caso errado, para o loop, mostra seus pontos e fecha
""" 
def game():

    points = 0      # a pontuação inicial do jogador é zero
    lifes = 5       # vidas do jogador

    util.clear_console
    player_name = input("Enter your name user: ")
    print(f"{RED}Welcome {YELLOW}{player_name}!{RESET}")
    print()

    for record in records_manager.load_records():
        if record == '':
            print('No records found!')
        else:
            print(record, end='')

    while(lifes > 0):
        text = strings()
        try:
            word, result = text.split(' ')
            answer = input(f'Whats is the translate of {YELLOW}"{word}"{RESET}? ')
            if answer.lower() == result:
                points += 1
                print(f'That\'s right! You have {CYAN}{points} point(s)!{RESET}')
            else:
                lifes -= 1
                print(f'It\'s wrong. Translate of {RED}{word}{RESET} is {YELLOW}"{result}"{RESET}.')
                if lifes > 0 :
                    print(f'{GREEN}{lifes} lives{RESET} remaining.')
                else:
                    util.clear_console()
                    print(f'{RED}GAME OVER!{RESET}');
                    if points > 1:
                        print(f'Your earn {YELLOW}{points}{RESET} points!')
                    elif points == 1:
                        print(f'Your earn {YELLOW}{points}{RESET} point!')
                    else:
                        print('You didn\'t earn any points.')
                    records_manager.write_records(player_name, points)
                add_log(f'Player {player_name} error! word:{word} | translate:{result} | player:{answer}')

            add_log(f'Player {points} points.')
        except ValueError as error:
            report_bug(str(error))
            input('Press "Enter" to quit.')
            break
