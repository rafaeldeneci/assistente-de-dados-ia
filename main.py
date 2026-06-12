import os 
import sys

caminho_do_arquivo = os.path.abspath(__file__)
raiz_do_projeto = os.path.dirname(caminho_do_arquivo)

sys.path.append(raiz_do_projeto)


from utils.db_utils import criar_tabela_chamados
from scripts.gerar_dados import gerar_massa_dados

def rodar_sistema():
    print('[1/2] Gerando Clientes Automaticamente...')
    gerar_massa_dados(quantia_clientes=20000)

    print('[2/3] Rodando banco de dados...')
    print('[3/3] Rlimentando banco de dados com clientes gerados...')
    criar_tabela_chamados()

    print('***Banco de dados criado e Alimentado com sucesso!***')

if __name__=='__main__': 
    rodar_sistema()