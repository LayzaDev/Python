def busca_pessoa_mais_velha(lista_pessoas: list) -> str:    
    """
    Retorna o nome da pessoa mais velha da lista de pessoas.

    Params:
    lista_pessoas (list): Lista de tuplas, onde cada tupla contém (nome: str, idade: int).

    Return:
    str: Nome da pessoa mais velha.
    """
    mais_velha = max(lista_pessoas, key=lambda pessoa: pessoa[1])    
    return mais_velha[0]

def busca_pessoa_mais_nova(lista_pessoas: list) -> str:    
    """
    Retorna o nome da pessoa mais nova da lista de pessoas.

    Params:
    lista_pessoas (list): Lista de tuplas, onde cada tupla contém (nome: str, idade: int).

    Return:
    str: Nome da pessoa mais nova.
    """
    mais_nova = min(lista_pessoas, key=lambda pessoa: pessoa[1])    
    return mais_nova[0]

def calcula_media_das_idades(lista_pessoas: list) -> float:    
    """
    Calcula a média das idades da lista de pessoas.

    Params:
    lista_pessoas (list): Lista de tuplas (nome: str, idade: int).

    Return:
    float: Média das idades. Se a lista estiver vazia retorna 0.0
    """
    idades = [idade for _, idade in lista_pessoas]
    media_idades = sum(idades) / len(idades) if idades else 0.0
    return media_idades

if __name__ == "__main__":
    """
    Solicita ao usuário os dados de 3 pessoas,
    armazena as informações em uma lista e
    exibe o nome da pessoa mais velha, da mais nova e a média das idades.
    """
    lista_pessoas = []
    
    for _ in range(3):
        nome = input("Informe um nome: ")
        idade = int(input("Informe uma idade: "))
        lista_pessoas.append((nome, idade))
        
    mais_velha = busca_pessoa_mais_velha(lista_pessoas)
    mais_nova = busca_pessoa_mais_nova(lista_pessoas)
    media = calcula_media_das_idades(lista_pessoas)
    
    print(f"\nPessoa mais velha: {mais_velha}")
    print(f"\nPessoa mais nova: {mais_nova}")
    print(f"\nMédia das idades: {media}")
    
    
    

    
    
        