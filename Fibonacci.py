t1 = 0
t2 = 1
cont = 0
n = int(input('Quantos termos você quer ver na sequencia de Fibonacci?'))
while cont <= n:
    t3 = t1 + t2
    t1 = t2 #MOVIMENTAÇÃO DAS VARIÁVEIS
    t2 = t3 #MOVIMENTAÇÃO DAS VARIÁVEIS
    cont+=1
    print (t3, end=' - ')
print('FIM')
