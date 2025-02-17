from wordpicker import strings # Import da função de consultar wordlist
from logs import add, report_bug
from colors import RED, RESET, CYAN, YELLOW, GREEN # texto formatado com cores

import util

"""
O script faz o seguinte:

Procura palavras no arquivo wordlist.txt
Transformas todas as palavras em um array
Aplica uma palavra do array aleatóriamente na var "word"
Pede a resposta da palavra em português de forma literal
Caso acerte, incrementa um ponto
Caso errado, para o loop, mostra seus pontos e fecha
"""

points = 0      # a pontuação inicial do jogador é zero
lifes = 5       # vidas do jogador
player_name = input("Enter your name: ")
print(f"Welcome {player_name}!")

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
                util.limpar_terminal()
                print(f'{RED}GAME OVER!{RESET}');
                print(f'Your earn {YELLOW}{points}{RESET} points!')
            add(f'Player {player_name} error! word:{word} | translate:{result} | player:{answer}')

        add(f'Player {points} points.')
    except ValueError as error:
        report_bug(str(error))
        input('Press "Enter" to quit.')
        break

