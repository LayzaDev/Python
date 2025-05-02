import sqlite3

def connect():
    return sqlite3.connect('users.db')

def create(name, age, profession, phone):
    
    if not name or not age or not profession or not phone:
        print("\nERRO: Nome, idade, profissão e telefone são obrigatórios.")
        return
    
    if not isinstance(age, int) or age <= 0:
        print("\nERRO: A idade deve ser um número inteiro positivo.")
        return
    
    try:
        with connect() as connection: 
            cursor = connection.cursor()
            sql_insert = 'INSERT INTO users (name, age, profession, phone) VALUES (?, ?, ?, ?)'
            cursor.execute(sql_insert, (name, age, profession, phone))
            connection.commit()
            print("\nUsuário inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"\nERRO: Não foi possível inserir o novo usuário: {e}")
        
def read():
    
    try:
        with connect() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            return users
    except sqlite3.Error as e:
        print(f"\nERRO: Não foi possível listar os usuários: {e}")
        return []
    
def update(id, name, age, profession, phone):
    
    if not name or not age or not profession or not phone:
        print("\nERRO: Nome, idade, profissão e telefone são obrigatórios.")
        return
    
    if not str(age).isdigit() or int(age) <= 0:
        print("\nERRO: A idade deve ser um número positivo.")
        return
    
    try:
        with connect() as connection:
            cursor = connection.cursor()
            sql_update = 'UPDATE users SET name=?, age=?, profession=?, phone=? WHERE id=?'
            cursor.execute(sql_update, (name, age, profession, phone, id))
            
            if cursor.rowcount == 0:
                print("\nERRO: Usuário não encontrado ou não existe.")
            else:
                connection.commit()
                print("\nUsuário atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"\nERRO: Problemas ao atualizar usuário: {e}")
        
def delete(id):
    
    try:
        with connect() as connection:
            cursor = connection.cursor()
            sql_delete = 'DELETE FROM users WHERE id=?'
            cursor.execute(sql_delete, (id,))
            if cursor.rowcount == 0:
                print("\nERRO: Usuário não encontrado ou não existe.")
            else:
                connection.commit()
                print("\nUsuário excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"\nERRO: Problemas ao excluir usuário: {e}")
