'''
Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2) que recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário.
'''


def sao_multiplicaveis(m1, m2):
    numeroColunas_m1 = 0
    for l in m1:
        numeroColunas_m1 = len(l)
    if numeroColunas_m1 == len(m2):
        return True
    else:
        return False


m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
print(sao_multiplicaveis(m1, m2))
