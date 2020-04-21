def imprime_matriz(matriz):
    linhas = len(matriz)
    colulas = len(matriz[0])
    for l in range(linhas):
        for c in range(colulas):
            if c == colulas -1:
                print(f'{matriz[l][c]}')
            else:
               print(f'{matriz[l][c]}', end=' ')

        


minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
