'''
1. Programe um script Python, que irá ler o arquivo entrada_03_01.txt, sendo que cada
linha do arquivo é um número inteiro. Este script irá imprimir as seguintes informações do
arquivo:
● A quantidade de linhas lidas do arquivo.
● A soma dos valores lidos.
● A média dos valores lidos (com duas casas decimais).
Por exemplo: suponha que o arquivo entrada_03_01.txt contenha as seguintes linhas:
7
1
9
O script irá imprimir:
Quantidade linhas: 3.
Soma: 17.
Média: 5.66.
'''

def manipula_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as arq:
            num_inteiros = [int(linha.strip()) for linha in arq if linha.strip()]

        quantidade_linhas = len(num_inteiros)
        soma = sum(num_inteiros)
        media = soma/quantidade_linhas if quantidade_linhas > 0 else 0

        print(f"\nQuantidade de linhas lidas do arquivo: {quantidade_linhas}")
        print(f"\nSoma: {soma}")
        print(f"\nMédia: {media}")
    except FileNotFoundError:
        print("\nArquivo não encontrado.\n")
    except ValueError:
        print("\nOs dados do arquivo são inválidos (não inteiros).")

if __name__ == "__main__":
    print("\n=========== MANIPULADOR DE ARQUIVOS ===========")
    arquivo = "./arquivos_entrada/entrada_03_01.txt"
    manipula_arquivo(arquivo)