import sqlite3
import util, logs_writer

DB_FILE = util.get_path('main.db')

def insert_record(username, record):
    """Inserts a new record for a user into the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM Users WHERE user = ?", (username,)) #Fixed table name to Users
            user_id_result = cursor.fetchone()
            if user_id_result:
                user_id = user_id_result[0]
                cursor.execute('INSERT INTO Records (user_id, date_time, record) VALUES (?, ?, ?)', (user_id, util.now(), record)) #Fixed table name to Records
                conn.commit()
                logs_writer.write_log(f"Record inserted for user '{username}': Record={record}", level="INFO", module=__file__)
                return True
            else:
                logs_writer.write_log(f"User '{username}' not found. Record insertion failed.", level="WARNING", module=__file__)
                print(f"User '{username}' not found.")
                return False

    except sqlite3.Error as e:
        logs_writer.write_log(f"Error inserting record for user '{username}': {e}", level="ERROR", module=__file__)
        print(f"Error inserting record: {e}")
        return False

def show_records():
    """Displays the top 5 records from the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Records ORDER BY record DESC LIMIT 5") #Fixed table name to Records
            records = cursor.fetchall()
            print("Records:")
            for i, record in enumerate(records, start=1):
                cursor.execute("SELECT user FROM Users WHERE id = ?", (record[1],)) #Fixed table name to Users
                username_result = cursor.fetchone()
                if username_result:
                  username = username_result[0]
                  print(f"| {i} - {username} | Points: {record[3]} | Date: {record[2].split(' ')[0]} | Time: {record[2].split(' ')[1]} |")
                else:
                  print(f"| {i} - Unknown User (ID: {record[1]}) | Points: {record[3]} | Date: {record[2].split(' ')[0]} | Time: {record[2].split(' ')[1]} |") #Print user ID if user doesnt exits

            print()
            logs_writer.write_log("Displayed top 5 records.", level="INFO", module=__file__)
            return True

    except sqlite3.Error as e:
        logs_writer.write_log(f"Error retrieving records: {e}", level="ERROR", module=__file__)
        print(f"Error retrieving records: {e}")
        return False

def clear_records():
    """Deletes all records from the database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Records") #Fixed table name to Records
            conn.commit()
            logs_writer.write_log("All records cleared from the database.", level="INFO", module=__file__)
            print("All records cleared!")
            return True
    except sqlite3.Error as e:
        logs_writer.write_log(f"Error clearing records: {e}", level="ERROR", module=__file__)
        print(f"Error clearing records: {e}")
        return False

if __name__ == "__main__":
    # Example Usage
    clear_records()
    insert_record("admin", 100)
    insert_record("admin", 200)
    insert_record("admin", 300)
    insert_record("admin", 400)
    show_records()