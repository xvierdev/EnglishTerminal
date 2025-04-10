# main application file
import modules.weekdays
import modules.vocabulary
import menu, about, util
import sqlite3, logging

logging.basicConfig(level=logging.INFO, filename=util.get_path('logs.log'), format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

def main ():
    try:
        while(True):
            op = menu.main_menu()
            if op in ['q', 'Q'] : menu.quit()
            else:
                match op:
                    case '1':
                        op = menu.game_menu()
                        match op:
                            case '1': modules.vocabulary.game()
                            case '2': modules.weekdays.weekday_translation_game()
                            case 'q': menu.quit()
                            case   _: menu.invalid_option(op)
                    case '2': menu.records()
                    case '3': about.about()
                    case   _: menu.invalid_option(op)
    except KeyboardInterrupt:
        print('User interrupt. Bye!')
        logging.info('User interrupt')
    except (sqlite3.Error, FileNotFoundError) as e:
        print(str(e))
        logging.error(str(e))

if __name__ == '__main__':
    util.get_word_list()
    util.make_database()
    main()