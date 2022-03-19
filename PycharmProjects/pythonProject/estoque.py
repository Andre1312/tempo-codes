
"""
UFRPE - Departamento Com´putaçao
Curso: Licenciatura em Computaçao
Disciplina: Programaçao 1
Prof.: Dr. Francisco Simoes
Aluno: Andre L. C Barros

ATIVIDADE 5 de PROGRAMAÇAO 1 (VA1)

Programa para preencher o estoque de mercadorias de uma empresa.
Inicialmente o programa deverá preencher 2 vetores com 10 posições cada,
onde o primeiro corresponde ao código de produto e o segundo ao total desse
produto em estoque.


"""
pedidos=[]
produtos=[]
qtde_produtos=[]

sair = False
while not sair :
    print('* Controle de Estoque *')
    print('-1- Cadastro de Produtos')
    print('-2- Imprime Estoque Atualizado')
    print('-3- Pedidos')
    print('-4- Imprime Lista de Pedidos')
    print('-S- Sair')
    opcao=str(input('Opção: ')).strip().lower()

    if opcao=='s':
        print('Programa de Controle de Estoque FINALIZADO !')
        break
    elif opcao=='1':
        print('* Controle de Estoque *')
        usar_cadastro=str(input('Usar o mesmo cadastro? -S- para Sim -N- para Não: ')).strip().lower()

        if usar_cadastro=='n':
            print('- Cadastro - Prencha com o codigo do produto e a quantidade: ')
            for ordem in range(0, 10, 1):
                produto = int(input(f'Entre com o codigo do produto -item:{ordem}-:'))
                produtos.append(produto)
                qtde_produto = int(input(f'Entre a quantidade do produto -item:{ordem}-:'))
                qtde_produtos.append(qtde_produto)

        elif usar_cadastro=='s':
            produtos=[1,11,21,31,41,51,61,71,81,91]
            qtde_produtos=[30,25,65,35,45,85,80,95,10,20]
            # Mostra o estoque
            print('-' * 40)
            print('* Estoque Atualizado *')
            print('\tOrdem\tProduto\tQtde')
            for ordem in range(0, len(produtos)):
                print(f'\t{ordem}\t\t{produtos[ordem]}\t\t{qtde_produtos[ordem]}')
            print('-' * 40)

    elif opcao=='2':
        # Mostra o estoque
        print('-' * 40)
        print('* Estoque Atualizado *')
        print('\tOrdem\tProduto\tQtde')
        for ordem in range(0, len(produtos)):
            print(f'\t{ordem}\t\t{produtos[ordem]}\t\t{qtde_produtos[ordem]}')
        print('-' * 40)

    elif opcao=='3':
        print('-' * 40)
        print('* Pedidos *')
        cliente=int(input('Entre código cliente: '))
        # se codigo cliente = 0 finaliza programa
        if cliente==0:
            print('Programa de Controle de Estoque FINALIZADO !')
            break
        pedido_produto=int(input('Entre codigo do produto: '))
        if pedido_produto in produtos:
            pedido_qtde=int(input('Entre quantidade do produto: '))
            idx = produtos.index(pedido_produto)
            qtde = qtde_produtos[idx]
            if qtde >= pedido_qtde:
                qtde = qtde - pedido_qtde
                qtde_produtos[idx] = qtde
                print('Pedido Atendido. Obrigado e Volte Sempre.')
                # atualiza lista pedidos
                pedidos.append(cliente)
                pedidos.append(pedido_produto)
                pedidos.append(pedido_qtde)

            elif qtde < pedido_qtde:
                print(f'Nao temos estoque suficiente dessa mercadoria. Codigo Produto:{pedido_produto}.')
                # atualiza lista pedidos
                pedidos.append(cliente)
                pedidos.append(pedido_produto)
                pedidos.append(0)
        else:
            print(f'Codigo inexistente. Codigo Produto:{pedido_produto}.')

    elif opcao == '4':
        print('-' * 40)
        print('* Lista de Pedidos *')
        print('\tOrdem\t\tCliente\t\tProduto\t\tQtde')
        if len(pedidos)==0:
            idx=3
        else:
            idx=len(pedidos)-3
        c=0
        for item in range(0,idx,3):
            print(f'\t{c}\t\t{pedidos[item]}\t\t{pedidos[item+1]}\t\t{pedidos[item+2]}')
            c += 1
        print('-' * 40)