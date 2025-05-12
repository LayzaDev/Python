'''
7. Crie um script que leia 10 números inteiros positivos e que irá apresentar:
●​ A lista dos valores lidos de forma ordenada.
●​ A contagem de cada item. Por exemplo, se o usuário informou [1,1,1,1,2, 3], aqui apresentamos:
○​ 1: 4x.
○​ 2: 1x.
○​ 3: 1x.
●​ Uma saída identificando o número, se o número é par e se é primo. Isto será feito separando por vírgulas: Por exemplo, se informou [1,2,3,6]. Iremos apresentar aqui:
○​ 1,ímpar,não é primo
○​ 2,par,é primo
○​ 3,ímpar,é primo
○​ 6,par,não é primo
'''

def ordenar_lista(lista: list) -> list:
    """
    Retorna a lista ordenada em ordem crescente.

    Args:
    lista (list): Lista de números inteiros.

    Return:
    list: Lista ordenada.
    """
    lista_ordenada = sorted(lista)
    return lista_ordenada
        
def contagem_de_cada_item(lista: list):
    """
    Conta a frequência de cada número na lista e formata os resultados.

    Args:
    lista (list): Lista de números inteiros.

    Return:
    str: Contagem de ocorrências de cada item da lista fornatados linha a linha.
    """
    contagem = {}
    lista_2 = []
    for item in lista:
        if item in contagem:
            contagem[item] += 1
        else:
            contagem[item] = 1
    for item in sorted(contagem):
        lista_2.append(f"{item}: {contagem[item]}x")
    return "\n".join(lista_2)

def eh_primo(numero: int) -> bool:
    """
    Verifica se o número informado é primo.

    Args:
    numero (int): Número inteiro a ser verificado.

    Return:
    bool: True se o número for primo, False caso contrário.
    """
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    
def classifica_numeros(lista: list) -> list:
    """
    Classifica cada número da lista como par/ímpar e primo/não primo.

    Args:
    lista (list): Lista de números inteiros.

    Return:
    str: Classificação de cada número, linha por linha.
    """
    lista_aux = []
    for numero in lista:
        paridade = "par" if numero % 2 == 0 else "ímpar"
        primo = "é primo" if eh_primo(numero) else "não é primo"
        lista_aux.append(f"{numero}, {paridade}, {primo}")
    return "\n".join(lista_aux)


if __name__ == "__main__":

    lista = []

    print("\n======= Manipulador de listas =======\n")
    print("Informe 10 numeros inteiros: \n")

    for i in range(10):
        while True:
            try:
                numero = int(input(f"Número {i}: "))
                if numero >= 0:
                    lista.append(numero)
                    break
                else:
                    print("\nValor inválido! O número deve ser um inteiro positivo (>= 0).\n")
            except ValueError:
                print("\nEntrada inválida! Digite um número inteiro.\n")
    
    print(f"\nLista Original: {lista}")
    lista_ordenada = ordenar_lista(lista)
    print(f"\nLista Ordenada: {lista_ordenada}")
    contagem = contagem_de_cada_item(lista)
    print(f"\nContagem:\n{contagem}")
    classificacao = classifica_numeros(lista)
    print(f"\nClassificação:\n{classificacao}")

