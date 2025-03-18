import sqlite3

def initialize_db():
    with sqlite3.connect('users.db') as connection:

        cursor = connection.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL,
                age INTEGER NOT NULL,
                profession VARCHAR(50) NOT NULL,
                phone VARCHAR(15) NOT NULL
            )
        ''')

        connection.commit()
        print("Banco de dados inicializado com sucesso!")