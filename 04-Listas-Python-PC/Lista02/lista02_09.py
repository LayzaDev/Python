'''
9. Crie um script que liste todos os números dos telefones, ao serem informados, o prefixo e os sufixos. Por exemplo, suponha que o prefixo seja “3232” e que o primeiro prefixo seja “0001” e o último sufixo seja “0005”; logo o programa irá imprimir:
Seus números de telefone são:
● 3232-0001
●​ 3232-0002
● 3232-0003
●​ 3232-0004
● 3232-0005
'''

def buscar_telefones(prefixo: str, primeiro_sufixo: str, ultimo_sufixo: str) -> None:
    """
    Gera e exibe uma lista de números de telefone com base em um prefixo e um intervalo de sufixos.

    Args:
    prefixo (str): Parte inicial do número de telefone (ex: "3232").
    primeiro_sufixo (str): Primeiro sufixo do intervalo (ex: "0001").
    ultimo_sufixo (str): Último sufixo do intervalo (ex: "0005").

    Return:
    None
    """
    inicio = int(primeiro_sufixo)
    fim = int(ultimo_sufixo)

    print("\nSeus números de telefone são: \n")
    for i in range(inicio, fim + 1):
        sufixo = f"{i:04d}"
        print(f"{prefixo}-{sufixo}")
        
if __name__ == "__main__":
    
    prefixo = input("Digite o prefixo do telefone (ex: 3232): ")
    primeiro_sufixo = input("Digite o primeiro sufixo do telefone (ex: 0001): ")
    ultimo_sufixo = input("Digite o último sufixo do telefone (ex: 0005): ")
    
    buscar_telefones(prefixo, primeiro_sufixo, ultimo_sufixo)
