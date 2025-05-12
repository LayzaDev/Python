'''
2. Crie um script que leia um número inteiro. Se o número for positivo, irá determinar se o número é par ou ímpar; caso contrário, informará que o número é inválido.
'''

def analisa_numero(numero):
    """
    Analisa se um número inteiro é par ou ímpar, desde que não seja negativo.

    Args:
    numero (int): Número inteiro passado pelo usuário.

    Return:
    str: Mensagem indicando se o número é par, ímpar ou inválido.
    """
    if numero < 0:
        return "O número não é válido!"
    
    if(numero % 2 == 0):
        return f"O número {numero} é par"
    
    return f"O número {numero} é ímpar"
    
if __name__ == "__main__":
    """
    Solicita ao usuário um número inteiro,
    e exibe o resultado (Se o número informado é par, impar ou inválido).
    """
    try:
        numero = int(input("Informe um número inteiro: "))
        resultado = analisa_numero(numero)
        print(resultado)
    except ValueError:
        print("Entrada inválida! Informe um número inteiro.")
        