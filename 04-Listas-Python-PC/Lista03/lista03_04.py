import csv
import configparser

def gerar_arquivo_csv():
   
    with open("./arquivos_entrada/vendas_03_04.csv", "w") as f_vendas:
        escritor = csv.writer(f_vendas, delimiter=",") 
        escritor.writerow(["2021-01-12 13:20:02", 1001, "empresa01", 125.30, "FINALIZADA"])
        escritor.writerow(["2021-01-12 13:20:02", 1001, "empresa02", 22.40, "FINALIZADA"])
        escritor.writerow(["2021-01-11 13:20:02", 1007, "empresa02", 125.30, "CANCELADA"])
        escritor.writerow(["2021-01-14 13:20:02", 1401, "empresa01", 125.30, "FINALIZADA"])
        escritor.writerow(["2021-01-12 17:45:00", 1075, "empresa01", 125.30, "CANCELADA"])
        escritor.writerow(["2021-01-14 13:20:02", 2001, "empresa01", 125.30, "FINALIZADA"])
        escritor.writerow(["2021-01-14 10:27:02", 2004, "empresa02", 125.30, "FINALIZADA"])
        escritor.writerow(["2021-01-14 13:20:02", 2101, "empresa01", 12.40, "FINALIZADA"])
        escritor.writerow(["2021-01-14 11:55:22", 5001, "empresa02", 145.70, "FINALIZADA"])
        escritor.writerow(["2021-01-14 00:00:33", 8001, "empresa03", 189.40, "FINALIZADA"])


def arquivo_conf_vazio():
    
    valores_vendas_finalizadas = []
    valores_vendas_canceladas = []
    
    with open("./arquivos_entrada/vendas_03_04.csv", newline="") as f_vendas:
        leitor = csv.reader(f_vendas)
        for _, linha in enumerate(leitor):
            if linha[4] == 'FINALIZADA':
                valores_vendas_finalizadas.append(float(linha[3]))
            else:
                valores_vendas_canceladas.append(float(linha[3]))
                
    return sum(valores_vendas_finalizadas), sum(valores_vendas_canceladas)
    
    
def determina_valores_do_pedido():
    
    config = configparser.ConfigParser()
    config.read("./arquivos_entrada/configuracao_03_03.conf")
    
    if config.sections() == []:
        return arquivo_conf_vazio()
    else:
        ...                      


if __name__ == "__main__":
    
    gerar_arquivo_csv()
    
    total_vendas_finalizadas, total_vendas_canceladas = determina_valores_do_pedido()
    
    print("Total de vendas do período:")
    print(f"Canceladas: {'{:.2f}'.format(total_vendas_canceladas)}\nFinalizadas: {'{:.2f}'.format(total_vendas_finalizadas)}")