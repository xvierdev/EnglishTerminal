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
    word = strings() # variável word se torna o return da string
    answer = input(f'Whats is {word}?') # aqui a variável answer vai receber a resposta digitada do teclado
    if answer == 'livro': # essa linha vai testar se a pessoa acertou a resposta
        print('Thats right!') # aqui é o congratulations do acerto
        points += 1 # nesta linha aumenta a pontuação em +1
    else: # aqui é caso a resposta esteja errada
        print('It\'s wrong.') # imprime a mensagem de erro na tela
        print(f'Points {points}') # mostra a pontuação final
        input('Press enter to quit') # aguarda o usuário apertar enter
        break # para o loop e o programa fecha