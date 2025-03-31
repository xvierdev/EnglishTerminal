def menu ():
    try:
        op = ''
        while(op != '2'):
            print('Escolha uma opção: ')
            print('1 - iniciar o jogo')
            print('2 - sair')
            op = input('> ')
        print('Bye')
    except KeyboardInterrupt as e:
        print('User interrupt. Bye!')

if __name__ == '__main__':
    menu()