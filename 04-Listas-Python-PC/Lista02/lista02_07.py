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

def contagem_teste(lista: list) -> list:
    lista2 = []
    for i in lista:
        numero = lista.count(i)
        result = f"{i}: {numero}x."   
        lista2.append(result)
    return lista2

def classifica_numeros(lista: list) -> list:
    ...

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
