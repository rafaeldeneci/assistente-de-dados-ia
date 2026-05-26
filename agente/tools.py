import sqlite3
import os

caminho_absoluto = os.path.abspath(__file__)
raiz_do_projeto = os.path.dirname(os.path.dirname(caminho_absoluto))
caminho_db = os.path.join(raiz_do_projeto, 'data', 'chamados.db')

colunas_permitidas =  {'nome_completo',
                       'plano',
                       'cidade',
                       'consumo_gb',
                       'status'
                       }

def consultar_banco_dados(filtro: dict) -> list:

  '''Busca clientes no banco de dados aplicando filtros exatos.

  COLUNAS DISPONÍVEIS E VALORES ACEITOS:

  - cidade: 'Nova Iguaçu', 'Duque de Caxias', 'São Gonçalo', 'Niterói',
            'Campinas', 'Santos', 'Guarulhos', 'Ribeirão Preto',
            'Uberlândia', 'Contagem', 'Juiz de Fora', 'Petrópolis'

  - plano: 'premium', 'basico', 'plus'

  - status: 'ativo', 'inativo'

  - nome_completo: nome exato do cliente

  - consumo_gb: número inteiro ex: 100

  REGRAS:
  1 - Use APENAS as colunas listadas acima
  2 - Respeite maiúsculas, minúsculas e acentos EXATAMENTE como mostrado
  3 - Nunca passe mais de 3 filtros ao mesmo tempo

  Exemplos:
  {'cidade': 'São Gonçalo'}
  {'cidade': 'São Gonçalo', 'status': 'ativo'}
  {'plano': 'premium'}
  '''

  for coluna in filtro:
    if coluna not in colunas_permitidas:
    
      raise ValueError(

        f'coluna "{coluna}" não exite ou não é permitida'
        f'use apenas colunas permitidas: {colunas_permitidas}'
      )
    
  query = 'SELECT * FROM chamados WHERE 1=1'
  valor_de_busca = []

  for coluna,valor in  filtro.items():
    query = query + f' AND {coluna} = ?'
    valor_de_busca.append(valor)

  with sqlite3.connect(caminho_db) as conexão:
    cursor = conexão.cursor()
    cursor.execute(query, valor_de_busca)
    resultado = cursor.fetchall()

    return resultado
  

colunas_ordenacao_permitidas = {'id_registro',
                                'nome_completo',
                                'consumo_gb', 
                                'cidade', 
                                'plano', 
                                'status'
                                }


def consultar_banco_dados_avancado(filtros: dict = {},
                                   ordenar_por: str = None,
                                   ordem: str = 'ASC', 
                                   limite: int = None,
                                   busca_parcial: bool = False) -> list:
    

    '''Busca clientes com suporte a busca parcial, ordenação e limite.

    Use quando:
     Usuário pedir busca parcial
    ex:
    'clientes com nome começando com I'
       busca_parcial=True, filtros={'nome_completo': 'I%'}

     Usuário pedir o primeiro ou último cliente
      ex:
       ordenar_por='id_registro', limite=1

     Usuário pedir quantidade limitada: 'me dá 5 clientes ativos'
      ex:
       filtros={'status': 'ativo'}, limite=5

    Para busca parcial use % como coringa
    ex:
      'I%'        começa com I
      '%Silva'    termina com Silva
      '%Silva%'   contém Silva em qualquer posição

    Colunas disponíveis para filtros: nome_completo, plano, cidade, consumo_gb, status
    Colunas disponíveis para ordenar_por: id_registro, nome_completo, consumo_gb, cidade, status
   
     ex:
    filtros={'nome_completo': 'I%'}, busca_parcial=True
    filtros={'status': 'ativo'}, ordenar_por='id_registro', limite=1
    filtros={'cidade': 'Niterói'}, limite=5

    Ordem: direção da ordenação, 'ASC' (padrão) ou 'DESC'
    ex:
      ordenar_por = 'consumo_gb', ordem='DESC'   maior consumo primeiro
      ordenar_por = 'nome_completo', ordem='ASC'  ordem alfabética
    '''
    

    for coluna in filtros:
      if coluna not in colunas_permitidas:
        raise ValueError (f'coluna"{coluna}" não permitida. use: {colunas_permitidas}')
    query = 'SELECT * FROM chamados WHERE 1=1'
    valores = []

    for coluna, valor in filtros.items():
      if busca_parcial:
        query += f' AND {coluna} LIKE ?'
      else:
        query += f' AND {coluna} = ?'
      valores.append(str(valor))

    if ordenar_por in colunas_ordenacao_permitidas:
      direcao = 'DESC' if ordem.upper() == 'DESC' else 'ASC'
      query += f' ORDER BY {ordenar_por} {direcao}'
    

    if limite:
      query += f' LIMIT {limite}'
    

    with sqlite3.connect(caminho_db) as conexao:
      cursor = conexao.cursor()
      cursor.execute(query, valores)
      return cursor.fetchall()

