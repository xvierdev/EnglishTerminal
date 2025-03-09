import sqlite3
import util, logs_writer

DB_FILE = util.get_path('main.db')
WORDLIST_FILE = util.get_path('wordlist.txt')

def create_tables(cursor):
    """Creates the necessary tables if they don't exist."""
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                points INTEGER
            );
        ''')
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_user ON Users (user);")

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

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Words (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                english TEXT UNIQUE NOT NULL,
                portuguese TEXT NOT NULL,
                category TEXT NOT NULL
            );
        ''')
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_words_english ON Words (english);")

        logs_writer.write_log("Tables created successfully.", level="INFO", module=__file__)
        return True
    except sqlite3.Error as e:
        logs_writer.write_log(f"Error creating tables: {e}", level="ERROR", module=__file__)
        print(f"Error creating tables: {e}")
        return False

def populate_words(cursor):
    """Populates the Words table from wordlist.txt."""
    try:
        with open(WORDLIST_FILE, 'r', encoding='utf-8') as wordlist:
            data_to_insert = []
            for line in wordlist:
                line_clean = line.strip()
                if not line_clean or line_clean.startswith('#'):
                    continue

                parts = line_clean.split(' ', 2)  # Split into three parts
                if len(parts) == 3:
                    category, en_word, br_word = parts
                    data_to_insert.append((en_word, br_word, category))
                else:
                    logs_writer.write_log(f"Skipping line due to incorrect format: {line_clean}", level="WARNING", module=__file__)
                    print(f"Warning: Skipping line due to incorrect format: {line_clean}")

            cursor.executemany("INSERT OR IGNORE INTO Words (english, portuguese, category) VALUES (?, ?, ?)", data_to_insert)
            logs_writer.write_log(f"{cursor.rowcount} Words inserted/ignored.", level="INFO", module=__file__)
            return True
    except FileNotFoundError:
        logs_writer.write_log(f"Error: File '{WORDLIST_FILE}' not found.", level="ERROR", module=__file__)
        print(f"Error: File '{WORDLIST_FILE}' not found.")
        return False
    except sqlite3.Error as e:
        logs_writer.write_log(f"Error inserting words: {e}", level="ERROR", module=__file__)
        print(f"Error inserting words: {e}")
        return False

def main():
    """Connects to the database, creates tables, and populates the Words table."""
    success = False
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()

            if create_tables(cursor):
                logs_writer.write_log("Tables creation process started", level="INFO", module=__file__)
                # print("Tables created successfully!")
                if populate_words(cursor):
                    conn.commit()  # Commit only if words were inserted successfully
                    logs_writer.write_log("Words inserted successfully and commited.", level="INFO", module=__file__)
                    # print("Words inserted successfully!")
                    success = True
                else:
                    logs_writer.write_log("Words insertion failed", level="ERROR", module=__file__)
                    # print("Word insertion failed.")
            else:
                logs_writer.write_log("Table creation failed", level="ERROR", module=__file__)
                # print("Table creation failed.")

    except sqlite3.Error as e:
        logs_writer.write_log(f"Error connecting to the database: {e}", level="ERROR", module=__file__)
        print(f"Error connecting to the database: {e}")
    finally:
        return success

if __name__ == "__main__":
    main()