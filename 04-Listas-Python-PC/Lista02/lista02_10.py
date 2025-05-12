'''
Faça um programa em que temos uma função em que recebe duas listas, a primeira lista refere-se ao nome de n pessoas, e a segunda lista são as n idades das pessoas. Esta função irá devolver uma lista de dicionários contendo o nome e a idade das junção das duas listas.
'''

def juntar_nomes_e_idades(nomes: list, idades: list) -> list:
    """
    Combina duas listas (nomes e idades) em uma lista de dicionários.

    Args:
    nomes (list): Lista de nomes (str).
    idades (list): Lista de idades (int), com a mesma ordem e tamanho da lista de nomes.

    Return:
    list: Lista de dicionários no formato {"nome": nome, "idade": idade}.
    """
    nova_lista = [{"nome": nome, "idade": idade} for nome, idade in zip(nomes, idades)]
    return nova_lista

if __name__ == "__main__":
    nomes = ["Ana","Carla","Bruno","Daniel","Yasmin","Felipe","Giovana","Henrique","Isabela","João"]
    idades = [25, 32, 28, 40, 22, 35, 27, 30, 26, 29]
    
    lista = juntar_nomes_e_idades(nomes, idades)
    print("\nLista de dicionarios contendo nomes e idades:\n\n",lista)