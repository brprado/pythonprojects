#JOKENPO.PY
from random import randint
from time import sleep
contvit = 0
pc = randint(1,3) 
while True:
    print('='*5,'JOKENPO.PY', '='*5)
    jogador = int(input('''
    \033[32mPEDRA\033[m  [ 1 ]
    \033[33mPAPEL\033[m  [ 2 ]
    \033[34mTESOURA\033[m[ 3 ]
    Escolha a sua opção: '''))
    print('JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('PO!!!')
    sleep(0.3)
    if jogador == 1: #jogador = pedra
        if pc == 1:
            print('\033[33mEmpate\033[m')
            print('Tente novamente!')
            print('-' * 22)
            print('Loading...')
            sleep(3)
        elif pc == 2:
            print('O computador escolheu papel')
            print('\033[31mVocê perdeu\033[m')
            print('\033[31mGAME OVER\033[m')
            print('Loading...')
            sleep(3)
            print('-=-' * 20)
            break
        elif pc == 3:
            print('O computador escolheu tesoura')
            print('\033[32mVocê ganhou!\033[m')
            contvit += 1
            print(f'Você está com \033[32m{contvit}\033[m pontos')
            print('Loading...')
            sleep(3)
            print('-' * 22)
    if jogador == 2: #jogador jogou papel
        if pc == 1:
            print('O computador escolheu pedra!')
            print('\033[32mVocê ganhou!\033[m')
            contvit += 1
            print(f'Você está com \033[32m{contvit}\033[m pontos')
            print('Loading...')
            sleep(3)
            print('-' * 22)
        elif pc == 2: 
            print('\033[33mEmpate\033[m')
            print('Tente novamente!')
            print('Loading...')
            sleep(3)
            print('-' * 22)
        elif pc == 3:
            print('O computador escolheu tesoura')
            print('\033[31mVocê perdeu\033[m')
            print('\033[31mGAME OVER\033[m')
            print('Loading...')
            sleep(3)
            print('-=-' * 20)
            break
    if jogador == 3: #jogador jogou tesoura
        if pc == 1:
            print('O computador escolheu pedra')
            print('\033[31mVocê perdeu\033[m')
            print('\033[31mGAME OVER\033[m')
            print('Loading...')
            sleep(3)
            print('-=-' * 20)
            break
        elif pc == 2:
            print('O computador escolheu papel')
            print('\033[32mVocê ganhou!\033[m')
            print(f'Você está com \033[32m{contvit}\033[m pontos')
            print('Loading...')
            sleep(3)
            contvit += 1
            print('-' * 22)
        elif pc == 3:
            print('\033[33mEmpate\033[m')
            print('Tente novamente!')
            print('Loading...')
            sleep(3)
            print('-' * 22)
print(f'Você conquistou \033[32m{contvit}\033[m vitória(a) consecutiva(s)')
print('-=-' * 20) 
