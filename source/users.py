import sqlite3
import util
from pathlib import Path

DB_FILE = Path(__file__).parent / "db" / "main.db"

def create_user(login, password):
    try:
        with sqlite3.connect(DB_FILE) as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO users (user, password) VALUES (?, ?)", (login, password))
            conexao.commit()
            print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao inserir dados: {erro}")
        
def read_user(login, password):
    try:
        with sqlite3.connect(DB_FILE) as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM users WHERE user = ? AND password = ?", (login, password))
            user = cursor.fetchone()
            if user:
                print("Usuário autenticado com sucesso!")
                return True
            else:
                print("Usuário ou senha incorretos.")
                return None
    except sqlite3.Error as erro:
        print(f"Erro ao buscar usuário: {erro}")
        
def remove_user(login):
    try:
        with sqlite3.connect(DB_FILE) as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM users WHERE user = ?", (login,))
            conexao.commit()
            print("Usuário removido com sucesso!")
    except sqlite3.Error as erro:
        print(f"Erro ao remover usuário: {erro}")
        
def update_user_password(login, old_password, new_password):
    try:
        with sqlite3.connect(DB_FILE) as conexao:
            cursor = conexao.cursor()
            cursor.execute("UPDATE users SET password = ? WHERE user = ? AND password = ?", (new_password, login, old_password))
            conexao.commit()
            print("Senha atualizada com sucesso!")
            return True
    except sqlite3.Error as erro:
        print(f"Erro ao atualizar senha: {erro}")
        
def show_users():
    try:
        with sqlite3.connect(DB_FILE) as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            print("Usuários:")
            for user in users:
                print(user)
    except sqlite3.Error as erro:
        print(f"Erro ao buscar usuários: {erro}")
        
def get_user_id(login):
    try:
        with sqlite3.connect(DB_FILE) as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id FROM users WHERE user = ?", (login,))
            user_id = cursor.fetchone()
            if user_id:
                return user_id[0]
            return None
    except sqlite3.Error as erro:
        print(f"Erro ao buscar id do usuário: {erro}")

if __name__ == '__main__':
    create_user('admin', util.hash('admin'))
    read_user('admin', util.hash('admin'))
    update_user_password('admin', util.hash('admin'), util.hash('admin123'))
    # remove_user('admin')
    show_users()
    print(get_user_id('admin'))
    