# main application file
from modules import vocabulary, weekdays, months, pronoun, numbers
import menu, about, util
import sqlite3, logging

# Classes

from user import User

# Initial config for log events
logging.basicConfig(level=logging.INFO, filename=util.get_path('logs.log'), format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

def main ():
    try:
        user = User('generic', 'noname', 0)
        while(True):
            op = menu.main_menu()
            if op in ['q', 'Q'] : menu.quit()
            else:
                match op:
                    case '1':
                        op = menu.game_menu()
                        match op:
                            case '1': vocabulary.game()
                            case '2': weekdays.weekday_translation_game()
                            case '3': months.month_translation_game()
                            case '4': pronoun.translate_pronouns()
                            case '5': numbers.number_translation_game()
                            case 'q': menu.quit(user)
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