import csv
import os

caminhp_absoluto = os.path.abspath(__file__)
raiz_projeto = os.path.dirname(os.path.dirname(caminhp_absoluto))
caminho_ate_csv = os.path.join(raiz_projeto,'data','clientes.csv')

def ler_clientes():

    clientes = []
    with open(caminho_ate_csv) as informações:
        leitor_de_arquivos = csv.DictReader(informações)
        for linha in leitor_de_arquivos:
            clientes.append({ 'nome_completo':linha['nome_completo'],
                              'plano':linha['plano'],
                              'cidade':linha['cidade'],
                              'consumo_gb':linha['consumo_gb'],
                              'status':linha['status']
                              })
    return clientes
