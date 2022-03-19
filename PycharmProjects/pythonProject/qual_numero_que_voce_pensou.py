"""
UFRPE - Departamento Com´putaçao
Curso: Licenciatura em Computaçao
Disciplina: Programaçao 1
Prof.: Dr. Francisco Simoes
Aluno: Andre L. C Barros

ATIVIDADE 4 de PROGRAMAÇAO 1

1) Faça um programa que descubra um número que o usuário pensou através de perguntas e respostas.
O número deve ser entre 0 e 100 e o programa só pode fazer perguntas comparativas
(ex: O número que você pensou é maior que… O número que você pensou é menor que).
    a) faça um programa que descubra o número pensado.
    b) otimize o programa para fazer a menor quantidade possível de perguntas até a adivinhação.
    c) modifique seu programa para receber o intervalo em que o número se encontra
    (ex: número entre 3 e 1000 ou número entre -6 e 15).
"""
import random as rd

tentativas = 0
resposta = False
numero = rd.randint(0, 100)
print('* Programa -Adivinho qual o numero que voce pensou ! *')
print('Escolha um numero entre 0 e 100')
comecar = str(input('Pressione s ou S para começar!'))
if comecar == 's' or comecar == 'S':
    while not resposta:
        acertou = input(f'o numero é {numero}? (s para sim ou n para nao)')
        tentativas += 1
        if acertou == 's' or acertou == 'S':
            print('-'*40)
            print(f'Depois de {tentativas} tentativa(s).')
            print(f'Conseguimos acertar o numero pensado que é {numero} !')
            print('-' * 40)
            resposta = True
        elif acertou == 'n' or acertou == 'N':
            numero_anterior = numero
            numero = rd.randint(0, 100)
            if numero == numero_anterior:
                numero = rd.randint(0, 100)
