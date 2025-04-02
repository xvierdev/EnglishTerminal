# main application file
import modules.weekdays
import menu, about, util
import modules.vocabulary
import sqlite3, logging

logging.basicConfig(level=logging.INFO, filename=util.get_path('logs.log'), format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

def main ():
    try:
        while(True):
            op = menu.main_menu()
            if op in ['q', 'Q'] : break
            else:
                match op:
                    case '1':
                        op = menu.game_menu()
                        match op:
                            case '1': modules.vocabulary.game()
                            case '2': modules.weekdays.weekday_translation_game()
                            case 'q': exit()
                            case   _: menu.invalid_option(op)
                    case '3': about.about()
                    case 'q': exit()
                    case   _: menu.invalid_option(op)
    except KeyboardInterrupt:
        print('User interrupt. Bye!')
        logging.info('User interrupt')
    except (sqlite3.Error, FileNotFoundError) as e:
        print(str(e))
        logging.error(str(e))

if __name__ == '__main__':
    main()