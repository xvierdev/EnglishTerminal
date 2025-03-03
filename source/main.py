import util
import about, records, users
import getpass

def login():
    trytimes = 3
    while trytimes > 0:
        username = input('Username: ')
        password = getpass.getpass('Password: ')
        if users.read_user(username, util.hash(password)):
            return username
        trytimes -= 1
        print(f'Invalid username or password. {trytimes} attempts remaining.')
    print('Too many failed attempts. Try again later.')
    return None

def main():
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
            
        elif command.lower() == 'hash':
            text = ' '.join(args)
            print(f'Hash of "{text}":')
            print(util.hash(' '.join(args)))
            
        elif command.lower() in ['addusr', 'add']:
            while(True):
                username = input('Username: ')
                if ' ' in username:
                    print('Username cannot contain spaces.')
                    continue
                password = getpass.getpass('Password: ')
                if users.create_user(username, util.hash(password)):
                    break
            
        elif command.lower() in ['auth', 'authenticate', 'login', 'enter']:
            current_username = login()
            if current_username:
                print(f'Logged in as {current_username}.')
                
        elif command.lower() in ['updusr', 'update']:
            if not current_username:
                print('You must be logged in to update your password.')
                print(current_username)
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
            pass
        
        elif command.lower() in ['logs', 'log']:
            pass
        
        elif command.lower() in ['records', 'record']:
            if 'clear' in args:
                records.clear_records()
            else:
                records.show_records()
        
        elif command.lower() in ['about', 'sobre']:
            about.about()
            
        else:
            print('Invalid command. Type help for help.')
        
if __name__ == '__main__':
    main()