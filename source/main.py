def menu():
    try:
        while True:
            print('Hello')
    except KeyboardInterrupt as e:
        print('User interrupt, bye!')
        
if __name__ == '__main__':
    menu()