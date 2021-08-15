from random import randint
from time import sleep
pc = randint(1, 10)
contvit = 0
while True:
    print('-=-'*9)
    jogador = int(input('Digíte um número de 0 a 10: '))
    if jogador > 10 or jogador < 0:
        print('\033[31mOPÇÃO INVÁLIDA\033[m')
    else:
        escolha = int(input('''\033[33mPAR\033[m   [ 1 ]\n\033[34mIMPAR\033[m [ 2 ]\nSUA ESCOLHA: '''))
        if escolha == 1 or escolha == 2:
            print('3')
            sleep(0.5)
            print('2')
            sleep(0.5)
            print('1')
            sleep(0.5)
            print('\033[33mPar ou Impar!\033[m')
            sleep(0.5)
            if escolha == 1: #escolha 'PAR'
                par = pc + jogador
                if par % 2 == 0:
                    print('-=-'*18)
                    print(f'\033[32mVocê ganhou!\033[m O computador escolheu {pc} e você {jogador}\nSomando os dois dá {pc + jogador} = \033[32mPAR\033[m')
                    print('-=-'*18)
                    print('\033[36mLoading...\033[m')
                    sleep(2.5)
                    contvit += 1
                else:
                    print('-=-'*18)
                    print(f'\033[31mVocê foi derrotado!\033[m O computador escolheu {pc} e você {jogador}\nSomando os dois dá {pc + jogador} = \033[31mIMPAR\033[m')
                    print('GAME OVER!')
                    print('-=-'*18)
                    print('\033[36mLoading...\033[m')
                    sleep(2.5)
                    break
            if escolha == 2:
                impar = pc + jogador
                if impar % 2 != 0:
                    print('-=-'*18)
                    print(f'\033[32mVocê ganhou!\033[m O computador escolheu {pc} e você {jogador}\nSomando os dois dá {pc + jogador} = \033[32mIMPAR\033[m')
                    print('-=-'*18)
                    print('\033[36mLoading...\033[m')
                    sleep(2.5)
                    contvit += 1
                else:
                    print('-=-'*18)
                    print(f'\033[31mVocê foi derrotado!\033[m O computador escolheu {pc} e você {jogador}\nSomando os dois dá {pc + jogador} = \033[31mPAR\033[m')
                    print('GAME OVER!')
                    print('-=-'*18)
                    print('\033[36mLoading...\033[m')
                    sleep(2.5)
                    break
        else:
            print('\033[31mOPÇÃO INVÁLIDA\033[m\nJOGUE NOVAMENTE, POR FAVOR')
if contvit > 0:
    print(f'Você terminou o jogo em uma sequência de \033[32m{contvit} vitórias\033[m')
    print('-=-'*18)
    sleep(3)
else:
    print('\033[31mPerdeu de primeira!\033[m Mais sorte da próxima vez...')
    sleep(3)
