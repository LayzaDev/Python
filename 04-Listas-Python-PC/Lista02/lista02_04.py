'''
4. Estou tentando entender os juros do meu banco. Para isto, ele me informou esta fórmula: valorFinal = valorEmprestimo + (valorEmprestimo * taxa * tempo) onde que:
●​ valorEmprestimo: É o valor que pegarei emprestado.
●​ taxa: É o valor da taxa por mês. Por exemplo: se for 4% ao mês, o valor será 0.04.
●​ tempo: Quantidade de meses que irei pagar o empréstimo.
Crie um script que colete cada um destes valores para calcular o valor final que estarei pagando ao banco.
'''

def calcula_valor_final_a_pagar(valor_emprestimo: float, taxa: float, tempo: float) -> float:
    """
    Calcula o valor final a ser pago de um empréstimo.

    Args:
    valor_emprestimo (float): Valor inicial do empréstimo.
    taxa (float): Taxa de juros ao mês (em porcentagem).
    tempo (float): Tempo de pagamento em meses.

    Return:
    float: Valor final a ser pago ao banco
    """
    valor_final = valor_emprestimo + (valor_emprestimo * (taxa/100) * tempo)
    return valor_final

if __name__ == "__main__":
    """
    Solicita ao usuário o valor do empréstimo, a taxa de juros mensal e o tempo de pagamento (em meses),
    e exibe o valor final a ser pago ao banco.
    """
    try:
        valor_emprestimo = float(input("Informe o valor do emprestimo: "))
        taxa = float(input("Informe o valor da taxa: "))
        tempo = float(input("Informe a quantidade de meses que irá pagar o emprestimo: "))
        valor_final = calcula_valor_final_a_pagar(valor_emprestimo, taxa, tempo)
        print(f"\nValor final a pagar: {valor_final}\n")
    except ValueError:
        print("\nValor Inválido! Digite um número.")
    