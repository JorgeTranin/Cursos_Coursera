from math import sqrt

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = b ** 2 - 4 * a * c


if delta == 0:
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    print('a raiz desta equação é', raiz1)

else:
    if delta < 0:
        print('esta equação não possui raízes reais')
    else:
        raiz2 = (-b - sqrt(delta)) / (2 * a)
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        if raiz1 <= raiz2:
            print('as raízes da equação são', raiz1, 'e', raiz2)
        else:
            print('as raízes da equação são', raiz2, 'e', raiz1)
