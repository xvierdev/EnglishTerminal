# main application file
from modules import vocabulary, weekdays, months, pronoun, numbers
import menu
import about
import util
import db.create_table as db
import sqlite3
import logging

# Classes

from user import User

# Initial config for log events
logging.basicConfig(
    level=logging.INFO,
    filename=util.get_path("logs.log"),
    format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
)

user = None


def main():
    try:
        user = User("noname", 0)
        while True:
            op = menu.main_menu()
            if op in ["q", "Q"]:
                menu.quit()
            else:
                match op:
                    case "1":
                        op = menu.game_menu()
                        match op:
                            case "1":
                                vocabulary.game(user)
                            case "2":
                                weekdays.weekday_translation_game()
                            case "3":
                                months.month_translation_game()
                            case "4":
                                pronoun.translate_pronouns()
                            case "5":
                                numbers.number_translation_game()
                            case "m":
                                menu.main_menu()
                            case "q":
                                menu.quit(user)
                            case _:
                                menu.invalid_option(op)
                    case "2":
                        menu.records(user)
                    case "3":
                        user = menu.login()
                        db.create_user(user, util.get_path(util.DB_FILE))
                    case "4":
                        about.about()
                    case _:
                        menu.invalid_option(op)
    except KeyboardInterrupt:
        print("User interrupt. Bye!")
        logging.info("User interrupt")
    except (sqlite3.Error, FileNotFoundError) as e:
        print(str(e))
        logging.error(str(e))


if __name__ == "__main__":
    util.get_word_list()
    util.make_database()
    main()
