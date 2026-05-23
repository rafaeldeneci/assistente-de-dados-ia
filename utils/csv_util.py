import csv



def ler_clientes(caminho_arquivo):

    clientes = []
    with open(caminho_arquivo) as informações:
        leitor_de_arquivos = csv.DictReader(informações)
        for linha in leitor_de_arquivos:
            clientes.append({ 'nome_completo':linha['nome_completo'],
                              'plano':linha['plano'],
                              'cidade':linha['cidade'],
                              'consumo_gb':linha['consumo_gb'],
                              'status':linha['status']
                              })
    return clientes
if __name__=='__main__' :      
 ler_clientes('data/clientes.csv')