def computador_escolhe_jogada(n, m):
    pc_remove = 1
    while pc_remove != m:
        if (n - pc_remove) % (m+1) == 0:
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


def campeonato():

    for i in range(0, 3):
        print()
        print(f'**** Rodada {i+1} ****')
        print()
        partida()

    print()
    print('**** Final do campeonato! ****')
    print()
    print('Placar: Você 0 X 3 Computador')


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

    while n > 0:
        if usuario:
            escolha_do_usuario = usuario_escolhe_jogada(n, m)
            print()

            if escolha_do_usuario == 1:
                print('Você tirou uma peça.')

            else:
                print(f'Voce tirou {escolha_do_usuario} peças.')

            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n != 0:
                print(
                    f'Agora resta  {n - escolha_do_usuario} peça no tabuleiro.')

            n -= escolha_do_usuario
            usuario = False

        else:
            escolha_do_pc = computador_escolhe_jogada(n, m)
            print()
            if escolha_do_pc == 1:
                print('O computador tirou uma peça.')
            else:
                print(f'O computador tirou {escolha_do_pc} peças.')

            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n != 0:
                print(f'Agora resta  {n - escolha_do_pc} peça no tabuleiro.')
            print()

            n -= escolha_do_pc
            usuario = True

    print('Fim do jogo! O computador ganhou!')


# Programa Principal!!
print()
print('Bem-vindo ao jogo do NIM! Escolha:')
print()

while True:
    print('1 - para jogar uma partida isolada')
    partida_ou_campeonato = int(input('2 - para jogar um campeonato '))
    if partida_ou_campeonato == 2:
        print()
        print('Voce escolheu um campeonato!')
        print()
        campeonato()
        break
    elif partida_ou_campeonato == 1:
        print()
        print('Voce escolheu partida isolada')
        print()
        partida()
        break
    else:
        print('Numero invalido tente de novo! ')
