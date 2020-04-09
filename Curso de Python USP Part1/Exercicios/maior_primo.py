'''
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.
'''

def eprimo(n):
    cont = 0
    for i in range(1, n):
        if n % i == 0:
            cont += 1
        if cont > 1:
            break
    if cont > 1:
        return False
    else:
        return True

def maior_primo(n):
    primo = n
    j = 0
    while j <= n:
        if eprimo(j):
            primo = j
        j += 1
    return primo


print(maior_primo(100))
print(maior_primo(7))
