'''
Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.
'''


def dimensoes(matriz):
    li = len(matriz)
    c = 1

    for i in matriz:
        c = len(i)
        
    return li, c


# Programa principal
minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)
