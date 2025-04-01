# main application file
import modules.weekdays
import create_table, util
import menu, about, write_log as log
import modules.vocabulary
import sqlite3

def main ():
    try:
        create_table.create_tables()
        create_table.populate_words()
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
                    case '3': about.about()
                    case 'q': break
                    case   _: menu.invalid_option(op)
    except KeyboardInterrupt:
        print('User interrupt. Bye!')
        log.write_log('User interrupt', 'INFO', module=__file__)
    except (sqlite3.Error, FileNotFoundError) as e:
        print(str(e))
        log.write_log(e, 'ERROR', module=__name__)


if __name__ == '__main__':
    main()