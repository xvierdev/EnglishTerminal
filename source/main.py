import getpass, sys
import logs_writer, util, about
import records, users
import db.create_table as first

from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent / 'modules'))

import weekdays, game_numbers, date_complete, wordpicker

DB_FILE = Path(__file__).parent / 'db' / "main.db"

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

    choice = input("> ")

    return choice

def play_game(username):
    """Presents the game menu and starts the chosen game."""
    points = 0
    while True:
        choice = game_menu()

        if choice == '1':
            logs_writer.write_log(f"User '{username}' started the Word Translation Game.", level="INFO", module=__file__)
            points = wordpicker.game() # Assuming the `game()` function is in wordpicker.py
            if points is not None:
              logs_writer.write_log(f"User '{username}' completed the game. Points: {points}", level="INFO", module=__file__)
              records.insert_record(username, points) # Add score to the database after the game finishes
              print("Records was added successfully!")
        elif choice == '2':
            logs_writer.write_log(f"User '{username}' started the Weekday Translation Game.", level="INFO", module=__file__)
            points = weekdays.weekday_translation_game()
            logs_writer.write_log(f"User '{username}' completed the game. Points: {points}", level="INFO", module=__file__)
            records.insert_record(username, points)
        elif choice == '3':
            logs_writer.write_log(f"User '{username}' started the Number Translation Game.", level="INFO", module=__file__)
            points = game_numbers.number_translation_game()
            logs_writer.write_log(f"User '{username}' completed the game. Points: {points}", level="INFO", module=__file__)
            records.insert_record(username, points)
        elif choice == '4':
            logs_writer.write_log(f"User '{username}' started the Date Translation Game.", level="INFO", module=__file__)
            points = date_complete.date_translation_game()
            logs_writer.write_log(f"User '{username}' completed the game. Points: {points}", level="INFO", module=__file__)
            records.insert_record(username, points)
        elif not choice:
            # User pressed Enter, return to main menu
            return
        else:
            print("Invalid choice. Please try again.")
        return points

def main():
    """Main application loop."""
    print('Welcome to English Terminal, input help to obtain help!')
    current_username = None
    while(True):
        input_command = input('> ')
        parts = input_command.split(' ')
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        if command.lower() in ['exit', 'quit']:
            print('Goodbye!')
            break

        elif command.lower() in ['cls', 'clear']:
            util.clear_console()

        elif command.lower() == 'help':
            print('Command list:')
            print('exit or quit: close the terminal')
            print('clear, cls: clear the terminal')
            print('hash: generate a hash of a text')
            print('now, agora: show the current date and time')
            print('addusr or add: add a new user')
            print('auth or authenticate or login or enter: authenticate a user')
            print('updusr or update: update the password of a user')
            print('logout or leave: logout the current user')
            print('game: Start a translation game')
            print('records [clear]: Show or clear game records')
            print('about: About section')

        elif command.lower() == 'hash':
            text = ' '.join(args)
            print(f'Hash of "{text}":')
            print(util.hash(' '.join(args)))

        elif command.lower() in ['addusr', 'add']:
            username = input('Username: ')
            if ' ' in username:
                print('Username cannot contain spaces.')
                continue
            password = getpass.getpass('Password: ')
            if users.create_user(username, util.hash(password)):
                print('User created successfully!')

        elif command.lower() in ['auth', 'authenticate', 'login', 'enter']:
            current_username = login()
            if current_username:
                print(f'Logged in as {current_username}.')

        elif command.lower() in ['updusr', 'update']:
            if not current_username:
                print('You must be logged in to update your password.')
            else:
                old_password = getpass.getpass('Old password: ')
                new_password = getpass.getpass('New password: ')
                users.update_user_password(current_username, util.hash(old_password), util.hash(new_password))

        elif command.lower() in ['logout', 'leave']:
            current_username = None
            print('Logged out.')

        elif command.lower() in ['now', 'agora']:
            print(f'Current date and time: {util.now()}')

        elif command.lower() == 'game':
            if current_username:
                points = play_game(current_username)  # Call the game and capture the points
                util.increment_user_points(current_username, points)

            else:
                print("You must log in to play the game.")

        elif command.lower() in ['records', 'record']:
            if 'clear' in args:
                records.clear_records()
            else:
                records.show_records()

        elif command.lower() in ['point', 'points', 'pontos']:
            if not current_username:
                print('Loging to view points.')
            else:
                points = util.read_user_points(current_username)
                print(f'{current_username} have {points}')

        elif command.lower() in ['about', 'sobre']:
            about.about()

        else:
            print('Invalid command. Type help for help.')

if __name__ == '__main__':
    if first.main():
        main()
    else:
        print(f'See logs for details.')