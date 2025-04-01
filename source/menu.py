# applications menu
def main_menu():
    print('choose your option:')
    print('1 - game')
    print('2 - records')
    print('3 - about')
    print('q - exit')
    return input('> ')

def game_menu():
    print('choose your option:')
    print('1 - vocabulary')
    print('2 - weekdays')
    print('3 - mounts')
    print('4 - pronouns')
    print('5 - numbers')
    print('m - back to main menu')
    print('q - exit')
    return input('> ')

def invalid_option(op):
    print()
    print(f'"{op}" is an invalid option.')
    print()

if __name__ == '__main__':
    main_menu()