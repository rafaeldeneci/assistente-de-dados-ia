import csv
import os

caminho_absoluto = os.path.abspath(__file__)
raiz_projeto = os.path.dirname(os.path.dirname(caminho_absoluto))
caminho_ate_csv = os.path.join(raiz_projeto,'data','clientes.csv')

def ler_clientes():

    clientes = []
    
    with open(caminho_ate_csv) as informações:
        leitor_de_arquivos = csv.DictReader(informações)
        for linha in leitor_de_arquivos:
            clientes.append({ 'nome_completo':linha['nome_completo'],
                              'plano':linha['plano'],
                              'estado':linha['estado'],
                              'cidade':linha['cidade'],
                              'consumo_Gb':linha['consumo_Gb'],
                              'mensalidade':linha['mensalidade'],
                              'status':linha['status'],
                              'inadimplencia':linha['inadimplencia'],
                            })
    return clientes

