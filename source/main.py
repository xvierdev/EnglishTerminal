from wordpicker import strings # Import da função de consultar wordlist
from logs import add, report_bug
from clear import cls

# Códigos de cores
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

"""
O script faz o seguinte:

Procura palavras no arquivo wordlist.txt
Transforma todas as palavras em um array
Aplica uma palavra do array aleatóriamente na var "word"
Pede a resposta da palavra em português de forma literal
Caso acerte, incrementa um ponto e mostra seus pontos
Caso errado, decrementa sua vida
Ao ficar sem vida, para o loop e pergunta se quer jogar de novo
"""


def game():
    while True:  # Loop principal do jogo
        print(RESET) # Bug fix provisório
        cls()
        points = 0  # Pontuação inicial
        life = 5  # Vidas do jogador
        question = 0
        player_name = input("Enter your name: ").capitalize()
        print(f"Welcome {player_name}!")

        while life > 0:
            question += 1
            print(f"Question: {question}")
            text = strings()
            try:
                word, result = text.split(' ')
                answer = input(f'What is the translation of {YELLOW}"{word}"{RESET}? ')
                if answer.lower() == result:
                    points += 1
                    print(f"That's right! You have {CYAN}{points} point(s)!{RESET}")
                else:
                    life -= 1
                    print(f"It's wrong. Translation of {RED}{word}{RESET} is {YELLOW}\"{result}\"{RESET}.")
                    if life > 0:
                        print(f"{GREEN}{life} lives{RESET} remaining.")
                    else:
                        cls()
                        print(f"{RED}GAME OVER!{RESET}")
                add(f"Player {player_name} error! word:{word} | translation:{result} | player:{answer}")
                add(f"Player {points} points.")

            except ValueError as error:
                report_bug(str(error))
                input('Press "Enter" to quit.')
                break  # Sai do jogo caso haja erro

        # Opção para reiniciar ou sair
        restart = input(f"{player_name}, wanna restart the game? ({GREEN}Y{RESET}/n) ").lower()
        if restart == "n":
            break  # Sai do loop e encerra o jogo