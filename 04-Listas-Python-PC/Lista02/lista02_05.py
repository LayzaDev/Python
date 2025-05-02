import math

"""
    Calcula as raízes de uma equação de segundo grau com a fórmula de Bhaskara.
"""
def calcular_discriminante(a: float, b: float, c: float) -> float:
    """
        Calcula o discriminante (delta) de uma equação do 2º grau.

        Args:
            a (float): Coeficiente quadrático.
            b (float): Coeficiente linear.
            c (float): Termo constante.

        Returns:
            float: O valor de delta.
    """
    if a == 0:
        raise ValueError("\nO coeficiente 'a' deve ser diferente de 0.\n")
    
    delta = b ** 2 - 4 * a * c
    return delta

def calcular_raizes(a: float, b: float, c: float):
    """
        Calcula as raízes reais de uma equação do 2º grau, se existirem.

        Args:
            a (float): Coeficiente quadrático.
            b (float): Coeficiente linear.
            c (float): Termo constante.

        Returns:
            tuple: Uma tupla contendo as duas raízes reais.
    """
    delta = calcular_discriminante(a, b, c)

    if delta < 0:
        raise ValueError("\nNão há raízes reais (as raízes são complexas).\n")
    elif delta == 0:
        x = -b / (2 * a)
        return (x, x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)

if __name__ == "__main__":
    """
    Permite que o usuário insira os coeficientes, e exibe as raízes reais ou informa se elas não existem.        
    """
    print("\n======== BHASKARA ========\n")

    a = float(input("Informe o valor de A: "))
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))

    try:
        raizes = calcular_raizes(a, b, c)
        print(f"\nRaízes: {raizes}")
    except ValueError as e:
        print(f"\nErro: {e}")


    
    