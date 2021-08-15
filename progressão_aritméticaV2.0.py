r = int(input('Digite a razão: '))
termos = 10
while termos > 0:
    print(termo)
    termo = termo + r
    termos -= 1
    if termos == 0:
        print('PAUSA')
        termos = int(input('Quantos valores a mais você quer ver? '))
        if termos == 0:
            print('Saindo do programa...')
            sleep(3)
            exit()
