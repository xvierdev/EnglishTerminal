points = 0      # a pontuação inicial do jogador é zero
while(True):    # mantém o programa em loop indefinidamente
    word = 'book' # primeira palavra que o jogador precisa acertar
    answer = input(f'Whats is {word}?') # aqui a variável answer vai receber a resposta digitada do teclado
    if answer == 'livro': # essa linha vai testar se a pessoa acertou a resposta
        print('Thats hight!') # aqui é o congratulations do acerto
        points += 1 # nesta linha aumenta a pontuação em +1
    else: # aqui é caso a resposta esteja errada
        print('It\'s wrong.') # imprime a mensagem de erro na tela
        print(f'Points {points}') # mostra a pontuação final
        input('Press enter to quit') # aguarda o usuário apertar enter
        break # para o loop e o programa fecha