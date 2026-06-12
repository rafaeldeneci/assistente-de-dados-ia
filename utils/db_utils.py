import sqlite3
from utils.csv_util import ler_clientes
import os 


caminho_absoluto = os.path.abspath(__file__)
raiz_projeto = os.path.dirname(os.path.dirname(caminho_absoluto))
caminho_csv = os.path.join(raiz_projeto, 'data', 'clientes.csv')
caminho_ao_db = os.path.join(raiz_projeto, 'data', 'chamados.db')

def criar_tabela_chamados():
    
    with sqlite3.connect(caminho_ao_db) as chamados:
        cursor = chamados.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chamados(
                       id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome_completo TEXT,
                       plano TEXT,
                       estado TEXT,
                       cidade TEXT,
                       consumo_Gb INTEGER,
                       mensalidade INTEGER,
                       status TEXT,
                       inadinplencia TEXT
                       );
                       
                       
                       ''')
        query_de_insercao = ''' INSERT INTO chamados(
          nome_completo,
          plano,
          estado,
          cidade,
          consumo_Gb,
          mensalidade,
          status,
          inadinplencia)
          VALUES(
          :nome_completo,
          :plano,
          :estado,
          :cidade,
          :consumo_Gb,
          :mensalidade,
          :status,
          :inadinplencia)
          '''
        cursor.executemany(query_de_insercao, ler_clientes())
        chamados.commit()
    


