'''
Exercício 2 - Soma dos elementos de uma lista
Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

'''


def soma_elementos(lista):
    """[Soma elementos de uma lista]

    Arguments:
        lista {[lista]} -- [quantos numeros quiser]

    Returns:
        [int] -- [elementos somados da lista]
    """
    soma_lista = 0
    for elemento in lista:
        soma_lista += elemento

    return soma_lista


print(soma_elementos([1, 2, 3, 4, 5, 6, 7, 8]))
