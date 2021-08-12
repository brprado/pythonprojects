#ANÁLISE DE DADOS PESSOAIS (MÉDIA DE IDADE, HOMEM MAIS VELHO E MULHERES C/ MENOS DE 20 ANOS)
totmulher20 = 0
for i in range (1, 5):
    print(f'-=-=-=-=-=-=-{i}ª PESSOA-=-=-=-=-=-=-')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('GÊNERO [ M ] OU [ F ]: '))
    somaidade += idade
    if i == 1 and sexo in ('Mm'): #UNNECESSARY LINE #se for a primeira pessoa do laço... atribui à variável seu nome e idade
        maioridhom = idade #UNNECESSARY LINE
        nomevelhom = nome #UNNECESSARY LINE
    if sexo in 'Mm' and idade > maioridhom: #se o sexo for M e a idade for maior do que a da primeira pessoa OU da anterior, atribui à variável a idade e seu nome
        maioridhom = idade
        nomevelhom = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20+=1
medidade = somaidade / 4
print(f'A média de idade do grupo é de {medidade}')
print(f'O homem mais velho se chama {nomevelhom} e ele tem {maioridhom} anos')
print(f'{totmulher20} mulher(es) tem menos de 20 anos de idade')
