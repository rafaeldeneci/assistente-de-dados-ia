import sqlite3
from utils.csv_util import ler_clientes


def criar_tabela_chamados(clientes='data/clientes.csv', nome_tabela = 'data/chamados.db'):
    
    with sqlite3.connect(nome_tabela) as chamados:
        cursor = chamados.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chamados(
                       id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome_completo TEXT,
                       plano TEXT,
                       cidade TEXT,
                       consumo_gb INTEGER,
                       status TEXT
                       );
                       
                       
                       '''
                       )
        query_de_insercao = ''' INSERT INTO chamados(
          
          nome_completo,
          plano,
          cidade,
          consumo_gb,
          status)
          VALUES(
          :nome_completo,
          :plano,
          :cidade,
          :consumo_gb,
          :status)
          '''
        cursor.executemany(query_de_insercao, ler_clientes(clientes))
        chamados.commit()
    
if __name__=='__main__':
 criar_tabela_chamados('data/clientes.csv')