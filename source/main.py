points = 0
while(True):
    word = 'book'
    answer = input(f'Whats is {word}?')
    if answer == 'livro':
        print('Thats hight!')
        points += 1
    else:
        print('It\'s wrong.')