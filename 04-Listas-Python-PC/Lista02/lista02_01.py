'''
1. Crie um script que irá calcular a área de um quadrado. Peça para a pessoa informar a medida numérica de um lado do quadrado. E depois informe-lhe o valor da área do quadrado.
'''

def calcula_area_quadrado(lado_do_quadrado):
    """
    Calcula a área de um quadrado com base no comprimento de seu lado.

    Args:
    lado_do_quadrado (int): Comprimento do lado.

    Return:
    int: A área do quadrado (lado * lado).
    """
    area = lado_do_quadrado * lado_do_quadrado
    return area

if __name__ == "__main__":
    """
    Solicita ao usuário o valor do lado do quadrado,
    e exibe a área do quadrado.
    """
    try:
        lado_do_quadrado = int(input("Informe o valor do lado do quadrado: "))
        area_do_quadrado = calcula_area_quadrado(lado_do_quadrado)
        print(f"Area do quadrado: {area_do_quadrado}")
    except ValueError:
        print(f"Entrada Inválida! Digite um número.")