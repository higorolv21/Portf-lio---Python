

# DICIONÁRIO PARA ARMAZENAMENTO DOS PRODUTOS
estoque = {
    'Whey Protein': {'Quantidade': 3},
    'Creatina': {'Quantidade': 0},
    'Hipercalórico': {'Quantidade': 0}
}


# FUNÇÃO PARA O MENU 
def menu():
    while True:

        print()
        print('Olá, seja bem vindo ao gereciamento de estoque!')
        print('Escolha uma opção: ')

        print('1. Adicionar um novo produto')
        print('2. Consultar produtos')
        print('3. Exibir estoque')
        print('4. Excluir unidade de produto')
        print('5. Sair')

        
        
        ação = input('Opção: ')

        if ação == '1':
            adicionar_produto()
        elif ação == '2':
            consultar_produtos()
        elif ação == '3':
            exibir_estoque()
        elif ação == '4':
            excluir_produto()
        elif ação == '5':
            print()
            print('Saindo...')
            break


# FUNÇÕES PARA AS AÇÕES

# adicionar produto ao estoque
def adicionar_produto():
    while True:
        nome_produto = input('Digite o nome do produto ou (sair) para sair: ')
        if nome_produto.lower() == 'sair':
            break

        try:
            qtd_produto = int(input('Digite a quantidade: '))
            if nome_produto in estoque:
                estoque[nome_produto]['Quantidade'] += qtd_produto
            else:
                estoque[nome_produto] = {'Quantidade': qtd_produto }
        
        except ValueError:
            print('Erro')
        
   
        
        # Consultar produto
def consultar_produtos():
    verificação = input('Digite o nome do produto para verificar suas informações: ')
    if verificação in estoque:
            print()
            print(f'{verificação}: {estoque[verificação]}')
    else:
        print('Produto não existente')
            


# Exibir estoque completo
def exibir_estoque():
    print()
    print('Consultando estoque completo')
    for itens, qtd in estoque.items():
        print(f'{itens}, {qtd}')



# Excluir produto do estoque
def excluir_produto():
    while True:
        nome_produto = input('Digite o nome do produto para remover unidades, ou digite (sair) para sair: ')
        if nome_produto.lower() == 'sair':
            break

        if nome_produto in estoque:
            
            try:
                qtd_a_remover = int(input('Digite a quantidade que deseja remover: '))
                if qtd_a_remover < 0:
                    print('Quantidade inválida')
                elif qtd_a_remover > estoque[nome_produto]['Quantidade']:
                    print('Quantidade inválida, selecione um valor inferior ou igual à quantidade total')
                else:
                    estoque[nome_produto]['Quantidade'] -= qtd_a_remover
                    print(f'{qtd_a_remover} unidades foram removidas de {nome_produto}')
            
            except ValueError:
                print('Por favor, insira uma quantidade válida')


         
menu()



