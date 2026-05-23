import csv
import random

def gerar_massa_dados(
                      caminho_do_arquivo='data/clientes.csv',
                      primeiro_nome = [
                     'Alan', 'Bia', 'Carlos', 'Diego',
                     'Elena', 'Fabio', 'Gisele', 'Heitor',
                     'Igor', 'Julia', 'Kevin', 'Larissa',
                     'Mateus', 'Natalia', 'Otavio', 'Patricia',
                     'Rafael', 'Sabrina', 'Tiago', 'Vanessa',
                     'William', 'Yasmin', 'Lucas', 'Mariana', 'Rodrigo'
],
                      segundo_nome = [
                     'Silva', 'Souza', 'Lima', 'Santos',
                     'Costa', 'Oliveira', 'Pereira', 'Rodrigues',
                     'Almeida', 'Nascimento', 'Ribeiro', 'Carvalho',
                     'Gomes', 'Martins', 'Araujo', 'Pinto',
                     'Barbosa', 'Melo', 'Castro', 'Teixeira'
],
                      plano=['premium','basico','plus'],
                      consumo_gb_minimo = 10,
                      consumo_gb_maximo = 500,
                      status=['ativo','inativo'],
                      quantia_clientes = 150,

                      cidade=[
                    'Nova Iguaçu','Duque de Caxias',
                    'São Gonçalo','Niterói',
                    'Campinas','Santos',
                    'Guarulhos','Ribeirão Preto',
                    'Uberlândia','Contagem',
                    'Juiz de Fora','Petrópolis'
]
):
    with open(caminho_do_arquivo, mode='w', newline='', encoding='utf-8') as file:
        escritor_nomes = csv.writer(file)
        escritor_nomes.writerow([
                                'nome_completo',
                                'plano',
                                'cidade',
                                'consumo_gb',
                                'status']
                                )
        for cliente in range(1,quantia_clientes + 1):

            nome_primario_aleatorio = random.choice(primeiro_nome)
            nome_secundario_aleatorio = random.choice(segundo_nome)

            nome_completo = f"{nome_primario_aleatorio} {nome_secundario_aleatorio}"

            cidade_aleatoria = random.choice(cidade)
            consumo_gb_aleatorio = random.randint(consumo_gb_minimo,consumo_gb_maximo)
            status_aleatorio = random.choice(status)
            plano_aleatorio = random.choice(plano)
            
            
            escritor_nomes.writerow([
                                     nome_completo,
                                     plano_aleatorio,
                                     cidade_aleatoria,
                                     consumo_gb_aleatorio,
                                     status_aleatorio 
                                     ])

if __name__=='__main__':
 gerar_massa_dados()
