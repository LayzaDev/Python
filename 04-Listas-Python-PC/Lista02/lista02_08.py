'''
8. Faça um programa para controle de sua poupança. Sua poupança deverá iniciar com saldo zerado (o script armazena o seu saldo na memória). O programa irá apresentar o seguinte menu principal de quatro opções:
a. Consultar saldo.
- Se escolhermos esta opção, iremos mostrar o saldo da poupança. E voltaremos a mostrar o menu principal.
b. Sacar.
- Se o saldo estiver zerado, iremos informar que não é possível sacar e voltaremos para o menu principal.
- Se o saldo não estiver zerado, iremos solicitar o valor a ser sacado.
- Se o valor sacado deixar a conta negativa, iremos informar que o valor é inválido e voltaremos para o menu principal.
- Se o valor sacado não deixar a conta negativa; então, iremos retirar o valor do saldo.
- Sempre voltamos a apresentar o menu principal.
c. Depositar.
- Iremos informar o valor a ser depositado e adicioná-lo ao saldo.Voltamos a apresentar o menu principal.
d. Sair.
- Saímos do programa.
'''

def consultar_saldo(saldo: float):
    """
    Exibe o saldo atual da conta.

    Args:
    saldo (float): Saldo atual da conta.

    Return:
    float: O mesmo saldo informado.
    """
    print("\n----------- CONSULTA -----------\n")
    print(f"Saldo: {saldo}")
    print("\n--------------------------------")
    return saldo

def sacar(saldo: float):
    """
    Realiza um saque do saldo disponível, se possível.

    Args:
    saldo (float): Saldo atual da conta.

    Return:
    float: Saldo atualizado após o saque (ou inalterado, se o saque não for possível).
    """
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
    """
    Realiza um depósito na conta.

    Args:
    saldo (float): Saldo atual da conta.

    Return:
    float: Saldo atualizado após o depósito.
    """
    print("\n----------- DEPÓSITO -----------\n")
    valor = float(input("Por favor, informe o valor a ser depositado: "))
    saldo += valor
    print("Deposito realizado com sucesso")
    print("\n--------------------------------")
    return saldo

def menu():
    """
    Exibe um menu interativo para o usuário realizar operações
    de consulta de saldo, saque, depósito ou sair do sistema.

    Essa função controla o fluxo principal do programa.
    """
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