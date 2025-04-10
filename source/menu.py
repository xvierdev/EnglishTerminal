# applications menu
import util

def main_menu():
    print('choose your option:')
    print('1 - game')
    print('2 - records')
    print('3 - about')
    print('q - exit')
    op = input('> ')
    util.clear_console()
    print(f'Selected: {op}')
    return op

def game_menu():
    print('choose your option:')
    print('1 - vocabulary')
    print('2 - weekdays')
    print('3 - mounts')
    print('4 - pronouns')
    print('5 - numbers')
    print('m - back to main menu')
    print('q - exit')
    op = input('> ')
    util.clear_console()
    print(f'Selected: {op}')
    return op

def records():
    print('Records features is not implemented!')
    print()

def invalid_option(op):
    print()
    print(f'"{op}" is an invalid option.')
    print()

def quit():
    print('Bye! See you later ... :D')
    print()
    exit()

if __name__ == '__main__':
    quit()
