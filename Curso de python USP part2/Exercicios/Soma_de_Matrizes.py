def dimensoes(matriz):
    li = len(matriz)
    c = 1

    for i in matriz:
        c = len(i)

    return li, c


def soma_matrizes(m1, m2):

    l, c = dimensoes(m1)

    if dimensoes(m1) == dimensoes(m2):
        m3 = m1
        for i in range(0, l):
            for col in range(0, c):
                m3[i][col] = m1[i][col] + m2[i][col]
        return m3
    else:
        return False

