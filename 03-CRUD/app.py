from operations import create, read, update, delete 
from db_connection import initialize_db

def showMenu():
    print("\n--- MENU DE OPERAÇÕES ---\n")
    print("1. Criar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Excluir usuário")
    print("5. Sair")
    
def main():
    initialize_db()
    
    while True:
        showMenu()
        
        option = input("\nEscolha uma opção: ")
        
        if option == "1":
            print('\n--- Cadastro de Usuário ---')
            name = input("Nome: ")
            age = input("Idade: ")
            profession = input("Profissão: ")
            phone = input("Telefone/Celular: ")
            
            create(name, age, profession, phone)
            
        elif option == "2":
            
            users = read()
            if users: 
                print("\n--- Lista de Usuários ---")
                for user in users:
                    print(f"\nID: {user[0]}, Nome: {user[1]}, Idade: {user[2]}, Profissão: {user[3]}, Telefone: {user[4]}")
                    print("---------------------------------------------------------------------------------------------------------------------------")
            else:
                print("\n--- Nenhum usuário cadastrado.")
        elif option == "3":
            id = input("\nInforme o ID do usuário que deseja atualizar: ")
            newName = input("Novo nome: ")
            newAge = input("Nova idade: ")
            newProfession = input("Nova profissão: ")
            newPhone = input("Novo número de telefone: ")
            update(id, newName, newAge, newProfession, newPhone)
        elif option == "4":
            id = input("\nInforme o ID do usuário que deseja excluir: ")
            delete(id)
        elif option == "5":
            print("\nEncerrando processo...")
            print("Encerrado.")
            break;
        else:
            print("\nOpção inválida!\n")
            showMenu()

if __name__ == "__main__":
    main()
