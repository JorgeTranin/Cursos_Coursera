'''
Exercício 1 - Maior elemento de uma lista
Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.



'''


def maior_elemento(lista):
    """[Recebe uma lista e devolve o maior elemento]

    Arguments:
        lista {[lista]} -- [lista]

    Returns:
        [int] -- [maior elemento da lista recebida]
    """
    maior = max(lista)
    return maior

print(maior_elemento([1, 2, 3, 4, 5, 6, 10, 11, 12]))
