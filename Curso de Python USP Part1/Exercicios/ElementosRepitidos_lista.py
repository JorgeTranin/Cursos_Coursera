'''
Exercício 1 - Removendo elementos repetidos
Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
'''


def remove_repetidos(list):
    """[Remove elementos repitidos de uma lista e devolve outra lista com esses elementos em ordem crescente]

    Arguments:
        list {[lista]} -- [uma lista]

    Returns:
        [lista] -- [elementos em ordem]
    """
    lista2 = []

    for elemento in list:
        if elemento not in lista2:
            lista2.append(elemento)
    lista2.sort()
    return lista2


lista = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista))

print(remove_repetidos([1, 2, 3, 3, 3, 4]))
