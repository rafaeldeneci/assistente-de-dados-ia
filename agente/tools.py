import sqlite3
import os

caminho_absoluto = os.path.abspath(__file__)
raiz_do_projeto = os.path.dirname(os.path.dirname(caminho_absoluto))
caminho_db = os.path.join(raiz_do_projeto, 'data', 'chamados.db')

colunas_permitidas =  {'nome_completo',
                       'plano',
                       'estado',
                       'cidade',
                       'consumo_Gb',
                       'mensalidade',
                       'status',
                       'inadimplencia'
                       }


def consultar_banco_dados(filtros: dict = {},
                          ordenar_por: str = None,
                          ordem: str = 'ASC', 
                          limite: int = None,
                          busca_parcial: bool = False) -> list:
    

    
    '''ferramenta definitiva para consulta de dados de clientes no banco de dados
    
    REGRAS!!!:
    1 - para buscar por nomes incompletos ou pedaços de palavras ative a "busca_parcial=True"
    
    2 - se o usuario pedir listas gerais(EX: clientes de sp ou inadinplentes) voce DEVE OBRIGATORIAMENTE 
    ajustar um "limite" para que não seja estourada a memoria do modelo, por 5 mil linhas de conteudo

    3 - caso o usuario realize uma busca por um cliente especifico, informando o nome completo exato, mantenha a "busca parcial=False"


    COLUNAS ACEITAS PARA FILTROS E ORDENAÇÃO:
    nome_completo,plano,estado,cidade,consumo_Gb,mensalidade,status,inadimplencia
    '''

    for coluna in filtros:
        if coluna not in colunas_permitidas:
            raise ValueError (f'coluna {coluna} não permitida, use apenas as colunas permitidas: {colunas_permitidas}')
        
    query = 'SELECT * FROM chamados WHERE 1=1'
    valor = []

    for coluna,valor in filtros.items():
        if busca_parcial:
            query+= f'AND {coluna} LIKE ?'
            valor.append(f'%{valor}%')
        else:
            query+= f'AND {coluna}=?'
            valor.append(str(valor))
    
    if ordenar_por and ordenar_por in colunas_permitidas:
        direcao = 'DESC' if ordem.upper() == 'DESC' else 'ASC'
        query += f'ORDER BY {ordenar_por} {direcao}'

    if limite:
        query += f'LIMIT {limite}'
    else:
        query += f'LIMIT 50'

    with sqlite3.connect(caminho_db) as conexão:
        cursor = conexão.cursor()
        cursor.execute(query,valor)
        return cursor.fetchall()   

