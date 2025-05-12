def buscar_telefones(prefixo: str, primeiro_sufixo: str, ultimo_sufixo: str):
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
