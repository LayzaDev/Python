"""
Manipulador de Listas Numéricas

O script permite ao usuário inserir 10 números inteiros positivos, e realiza as seguintes operações:

1. Ordena a lista dos valores lidos.
2. Conta quantas vezes cada número aparece.
3. identifica o número, e indica se é par e se é primo

Funções:
- ordenar_lista(lista): Retorna a lista de entrada ordenada em ordem crescente.
- contagem_de_cada_item(lista): Retorna uma string formatada com a contagem de ocorrências de cada item da lista.
- eh_primo(numero): Verifica se um número inteiro é primo.
- classifica_numeros(lista): Retorna uma string classificando cada número como par/ímpar e primo/não primo.

Ao executar o script, o usuário é solicitado a inserir 10 números inteiros positivos. Em seguida, são exibidos:
- A lista original;
- A lista ordenada;
- A contagem de cada item da lista;
- A classificação de cada número quanto à paridade e primalidade.
"""

from collections import Counter

def ordenar_lista(lista: list) -> list:
    lista_ordenada = sorted(lista)
    return lista_ordenada
        
def contagem_de_cada_item(lista: list):
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
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    
def classifica_numeros(lista: list) -> list:
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

