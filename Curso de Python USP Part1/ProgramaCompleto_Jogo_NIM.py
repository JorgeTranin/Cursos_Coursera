def computador_escolhe_jogada(n, m):
    pc_remove = 1
    while pc_remove != m:
        if n - pc_remove % (m+1) == 0:
            return pc_remove
        else:
            pc_remove += 1
    return pc_remove

def usuario_escolhe_jogada(n, m):
    while True:
        usuario_removeu = int(input('Quantas peças você vai tirar? '))
        if usuario_removeu > m or usuario_removeu <= 0:
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            break
    return usuario_removeu


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()
    usuario = False
    if n % (m+1) == 0:
        print('Você começa')
        usuario = True
    else:
        print('Computador começa')

    if usuario == True:
        



    escolha_do_usuario = usuario_escolhe_jogada(n, m)
    print()
    print(f'Voce tirou {escolha_do_usuario} peças.')
    print(f'Agora resta  {n - escolha_do_usuario} peça no tabuleiro.')
    print()

    
    



#Programa Principal!!

print('*'*40)
print('Bem-vindo ao jogo do NIM! Escolha:')
print('-='*40)

while True:
    print('1 - para jogar uma partida isolada')
    partida_ou_campeonato = int(input('2 - para jogar um campeonato '))
    if partida_ou_campeonato == 2:
        print('Voce escolheu um campeonato!')

        break
    elif partida_ou_campeonato == 1:
        print('-='*40)
        print('Voce escolheu partida isolada')
        print('-='*40)
        partida()
        break
    else:
        print('Numero invalido tente de novo! ')

