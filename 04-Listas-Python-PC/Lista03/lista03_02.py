def mescla_arquivos():
    try:
        with open("./arquivos_entrada/entrada_03_02.txt", 'r', encoding='UTF-8') as f_emp:
            empresas = f_emp.read().splitlines()

        with open("./arquivos_entrada/entrada_identificadores_03_02.txt", 'r', encoding='UTF-8') as f_id:
            chaves = f_id.read().splitlines()
        if len(empresas) != len(chaves):
            raise ValueError("O número de empresas e de chaves não é o mesmo.")
        
        with open("./arquivos_saida/saida_03_03.csv", 'w', encoding='UTF-8') as f_saida:
            for empresa, chave in zip(empresas, chaves):
                f_saida.write(f"{empresa}, {chave}\n")

        print(f"Arquivo criado/atualizado com sucesso.")
    except FileNotFoundError:
        print(f"\nArquivo não encontrado.")

if __name__ == "__main__":
    
    mescla_arquivos()
    

    
