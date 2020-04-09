'''
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder,
respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois
últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
'longe'
na saída. Caso o contrário, quando a distância for menor que 10, imprima
'perto'
Dica: lembre-se que a fórmula da distância para dois pontos num plano cartesiano é a seguinte:

'''
from math import sqrt
x1 = int(input('Digite um numero: '))
y1 = int(input('Digite um numero: '))
x2 = int(input('Digite um numero: '))
y2 = int(input('Digite um numero: '))

Distancia_x_y = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


if Distancia_x_y >= 10:
    print('longe')
else:
    print('perto')
