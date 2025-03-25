import sqlite3
import util, logs_writer

DB_FILE = util.get_path('main.db')

def create_user(login, password):
    """Creates a new user in the database."""
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Users (user, password) VALUES (?, ?)", (login, password)) #Corrected table name to Users
            connection.commit()
            logs_writer.write_log(f"User '{login}' created successfully.", level="INFO", module=__file__)
            print("User created successfully!")
            return True
    except sqlite3.Error as error:
        logs_writer.write_log(f"Error creating user '{login}': {error}", level="ERROR", module=__file__)
        print(f"Error creating user: {error}")
        return False

def read_user(login, password):
    """Authenticates a user by checking login and password."""
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE user = ? AND password = ?", (login, password)) #Corrected table name to Users
            user = cursor.fetchone()
            if user:
                logs_writer.write_log(f"User '{login}' authenticated successfully.", level="INFO", module=__file__)
                print("User successfully authenticated!")
                return True
            else:
                logs_writer.write_log(f"Authentication failed for user '{login}'.", level="WARNING", module=__file__)
                print("Invalid user or password.")
                return False
    except sqlite3.Error as error:
        logs_writer.write_log(f"Error retrieving user '{login}': {error}", level="ERROR", module=__file__)
        print(f"Error retrieving user: {error}")
        return False

def remove_user(login):
    """Removes a user from the database."""
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Users WHERE user = ?", (login,)) #Corrected table name to Users
            connection.commit()
            logs_writer.write_log(f"User '{login}' removed successfully.", level="INFO", module=__file__)
            print("User successfully removed!")
            return True
    except sqlite3.Error as error:
        logs_writer.write_log(f"Error removing user '{login}': {error}", level="ERROR", module=__file__)
        print(f"Error removing user: {error}")
        return False

def update_user_password(login, old_password, new_password):
    """Updates a user's password in the database."""
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE Users SET password = ? WHERE user = ? AND password = ?", (new_password, login, old_password)) #Corrected table name to Users
            connection.commit()
            logs_writer.write_log(f"Password updated successfully for user '{login}'.", level="INFO", module=__file__)
            print("Password updated successfully!")
            return True
    except sqlite3.Error as error:
        logs_writer.write_log(f"Error updating password for user '{login}': {error}", level="ERROR", module=__file__)
        print(f"Error updating password: {error}")
        return False

def show_users():
    """Displays all users in the database."""
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users")  #Corrected table name to Users
            users = cursor.fetchall()
            print("Users:")
            for user in users:
                print(user)
            logs_writer.write_log("Displayed all users.", level="INFO", module=__file__)
            return True
    except sqlite3.Error as error:
        logs_writer.write_log(f"Error retrieving users: {error}", level="ERROR", module=__file__)
        print(f"Error retrieving users: {error}")
        return False

def get_user_id(login):
    """Retrieves the user ID for a given login."""
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM Users WHERE user = ?", (login,)) #Corrected table name to Users
            user_id = cursor.fetchone()
            if user_id:
                logs_writer.write_log(f"Retrieved user ID for '{login}': {user_id[0]}", level="INFO", module=__file__)
                return user_id[0]
            logs_writer.write_log(f"User '{login}' not found.", level="WARNING", module=__file__)
            print("User not found.")
            return None
    except sqlite3.Error as error:
        logs_writer.write_log(f"Error retrieving user ID for '{login}': {error}", level="ERROR", module=__file__)
        print(f"Error retrieving user ID: {error}")
        return None

if __name__ == '__main__':
    #Example USAGE
    try:
      create_user('admin', util.hash('admin'))
      read_user('admin', util.hash('admin'))
      update_user_password('admin', util.hash('admin'), util.hash('admin123'))
      # remove_user('admin')
      show_users()
      print(get_user_id('admin'))
    except Exception as e:
       logs_writer.write_log(f"Error: {e}", level="ERROR", module=__file__)