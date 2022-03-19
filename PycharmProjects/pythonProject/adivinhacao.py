print('*'*25)
print('*  Jogo da Adivinhação  *')
print('*'*25)

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (total_de_tentativas >0):
    chute=int(input(f'Rodada: {rodada} Digite seu numero: '))
    print('Voce digitou: ', chute)

    acertou=numero_secreto==chute
    maior=chute > numero_secreto
    menor=chute < numero_secreto

    if (acertou):
        print('Vocẽ acertou !!!')
        break
    elif (maior):
        print('Numero maior que numero secreto !')
    elif (menor):
        print('Numero menor que numero secreto !')
    total_de_tentativas -=1
    rodada +=1
print('Fim de Jogo !!!')