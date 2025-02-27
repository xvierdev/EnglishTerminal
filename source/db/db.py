import sqlite3
import util

def insert_user(name, password):
    try:
        with sqlite3.connect('users.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    nome TEXT PRIMARY KEY,
                    password TEXT
                )
            ''')

            hashed_password = util.hash_text(password)
            cursor.execute("INSERT OR IGNORE INTO users (nome, password) VALUES (?, ?)", (name, hashed_password))
            conexao.commit()
            print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao inserir dados: {erro}")

def read_user(name):
    try:
        with sqlite3.connect('users.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM users WHERE nome = ?", (name,))
            user = cursor.fetchone()
            if user:
                print(f"Usuário encontrado: {user}")
                return user
            else:
                print("Usuário não encontrado.")
                return None

    except sqlite3.Error as erro:
        print(f"Erro ao ler dados: {erro}")
        return None

def update_user(name, new_password):
    try:
        with sqlite3.connect('users.db') as conexao:
            cursor = conexao.cursor()
            hashed_password = util.hash_text(new_password)
            cursor.execute("UPDATE users SET password = ? WHERE nome = ?", (hashed_password, name))
            conexao.commit()
            if cursor.rowcount > 0:
                print("Senha atualizada com sucesso!")
            else:
                print("Usuário não encontrado ou senha não alterada.")

    except sqlite3.Error as erro:
        print(f"Erro ao atualizar dados: {erro}")

def delete_user(name):
    try:
        with sqlite3.connect('users.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM users WHERE nome = ?", (name,))
            conexao.commit()
            if cursor.rowcount > 0:
                print("Usuário deletado com sucesso!")
            else:
                print("Usuário não encontrado.")

    except sqlite3.Error as erro:
        print(f"Erro ao deletar dados: {erro}")