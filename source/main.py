import menu
def main ():
    try:
        while(True):
            op = menu.main_menu()
            if op in ['q', 'Q'] : break
    except KeyboardInterrupt:
        print('User interrupt. Bye!')

if __name__ == '__main__':
    main()