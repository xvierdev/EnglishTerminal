import create_table, util
import menu, about, write_log as log
import modules.wordpicker
def main ():
    try:
        while(True):
            op = menu.main_menu()
            if op in ['q', 'Q'] : break
            elif op == '1':
                op = menu.game_menu()
                if op == '1':
                    modules.wordpicker.game()
                elif op == 'q': break
            elif op == '3': about.about()
    except KeyboardInterrupt:
        print('User interrupt. Bye!')
        log.write_log('User interrupt', 'INFO', module=__file__)

if __name__ == '__main__':
    main()
    create_table.main()