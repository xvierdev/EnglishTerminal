-- Tabela de Usuários
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    points INTEGER
);

-- Tabela de Recordes
CREATE TABLE IF NOT EXISTS Records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date_time TEXT NOT NULL,
    record INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Tabela de Palavras
CREATE TABLE IF NOT EXISTS Words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english TEXT UNIQUE NOT NULL,
    portuguese TEXT NOT NULL,
    category TEXT -- Adicionado o campo 'category'
);