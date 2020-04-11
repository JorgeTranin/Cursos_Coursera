largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

for i in range(0, altura):
    cont = 0
    while cont <= largura - 1:
        if i == 0 or i == altura - 1:
            print('#', end='')
        else:
            if cont == 0 or cont == largura - 1:
                print('#', end='')
            else:
                print(' ', end='')
        cont += 1
    print()
