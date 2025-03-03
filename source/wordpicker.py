import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "db" / "main.db"

def get_random_word():
    """Retorna uma palavra aleatória do banco de dados main.db."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT english, portuguese FROM words ORDER BY RANDOM() LIMIT 1')
            word = cursor.fetchone()
            if word:
                return word
            else:
                return None

    except (sqlite3.Error, FileNotFoundError) as e:
        print(f'Erro: {e}')
        return None

# Exemplo de uso
word = get_random_word()
if word:
    ingles, traducao = word
    print(f"Palavra em inglês: {ingles}")
    print(f"Tradução: {traducao}")
else:
    print("Não foi possível obter uma palavra do banco de dados.")
    
if __name__ == 'main':
    get_random_word()
