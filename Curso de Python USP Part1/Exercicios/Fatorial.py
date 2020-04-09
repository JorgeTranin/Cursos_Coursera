n = int(input('Digite o valor de n: '))

if n == 0:
    n = 1
fatorial = 1
cont = n
while cont != 1:

    fatorial *= cont
    cont -= 1


print(fatorial)
