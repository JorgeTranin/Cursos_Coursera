'''
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Exemplos de execução no shell de Python

Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.

Como enviar
Quando você estiver pronto para enviar, você pode fazer upload dos arquivos para cada parte da tarefa na guia "Meu envio".
'''


def vogal(c):

    if c in 'AEIOUaeiou':
        return True
    else:
        return False


print(vogal('a'))

print(vogal('b'))

print(vogal('E'))
