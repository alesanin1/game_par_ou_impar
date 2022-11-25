from random import randint
print ('#JOGO DO PAR OU IMPAR#')
qnt_victory=0

while True:
    while True:
        numero_maquina = randint(1, 10)
        while True:
            numero_user = str(input('Diga um Número: '))
            if numero_user.isnumeric():
                numero_user=int(numero_user)
                break
        par_ou_impar=' '
        while par_ou_impar not in 'PI':
            par_ou_impar = str(input('Você quer par ou impar? (P/I): ')).upper().strip()[0]
        soma_numeros = numero_maquina+numero_user
        
        if soma_numeros % 2 == 0:
            if par_ou_impar == 'P':
                qnt_victory += 1
                print('=~'*25)
                print(f'PARABÉNS, VOCÊ ESCOLHEU PAR E VENÇEU! \n(pc= {numero_maquina}/você= {numero_user}.)')
                print('=~'*25)

            else:
                print('=~'*25)
                print('QUE PENA, O COMPUTADOR GANHOU! DEU PAR!')
                print('=~'*25)
                break

        else:
            if par_ou_impar == 'I':
                qnt_victory += 1
                print('=~'*25)
                print(f'PARABÉNS, VOCÊ ESCOLHEU IMPAR E VENÇEU! \n(pc={numero_maquina}/você= {numero_user}.)')
                print('=~'*25)
    
            else:
                print('=~'*25)
                print('QUE PENA, O COMPUTADOR GANHOU! DEU IMPAR!')
                print('=~'*25)
                break

    print('=~'*25)
    print(f'O COMPUTADOR DIGITOU {numero_maquina} E VOCÊ {numero_user}')
    print(f'O seu total de vitórias consecutivas foram de {qnt_victory}')
    print('=~'*25)
    qnt_victory=0
    stop=' '
    while stop not in 'SN':
        stop=str(input('Deseja parar?[S/N]: ')).upper()[0]
    if 'S' in stop:
        break
print('FIM DE JOGO, VOLTE SEMPRE!')