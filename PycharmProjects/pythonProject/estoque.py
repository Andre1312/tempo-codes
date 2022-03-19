
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
cliente=[]
produtos=[]
qtde_produtos=[]

# Cadastra o estoque 10 itens
print('* Controle de Estoque *')
print('- Cadastro - Prencha com o codigo do produto e a quantidade: ')
for ordem in range(1,11,1):
    produto=int(input(f'Entre com o codigo do produto -{ordem}-:'))
    produtos.append(produto)
    qtde_produto=int(input(f'Entre a quantidade do produto -{ordem}-:'))
    qtde_produtos.append(qtde_produto)

# Mostra o estoque atualizado
print('* Estoque Atualizado *')
for ordem in range(1,11,1):
    print('Ordem-----Produto-----Qtde')
    print(f'{ordem}-----{produtos[ordem]}-----{qtde_produtos[ordem]}')

sair = False
while not sair :
    print('* Controle de Estoque *')
    print('-1- Cadastro de Produtos')
    print('-2- Compras')
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
            for ordem in range(1, 11, 1):
                produto = int(input(f'Entre com o codigo do produto -{ordem}-:'))
                produtos.append(produto)
                qtde_produto = int(input(f'Entre a quantidade do produto -{ordem}-:'))
                qtde_produtos.append(qtde_produto)

        elif usar_cadastro=='s':
            # Mostra o estoque
            print('* Estoque Atualizado *')
            for ordem in range(1, 11, 1):
                print('Ordem-----Produto-----Qtde')
                print(f'{ordem}-----{produtos[ordem]}-----{qtde_produtos[ordem]}')

    elif opcao=='2':
