def n_primos(n):

    primo = 0
    for i in range(1, n+1):
        for c in range (1, i+1):
            if i % c == 0 and primo <= 2:
                print(i)
                primo += 1
        

n = int(input('digite um numero inteiro: '))  
n_primos(n)


