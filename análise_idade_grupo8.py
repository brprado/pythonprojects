from datetime import date
atual = date.today().year
cont = 0
cont2 = 0
for i in range (1, 8):
    n = int(input(f'Digite o ano de nascimento {i}°: '))
    idade = atual - n
    if idade >= 18:
        cont+=1
    elif idade < 18:
        cont2+=1
print(f'\033[32m{cont}\033[m pessoa(s) desta lista é(são) maior(es) de idade')
print(f'\033[33m{cont2}\033[m pessoa(s) desta lista é(são) menor(es) de idade')
