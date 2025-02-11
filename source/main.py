from wordpicker import strings # Import da função de consultar wordlist
"""
O script faz o algoritmo seguinte:

Procura palavras no arquivo wordlist.txt
Transformas todas as palavras em um array
Aplica uma palavra do array aleatóriamente na var "word"
Pede a resposta da palavra em português de forma literal
Caso acerte, incrementa um ponto
Caso errado, para o loop, mostra seus pontos e fecha
"""
# TODO: respostas de acordo com a string escolhida

points = 0      # a pontuação inicial do jogador é zero
while(True):    # mantém o programa em loop indefinidamente
    text = strings()
    word, result = text.split(' ') # variável word se torna o return da string
    answer = input(f'Whats is {word}? ') # aqui a variável answer vai receber a resposta digitada do teclado
    if answer == result: # essa linha vai testar se a pessoa acertou a resposta
        points += 1 # nesta linha aumenta a pontuação em +1
        print(f'That\'s right! You earn {points}') # aqui é o congratulations do acerto
    else: # aqui é caso a resposta esteja errada
        print(f'It\'s wrong. {word} is "{result}"') # imprime a mensagem de erro na tela
        print(f'Points {points}') # mostra a pontuação final
        input('Press enter to quit\n') # aguarda o usuário apertar enter
        break # para o loop e o programa fecha