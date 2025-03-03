from pathlib import Path
import sqlite3

def create_table_users(cursor):
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        ''')
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_user ON Users (user);")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela usuarios: {e}")

def create_table_records(cursor):
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                date_time TEXT NOT NULL,
                record INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
            );
        ''')
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_recordes_user_id ON Records (user_id);")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela recordes: {e}")

def create_table_words(cursor):
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Words (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                english TEXT UNIQUE NOT NULL,
                portuguese TEXT NOT NULL
            );
        ''')
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_words_english ON Words (english);")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela palavras: {e}")

def main():
    db_file = Path(__file__).parent / "main.db"
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            create_table_users(cursor)
            create_table_records(cursor)
            create_table_words(cursor)
            conn.commit()
            print("Tabelas criadas com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ou executar comandos no banco de dados: {e}")

if __name__ == "__main__":
    main()