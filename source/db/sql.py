# SQL queries to create database and tables.
create_table = '''
CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT UNIQUE NOT NULL,
        record INTEGER
);'''

create_words = '''
CREATE TABLE IF NOT EXISTS Words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english TEXT UNIQUE NOT NULL,
    portuguese TEXT NOT NULL,
    category TEXT NOT NULL
);'''

user_index = "CREATE INDEX IF NOT EXISTS idx_users_user ON Users (user);"
words_index = "CREATE INDEX IF NOT EXISTS idx_words_english ON Words (english);"