import hashlib
import sqlite3

# Constantes
DB_FILE = 'records.db'

def calcular_hash(records):
    """Calcula o hash SHA-256 dos recordes."""
    records_str = ''.join([f"{r[0]} {r[1]} {r[2]}\n" for r in records])
    return hashlib.sha256(records_str.encode()).hexdigest()

def get_records_from_db():
    """Obtém os recordes do banco de dados."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT timestamp, name, points FROM records ORDER BY points DESC LIMIT 5")
            return cursor.fetchall()
    except sqlite3.Error:
        return []

def save_records_to_db(records):
    """Salva os recordes no banco de dados."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS records (
                    timestamp TEXT,
                    name TEXT,
                    points INTEGER
                )
            ''')
            cursor.execute("DELETE FROM records")  # Limpa os recordes antigos
            cursor.executemany("INSERT INTO records VALUES (?, ?, ?)", records)
            conn.commit()
    except sqlite3.Error:
        pass  # Lidar com erros aqui