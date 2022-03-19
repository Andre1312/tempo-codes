'''

'''
import random

sorteio_numero=random.randint(1,100)
tentativas=0
#print(sorteio_numero)

while tentativas<4:
    aposta = int(input('Tente acertar, digite um numero entre 1 e 100: '))
    if aposta==sorteio_numero:
        print('Voce acertou !')
        break
    else:
        tentativas+=1
        print(f'Tentativas: {tentativas}')
