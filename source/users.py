import sqlite3
import util
from pathlib import Path

DB_FILE = Path(__file__).parent / "db" / "main.db"

def create_user(login, password):
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (user, password) VALUES (?, ?)", (login, password))
            connection.commit()
            print("Data inserted successfully!")
            return True
    except sqlite3.Error as error:
        print(f"Error inserting data: {error}")
        return False
        
def read_user(login, password):
    try:
        with sqlite3.connect(DB_FILE) as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM users WHERE user = ? AND password = ?", (login, password))
            user = cursor.fetchone()
            if user:
                print("User successfully authenticated!")
                return True
            else:
                print("Invalid user or password.")
                return None
    except sqlite3.Error as erro:
        print(f"Error retrieving user: {erro}")
        
def remove_user(login):
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE user = ?", (login,))
            connection.commit()
            print("User successfully removed!")
    except sqlite3.Error as error:
        print(f"Error removing user: {error}")
        
def update_user_password(login, old_password, new_password):
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET password = ? WHERE user = ? AND password = ?", (new_password, login, old_password))
            connection.commit()
            print("Password updated successfully!")
            return True
    except sqlite3.Error as error:
        print(f"Error updating password: {error}")
        return False
        
def show_users():
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            print("Users:")
            for user in users:
                print(user)
    except sqlite3.Error as error:
        print(f"Error retrieving users: {error}")
        
def get_user_id(login):
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM users WHERE user = ?", (login,))
            user_id = cursor.fetchone()
            if user_id:
                return user_id[0]
            return None
    except sqlite3.Error as error:
        print(f"Error retrieving user ID: {error}")
        return None

if __name__ == '__main__':
    create_user('admin', util.hash('admin'))
    read_user('admin', util.hash('admin'))
    update_user_password('admin', util.hash('admin'), util.hash('admin123'))
    # remove_user('admin')
    show_users()
    print(get_user_id('admin'))
    