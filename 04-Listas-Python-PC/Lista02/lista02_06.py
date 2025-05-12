'''
6. Faça um programa que leia a nota de um aluno. Garanta que a nota seja um valor inteiro entre zero e 100. Se o valor não estiver dentro desse intervalo, informe que a nota é inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso contrário, informa que ele foi reprovado.
'''

def verifica_nota(nota: float) -> str:
    """
    Verifica se a nota do aluno é suficiente para ser aprovado.

    Parâmetros:
        nota (float): A nota do aluno, que deve estar no intervalo de 0 a 100.

    Retorna:
        str: "Aprovado" se a nota for maior que 60, caso contrário "Reprovado".
    """
    if nota > 60:
        return "Aprovado"
    return "Reprovado"

if __name__ == "__main__":
    print("\n======= Verificador de Notas =======\n")

    nota = float(input("Informe a nota do aluno: "))

    while not (nota >= 0 and nota <= 100):
        print("\n***** Nota inválida! *****")
        nota = float(input("\nInforme a nota do aluno novamente (valores entre 0 e 100): "))

    resultado = verifica_nota(nota)
    print(f"\nResultado: {resultado}")