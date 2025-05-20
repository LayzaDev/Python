import csv
import configparser

def gerar_arquivo_vendas_csv(data_venda, numero_pedido, nome_empresa, valor_total_pedidos, situacao):
   
    with open("./arquivos_entrada/vendas_03_04.csv", "a") as f_vendas:
        escritor = csv.writer(f_vendas, delimiter=",") 
        escritor.writerow([data_venda, numero_pedido, nome_empresa, valor_total_pedidos, situacao])
            #escritor.writerow(["2021-01-12 13:20:02", 1001, "empresa02", 22.40, "FINALIZADA"])
            #escritor.writerow(["2021-01-11 13:20:02", 1007, "empresa02", 125.30, "CANCELADA"])
            #escritor.writerow(["2021-01-14 13:20:02", 1401, "empresa01", 125.30, "FINALIZADA"])
            #escritor.writerow(["2021-01-12 17:45:00", 1075, "empresa01", 125.30, "CANCELADA"])
            #escritor.writerow(["2021-01-14 13:20:02", 2001, "empresa01", 125.30, "FINALIZADA"])
            #escritor.writerow(["2021-01-14 10:27:02", 2004, "empresa02", 125.30, "FINALIZADA"])
            #escritor.writerow(["2021-01-14 13:20:02", 2101, "empresa01", 12.40, "FINALIZADA"])
            #escritor.writerow(["2021-01-14 11:55:22", 5001, "empresa02", 145.70, "FINALIZADA"])
            #escritor.writerow(["2021-01-14 00:00:33", 8001, "empresa03", 189.40, "FINALIZADA"])

def escrever_no_arquivo_conf(data, empresa):
    config = configparser.ConfigParser()
    config.optionxform = str 
    if data and empresa == "":
        config['GERAL'] = {"DATA": data}
    elif empresa and data == "":
        config['GERAL'] = {"EMPRESA": empresa}
    elif data and empresa:
        config['GERAL'] = {"DATA": data, "EMPRESA": empresa}
    else:
        print("Valor inválido.")
        
    with open('./arquivos_entrada/configuracao_03_03.conf', 'w') as f_config:
        config.write(f_config)
        print(f"\nEscrita no arquivo .conf realizada com sucesso!")

"""      
def ler_arquivo_vendas():
    try: 
        with open("./arquivos_entrada/vendas_03_04.csv", "r") as f_vendas:
            leitor = csv.reader(f_vendas)
            return leitor
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")
""" 

def arquivo_conf_vazio():
    
    valores_vendas_finalizadas = []
    valores_vendas_canceladas = []
    try: 
        with open("./arquivos_entrada/vendas_03_04.csv", "r") as f_vendas:
            leitor = csv.reader(f_vendas)
            for _, linha in enumerate(leitor):
                if linha[4] == 'FINALIZADA':
                    valores_vendas_finalizadas.append(float(linha[3]))
                else:
                    valores_vendas_canceladas.append(float(linha[3]))
        print("\nTotal de vendas do período:")
        print(f"Canceladas: {'{:.2f}'.format(sum(valores_vendas_canceladas))}\nFinalizadas: {'{:.2f}'.format(sum(valores_vendas_finalizadas))}")
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")

def arquivo_conf_contendo_uma_empresa(empresa: str):
    
    try:  
        with open("./arquivos_entrada/vendas_03_04.csv", "r") as f_vendas:
            valores_vendas_finalizadas = []
            valores_vendas_canceladas = []
            leitor = csv.reader(f_vendas)
            for _, linha in enumerate(leitor):
                if linha[2] == empresa:
                    if linha[4] == "FINALIZADA":
                        valores_vendas_finalizadas.append(float(linha[3]))
                    else: 
                        valores_vendas_canceladas.append(float(linha[3]))
        print(f"\nTotal de vendas de '{empresa}':")
        print(f"Canceladas: {'{:.2f}'.format(sum(valores_vendas_canceladas))}\nFinalizadas: {'{:.2f}'.format(sum(valores_vendas_finalizadas))}")
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")
    
def arquivo_conf_contendo_uma_data(data: str):
    try:  
        with open("./arquivos_entrada/vendas_03_04.csv", "r") as f_vendas:
            valores_vendas_finalizadas = []
            valores_vendas_canceladas = []
            leitor = csv.reader(f_vendas)
            for _, linha in enumerate(leitor):
                if linha[0][:10] == data:
                    if linha[4] == "FINALIZADA":
                        valores_vendas_finalizadas.append(float(linha[3]))
                    else: 
                        valores_vendas_canceladas.append(float(linha[3]))
        print(f"\nTotal de vendas na data '{data}':")
        print(f"Canceladas: {'{:.2f}'.format(sum(valores_vendas_canceladas))}\nFinalizadas: {'{:.2f}'.format(sum(valores_vendas_finalizadas))}")        
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")
            
def arquivo_conf_contendo_data_e_empresa(data, empresa):
    try:  
        with open("./arquivos_entrada/vendas_03_04.csv", "r") as f_vendas:
            valores_vendas_finalizadas = []
            valores_vendas_canceladas = []
            leitor = csv.reader(f_vendas)
            for _, linha in enumerate(leitor):
                if linha[0][:10] == data and linha[2] == empresa:
                    if linha[4] == "FINALIZADA":
                        valores_vendas_finalizadas.append(float(linha[3]))
                    else: 
                        valores_vendas_canceladas.append(float(linha[3]))
        print(f"\nTotal de vendas de '{empresa}' na data '{data}':")
        print(f"Canceladas: {'{:.2f}'.format(sum(valores_vendas_canceladas))}\nFinalizadas: {'{:.2f}'.format(sum(valores_vendas_finalizadas))}")        
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")
    
def empresas_e_datas_inexistentes():
    try:  
        with open("./arquivos_entrada/vendas_03_04.csv", "r") as f_vendas:
            leitor = csv.reader(f_vendas)
            ...    
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")
    
def consultar_pedidos():

    config = configparser.ConfigParser()
    config.optionxform = str 
    config.read("./arquivos_entrada/configuracao_03_03.conf")
    
    if config.sections() == []:
        
        return arquivo_conf_vazio()
    
    elif 'EMPRESA' in config['GERAL'] and 'DATA' not in config['GERAL']:
        
        return arquivo_conf_contendo_uma_empresa(config['GERAL']['EMPRESA'])  
     
    elif 'DATA' in config['GERAL'] and 'EMPRESA' not in config['GERAL']:
        
        return arquivo_conf_contendo_uma_data(config["GERAL"]['DATA'])
    
    elif 'DATA' in config['GERAL'] and 'EMPRESA' in config['GERAL']:
        
        return arquivo_conf_contendo_data_e_empresa(config["GERAL"]['DATA'], config['GERAL']['EMPRESA'])  
           
    else:
        return empresas_e_datas_inexistentes()

if __name__ == "__main__":
    
    while True:
        
        print("\nMENU DE OPÇÕES\n")
        print("1. Cadastrar pedidos no arquivo .csv")
        print("2. Atualizar arquivo .conf")
        print("3. Consultar pedidos")
        print("4. Sair")
        
        option = input("\nEscolha uma opção: ")
        
        if option == '1':
            
            print("\nCADASTRO\n")
            
            total_linhas = int(input("Quantidade de pedidos a cadastrar: "))
            
            for i in range(total_linhas):
                
                if i < total_linhas:
                    print(f"\nPedido {i}: \n")
                    
                data_venda = input("Data da venda (AAAA-MM-DD HH:MM:SS): ")
                numero_pedido = input("Número do pedido (ex: 1001): ")
                nome_empresa = input("Identificador do varejista (ex: Empresa02): ")
                valor_total_pedidos = input("Valor total dos produtos (ex: 125.30): ")
                situacao = input("Situação da venda (CANCELADA ou FINALIZADA): ")
                
                gerar_arquivo_vendas_csv(data_venda, numero_pedido, nome_empresa, valor_total_pedidos, situacao)
                
                print("\nPedido cadastrado!")
        elif option == '2':
            
            print("\nATUALIZAR CONFIGURAÇÕES\n")
            print("O que você deseja adicionar? ")
            print("1. Empresa")
            print("2. Data")
            print("3. Data e Empresa")
            print("4. Cancelar")
            
            opcao2 = input("\nEscolha uma opção: ")
            
            while True:
                if opcao2 == '1':
                    data = ""
                    empresa = input("\nNome da empresa: ")
                    escrever_no_arquivo_conf(data, empresa)
                    break
                elif opcao2 == '2':
                    empresa = ""
                    data = input("\nData da venda: ")
                    escrever_no_arquivo_conf(data, empresa)
                    break
                elif opcao2 == '3':
                    empresa = input("\nNome da empresa: ")
                    data = input("\nData da venda: ")
                    escrever_no_arquivo_conf(data, empresa)
                    break
                elif opcao2 == '4':
                    print("Operação cancelada!")
                    break
                else:
                    print("Opção inválida.")
                    break
        elif option == '3':
            print("\nCONSULTAS")
            consultar_pedidos()
        elif option == '4':
            print("\nAté a próxima!")
            break
        else:
            print("\nOpção inválida.")
            break
    #total_vendas_finalizadas, total_vendas_canceladas = determina_valores_do_pedido()
    
    #escrever_no_arquivo_conf()

    
    