backup = n = int(input('Digite um número inteiro: '))

anterior = n % 10
n //= 10
iguais = False


while n > 0 and not iguais:
    numeroAtual = n % 10
    if numeroAtual == anterior:
        iguais = True
        
    anterior = numeroAtual
    n = n // 10
if iguais:
    print('sim')
else:
    print('não')
