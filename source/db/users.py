# CRUD de usuários do sistema.

import sqlite3

# Insere novos usuários no banco de dados.
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

            cursor.execute("INSERT INTO users (nome, password) VALUES (?, ?)", (name, password))
            conexao.commit()
            print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        return(f"Erro ao inserir dados: {erro}")

# Verifica a existência e a senha do usuário.
def read_user(name, password):
    try:
        with sqlite3.connect('users.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM users WHERE nome = ? AND password = ?", (name,password))
            user = cursor.fetchone()
            if user:
                print(f"Usuário encontrado: {user}")
                return user
            else:
                print("Usuário não encontrado ou senha inválida.")
                return None

    except sqlite3.Error as erro:
        print(f"Erro ao ler dados: {erro}")
        return None

# Atualiza a senha do usuário válido.
def update_user(name, new_password):
    try:
        with sqlite3.connect('users.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("UPDATE users SET password = ? WHERE nome = ?", (new_password, name))
            conexao.commit()
            if cursor.rowcount > 0:
                return("Senha atualizada com sucesso!")
            else:
                return("Usuário não encontrado ou senha não alterada.")

    except sqlite3.Error as erro:
        return(f"Erro ao atualizar dados: {erro}")

# Remove um usuário do banco de dados.
def delete_user(name):
    try:
        with sqlite3.connect('users.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM users WHERE nome = ?", (name,))
            conexao.commit()
            if cursor.rowcount > 0:
                return("Usuário deletado com sucesso!")
            else:
                return("Usuário não encontrado.")

    except sqlite3.Error as erro:
        print(f"Erro ao deletar dados: {erro}")