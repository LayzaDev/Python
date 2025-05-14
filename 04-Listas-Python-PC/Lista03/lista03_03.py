def cria_arquivo_saida():
    with open("./arquivos_entrada/entrada_empresa_03.csv", "r", encoding='UTF-8') as f_emp:
        dados_empresa = f_emp.read().splitlines()
    
    with open("./arquivos_saida/saida_03_03.log", "w", encoding='UTF-8') as f_saida:
        for linha in dados_empresa:
            documento, nome, chave = linha.split(',')
            dicionario = {
                "documento": documento,
                "nome": nome,
                "chave": chave
            }
            f_saida.write(f"{dicionario}\n")

    print("Arquivo saida_03_03.log criado.")
if __name__ == "__main__":
    cria_arquivo_saida()