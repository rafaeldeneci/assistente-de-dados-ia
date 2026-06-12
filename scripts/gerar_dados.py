import csv
import random
import os

caminho_absoluto = os.path.abspath(__file__)
raiz = os.path.dirname(os.path.dirname(caminho_absoluto))

def gerar_massa_dados(
                      caminho_do_arquivo=os.path.join(raiz,'data','clientes.csv'),
                     primeiro_nome = [
        'Alan', 'Bia', 'Carlos', 'Diego', 'Elena', 'Fabio', 'Gisele', 'Heitor',
        'Igor', 'Julia', 'Kevin', 'Larissa', 'Mateus', 'Natalia', 'Otavio', 'Patricia',
        'Rafael', 'Sabrina', 'Thiago', 'Vanessa', 'William', 'Yasmin', 'Lucas', 'Mariana',
        'Rodrigo', 'Marcos', 'Davi', 'Ana', 'Maria', 'Robson', 'Roberto', 'Yuri',
        'Marlon', 'Arthur', 'Miriam', 'Amanda', 'Alice', 'Beatriz', 'isac', 'Bruna',
        'Camila', 'Carolina', 'Clara', 'Daniela', 'Eduarda', 'João', 'Nicolas',
        'Victor', 'Helena', 'Henrique', 'Raphael', 'Murilo', 'Pedro', 'Sofia', 'Laura',
        'Sonia', 'Marta', 'Fabricio', 'Andreia', 'Marcelho', 'Guilherme', 'Kauã', 'Leonardo',
        'Veronica', 'Valmir', 'Sandra', 'Maicon', 'Ruan', 'Angelina', 'Armando', 'Ramon',
        'Sandro', 'Isabel', 'Astrogilda', 'Antonieta', 'Enzo', 'Valentina', 'Lorenzo', 'Theo', 
        'Benício', 'Isaac', 'Felipe', 'Gabriel', 'Gustavo', 'Samuel', 'Daniel', 'Vitor', 
        'Eduardo', 'Luiz', 'Antônio', 'Francisco', 'Augusto', 'Alexandre', 'Ricardo', 'Renato', 
        'Fernando', 'Henry', 'Oliver', 'Thomas', 'Ian', 'Eric', 'Giovanna', 'Leticia', 
        'Gabriela', 'Luana', 'Juliana', 'Fernanda', 'Aline', 'Jessica', 'Rafaela', 'Isabela', 
        'Vitória', 'Nicole', 'Rebeca', 'Taís', 'Andressa', 'Isadora', 'Lorena', 'Milena', 
        'Bárbara', 'Danielle', 'Priscila', 'Caroline', 'Manuela', 'Sophia', 'Heloísa', 'Luiza', 'Mirella'
],
                      segundo_nome = [
        'Silva', 'Souza', 'Lima', 'Santos', 'Costa', 'Oliveira', 'Pereira', 'Rodrigues',
        'Almeida', 'Nascimento', 'Ribeiro', 'Carvalho', 'Gomes', 'Martins', 'Araujo', 'Pinto',
        'Barbosa', 'Melo', 'Castro', 'Teixeira', 'Vasconcelo', 'Azevedo', 'Farias',
        'Ferreira', 'Fonseca', 'Figueredo', 'castro', 'Cunha', 'Dias', 'Lacerda', 'Lopes',
        'Machado', 'Medeiros', 'Miranda', 'Monteiro', 'Moraes', 'Moreira', 'Nunes', 'Pacheco',
        'Ramos', 'Rocha', 'Sales', 'Silveira', 'Tavares', 'Torres', 'Vieira', 'Xavier',
        'Antunes', 'Braga', 'Campos', 'Cardoso', 'Correia', 'Duarte', 'Freitas', 'Guimarães',
        'Leal', 'Leite', 'Macedo', 'Marques', 'Mendes', 'Mesquita', 'Neves', 'Paiva',
        'Pinheiro', 'Prado', 'Queiroz', 'Reis', 'Santana', 'Vargas', 'Vasconcelos', 'Siqueira',
        'Guerra', 'Borges', 'Carneiro', 'Pires', 'Fogaça', 'Aragão', 'Garrido', 'Amaral',
        'Peixoto', 'Maldonado', 'Fontes', 'Andrade', 'Barros', 'Batista', 'Brito', 'Caldeira',
        'Camargo', 'Chaves', 'Coelho', 'Cordeiro', 'Cruz', 'Fagundes', 'Freire', 'Furtado',
        'Galvão', 'Giacomo', 'Godoy', 'Goulart', 'Lemos', 'Linhares', 'Luz', 'Maia',
        'Meireles', 'Mello', 'Menezes'
],
                      planos = {'basico':{'consumo':(15,40),'mensalidade':(70)},
                                'premium':{'consumo':(50,100),'mensalidade':(120)},
                                'plus':{"consumo":(150,350),'mensalidade':(240)},
                                },
                    
                    
                      quantia_clientes = 150,

                      estados = {'São Paulo':{'campinas','Santos','Guarulhos','Ribeirão Preto',
                                              'São Bernardo do Campo','Santo André','Osasco',
                                              'Sorocaba','Mauá','Bauru'},

                                 'Rio De Janeiro':{'Nova Iguaçu','Duque de Caxias','São Gonçalo','Niterói',
                                                   'Petrópolis','Volta redonda','Campos dos Goytacazes',
                                                   'Belford roxo','Macaé','Cabo Frio'},

                                'Minas Gerais':{'Belo Horizonte','Juiz de Fora','Uberlandia',
                                                'Contagem','Betim','Montes claros',
                                                'Governador Valadares','Uberaba','Ipatinga',
                                                'Sete Lagoas'}
                                },

                      

):
    with open(caminho_do_arquivo, mode='w', newline='', encoding='utf-8') as file:
        escritor_nomes = csv.writer(file)
        escritor_nomes.writerow([
                                'nome_completo',
                                'plano',
                                'estado',
                                'cidade',
                                'consumo_Gb',
                                'mensalidade',
                                'status',
                                'inadinplencia',
                                ]
                                )
        for cliente in range(1,quantia_clientes + 1):

            nome_primario_aleatorio = random.choice(primeiro_nome)
            nome_secundario_aleatorio = random.choice(segundo_nome)
            nome_completo = f"{nome_primario_aleatorio} {nome_secundario_aleatorio}"

            estados_aleatorio = random.choice(list(estados.keys()))
            cidade_aleatoria = random.choice(list(estados[estados_aleatorio]))

            plano_aleatorio = random.choice(list(planos.keys()))
            consumo_min,consumo_max = planos[plano_aleatorio]['consumo']
            consumo_total = random.randint(consumo_min,consumo_max)
            mensalidade = planos[plano_aleatorio]['mensalidade']

            status_aleatorio = random.choices(['ativo','inativo'],weights=[76,34])[0]
            inadinplencia_aleatoria = random.choices(['sim','não'],weights=[27,74])[0]

            
            escritor_nomes.writerow([nome_completo,
                                     plano_aleatorio,
                                     estados_aleatorio,
                                     cidade_aleatoria,
                                     consumo_total,
                                     mensalidade,
                                     status_aleatorio,
                                     inadinplencia_aleatoria ])
            
        

