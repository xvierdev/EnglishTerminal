def connect():
    import sqlite3
    from sqlite3 import Error

    # Create a database connection
    conn = None
    try:
        conn = sqlite3.connect('database.db')
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn

if __name__ == "__main__":
    conn = connect()
    if conn:
        conn.close()
        print("Connection closed")