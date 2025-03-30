import getpass
import logs_writer, util, about
import records, users, create_table

import modules.weekdays as weekdays
import modules.game_numbers as game_numbers
import modules.date_complete as date_complete
import modules.wordpicker as wordpicker

DB_FILE = util.get_path('main.db')

def login():
    """Authenticates a user."""
    trytimes = 3
    while trytimes > 0:
        username = input('Username: ')
        password = getpass.getpass('Password: ')
        if users.read_user(username, util.hash(password)):
            logs_writer.write_log(f"User '{username}' logged in successfully.", level="INFO", module=__file__)
            return username
        trytimes -= 1
        print(f'Invalid username or password. {trytimes} attempts remaining.')
    print('Too many failed attempts. Try again later.')
    logs_writer.write_log("Login failed after multiple attempts.", level="WARNING", module=__file__)
    return None

def game_menu():
    """Displays the available game options and returns the user's choice."""
    print("\n--- Game Menu ---")
    print("1. Word Translation Game")
    print("2. Weekday Translation Game")
    print("3. Number Translation Game")
    print("4. Date Translation Game")
    print("Enter the number of the game you want to play (or press Enter to return to the main menu):")

    choice = input("Game >> ")

    return choice

def play_game(username):
    """Presents the game menu and starts the chosen game."""
    points = 0
    while True:
        choice = game_menu()

        match choice:
            case'1':
                logs_writer.write_log(f"User '{username}' started the Word Translation Game.", level="INFO", module=__file__)
                points = wordpicker.game() # Assuming the `game()` function is in wordpicker.py
                if points is not None:
                  logs_writer.write_log(f"User '{username}' completed the game. Points: {points}", level="INFO", module=__file__)
                  records.insert_record(username, points) # Add score to the database after the game finishes
                  print("Records was added successfully!")
            case'2':
                logs_writer.write_log(f"User '{username}' started the Weekday Translation Game.", level="INFO", module=__file__)
                points = weekdays.weekday_translation_game()
                logs_writer.write_log(f"User '{username}' completed the game. Points: {points}", level="INFO", module=__file__)
                records.insert_record(username, points)
            case'3':
                logs_writer.write_log(f"User '{username}' started the Number Translation Game.", level="INFO", module=__file__)
                points = game_numbers.number_translation_game()
                logs_writer.write_log(f"User '{username}' completed the game. Points: {points}", level="INFO", module=__file__)
                records.insert_record(username, points)
            case'4':
                logs_writer.write_log(f"User '{username}' started the Date Translation Game.", level="INFO", module=__file__)
                points = date_complete.date_translation_game()
                logs_writer.write_log(f"User '{username}' completed the game. Points: {points}", level="INFO", module=__file__)
                records.insert_record(username, points)
            case"":
                # User pressed Enter, return to main menu
                return
            case _:
                print("Invalid choice. Please try again.")
                return points

def main():
    """Main application loop."""
    print('Welcome to English Terminal!')
    print('First create an account to be able to play. Use "add" to create')
    print('Then type "login" to enter your created account')
    print('Option list:')
    print('exit: close the terminal')
    print('cls: clear the terminal')
    print('hash: generate a hash of a text')
    print('now: show the current date and time')
    print('add: add a new user')
    print('login: authenticate a user')
    print('updusr: update the password of a user')
    print('logout: logout the current user')
    print('update: update word list')
    print('game: Start a translation game')
    print('records [clear]: Show or clear game records')
    print('about: About section')

    current_username = None
    while(True):
        input_command = input('EnglishTerminal >> ')
        parts = input_command.split(' ')
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        match input_command:
            case'exit':
                print('Goodbye!')
                break

            case'cls':
                util.clear_console()

            case'help':
                print('Option list:')
                print('exit: close the terminal')
                print('cls: clear the terminal')
                print('hash: generate a hash of a text')
                print('now: show the current date and time')
                print('add: add a new user')
                print('login: authenticate a user')
                print('updusr: update the password of a user')
                print('logout: logout the current user')
                print('update: update word list')
                print('game: Start a translation game')
                print('records [clear]: Show or clear game records')
                print('about: About section')

            case'hash':
                text = ' '.join(args)
                print(f'Hash of "{text}":')
                print(util.hash(' '.join(args)))

            case'add':
                username = input('Username: ')
                if ' ' in username:
                    print('Username cannot contain spaces.')
                    continue
                password = getpass.getpass('Password: ')
                users.create_user(username, util.hash(password))
                current_username = username

            case'login':
                current_username = login()
                if current_username:
                    print(f'Logged in as {current_username}.')

            case'updusr':
                if not current_username:
                    print('You must be logged in to update your password.')
                else:
                    old_password = getpass.getpass('Old password: ')
                    new_password = getpass.getpass('New password: ')
                    users.update_user_password(current_username, util.hash(old_password), util.hash(new_password))

            case'logout':
                current_username = None
                print('Logged out.')

            case'now':
                print(f'Current date and time: {util.now()}')

            case'game':
                if current_username:
                    points = play_game(current_username)  # Call the game and capture the points
                    util.increment_user_points(current_username, points)

                else:
                    print("You must log in to play the game.")

            case'records':
                if 'clear' in args:
                    records.clear_records()
                else:
                    records.show_records()

            case'points':
                if not current_username:
                    print('Loging to view points.')
                else:
                    points = util.read_user_points(current_username)
                    print(f'{current_username} have {points}')

            case'update':
                util.get_word_list('https://english-terminal.vercel.app/wordlist.txt')
                if create_table.main():
                    print('Successfully updated.')
                else:
                    print('Error.')
            

            case'about':
                about.about()

            case"":
                print()

            case _:
                print('Invalid option. Type help for help.')

if __name__ == '__main__':
    util.get_word_list('https://english-terminal.vercel.app/wordlist.txt')
    if create_table.main():
        main()
    else:
        print(f'See logs for details.')