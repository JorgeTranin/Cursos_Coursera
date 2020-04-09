
n = int(input('Digite um número inteiro: '))

cont = 1
primo = 0
while cont <= n:
    if n % cont == 0:
        primo += 1
    cont += 1

if primo == 2:
    print('primo')

else:
    print('não primo')
