def consultar_saldo(saldo: float):
    print("\n----------- CONSULTA -----------\n")
    print(f"Saldo: {saldo}")
    print("\n--------------------------------")
    return saldo

def sacar(saldo: float):
    print("\n------------ SAQUE -------------\n")
    if saldo == 0:
        print(f"Não foi posível realizar o saque, seu saldo é de {saldo}")
        print("\n--------------------------------")
        return saldo
    valor = float(input("\nPor favor, informe o valor a ser sacado: "))
    if valor > saldo:
        print("Valor inválido, o valor do saque não pode ser maior que o saldo disponível.")
    else:
        saldo -= valor
        print("Saque realizado.")
    print("\n--------------------------------")
    return saldo

def depositar(saldo: float):
    print("\n----------- DEPÓSITO -----------\n")
    valor = float(input("Por favor, informe o valor a ser depositado: "))
    saldo += valor
    print("Deposito realizado com sucesso")
    print("\n--------------------------------")
    return saldo
def menu():
    saldo = 0.0
    while True:
        print("\n===== MENU =====\n")
        print("1. Consultar saldo")
        print("2. Sacar")
        print("3. Depositar")
        print("4. Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            consultar_saldo(saldo)
        elif opcao == "2":
            saldo = sacar(saldo)
        elif opcao == "3":
            saldo = depositar(saldo)
        elif opcao == "4":
            print("\nEncerrando operação.")
            break
        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    print("\nBem-vind@ à sua poupança!")
    menu()