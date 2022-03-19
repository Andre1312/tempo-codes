'''
UFRPE - Departamento Com´putaçao
Curso: Licenciatura em Computaçao
Disciplina: Programaçao 1
Prof.: Dr. Francisco Simoes
Aluno: Andre L. C Barros

ATIVIDADE 3 de PROGRAMAÇAO 1

Implemente uma mini-Calculadora
Operações:
    Adição
    Subtração
    Multiplicação
    Divisão
    Raiz Quadrada
    Maior de 03 numeros
    Media de 04 numeros
'''
# Apresentação do MENU
print('\nMenu - Calculadora')
print('Selecione a operação desejada:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Raiz Quadrada')
print('6 - Maior de 03 numeros')
print('7 - Media de 04 numeros')
print('0 - Sair')
# entrada da opção
opcao=int(input('Opcao: '))
# Adição
if opcao==1:
    print('_' * 35)
    print('Adição X+Y')
    x=float(input('X: '))
    y=float(input('Y: '))
    print(f'{x} + {y} = {x+y}')
    print('_' * 35)
# Subtração
elif opcao==2:
    print('_' * 35)
    print('Subtração X-Y')
    x=float(input('X: '))
    y=float(input('Y: '))
    print(f'{x} - {y} = {x-y}')
    print('_' * 35)
# Multiplicação
elif opcao==3:
    print('_'*35)
    print('Multiplicação X.Y')
    x=float(input('X: '))
    y=float(input('Y: '))
    print(f'{x} x {y} = {x*y}')
    print('_' * 35)
# Divisão
elif opcao==4:
    print('_' * 35)
    print('Divisão X/Y')
    x=float(input('X: '))
    y=float(input('Y: '))
    print(f'{x} / {y} = {x/y}')
    print('_' * 35)
# Raiz Quadrada
elif opcao==5:
    print('_' * 35)
    print('Raiz Quadrada (X)^(1/2)')
    x=float(input('X: '))
    y=0.5
    print(f'{x}^(1/2) = {x**y:.3f}')
    print('_' * 35)
# Maior de 3 numeros
elif opcao==6:
    print('_'*35)
    print('Maior de 3 numeros (X,Y,Z)')
    x=float(input('X: '))
    y=float(input('Y: '))
    z=float(input('Z: '))
    print(f'Maior entre {x}, {y} e {z} = {max(x,y,z)}')
    print('_' * 35)
# Media entre 4 numeros
elif opcao==7:
    print('_' * 35)
    print('Media entre (X,Y,W,Z)')
    x=float(input('X: '))
    y=float(input('Y: '))
    w=float(input('W: '))
    z=float(input('Z: '))
    print(f'Media entre {x}, {y}, {w} e {z} = {(x+y+w+z)/4:.3f}')
    print('_' * 35)
# Sair do programa
elif opcao==0:
    print('_' * 35)
    print('Programa finalizado')
    print('_' * 35)
# Opção inexistente no menu
else:
    print('_' * 35)
    print('Operação não implementada')
    print('_' * 35)
