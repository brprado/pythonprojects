#ANÁLISE DE NÚMEROS PRIMOS
n = int(input('Digite um número: '))
tot = 0
for div in range (1, n + 1):
    if n % div == 0:
        print("\033[34m", end=' ') #se for divisivel por 'div' usa uma cor
        tot = tot + 1
    else:
        print('\033[m', end= ' ') # se não for divisivel, sem cor
    print(f'{div}', end=' ')
print(f'\n\033[mEste número foi divido {tot} vezes')
if tot == 2: #contador. números primos só são divisíveis por 1 e por ele mesmo

    print('\033[32me por isso ele é um número PRIMO')
else:
    print('\033[31mEste número NÃO É PRIMO')
