import sqlite3, util
from pathlib import Path

DB_FILE = Path(__file__).parent / "db" / "main.db"

def insert_record(username, record):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE user = ?", (username,))
            userid=cursor.fetchone()[0]        
            cursor.execute('INSERT INTO records (user_id, date_time, record) VALUES (?, ?, ?)', (userid, util.now(), record))
            conn.commit()
    except Exception as e:
        print(e)
        
def show_records():
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM records ORDER BY record DESC LIMIT 5")
            records = cursor.fetchall()
            print("Records:")
            for i, record in enumerate(records, start=1):
                cursor.execute("SELECT user FROM users WHERE id = ?", (record[1],))
                username = cursor.fetchone()[0]
                print(f"| {i} - {username} | Points: {record[3]} | Date: {record[2].split(' ')[0]} | Time: {record[2].split(' ')[1]} |")
            print()
    except Exception as e:
        print(e)
            
def clear_records():
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM records")
            conn.commit()
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    clear_records()
    insert_record("admin", 100)
    insert_record("admin", 200)
    insert_record("admin", 300)
    insert_record("admin", 400)
    show_records()