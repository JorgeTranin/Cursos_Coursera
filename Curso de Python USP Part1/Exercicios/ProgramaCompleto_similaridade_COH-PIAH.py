import re


def le_assinatura():
    """[A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos]

    Returns:
        [list] -- [description]
    """

    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """[A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento]

    Returns:
        [Lista] -- [Cada texto com 1 elemento]
    """
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    """[A funcao recebe um texto e devolve uma lista das sentencas dentro do texto]

    Arguments:
        texto {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """[A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca]

    Arguments:
        sentenca {[str]} -- [recebe uma frase]

    Returns:
        [lista] -- [lista das frases contidas na sentença]
    """

    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """[A funcao recebe uma frase e devolve uma lista das palavras dentro da frase]

    Arguments:
        frase {[str]} -- [Uma frase]

    Returns:
        [lista] -- [Retorna uma lista de palavras dentro da frase recebida]
    """

    return frase.split()


def n_palavras_unicas(lista_palavras):
    """[Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez]

    Arguments:
        lista_palavras {[list]} -- [Recebe uma lista de palavras]

    Returns:
        [int] -- [Devolve o numero de palavras que aparecem uma unica vez]
    """

    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """[Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas]

    Arguments:
        lista_palavras {[list]} -- [lista de palavras]

    Returns:
        [int] -- [Retorna o tamanho de palavras diferentes]
    """

    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    """[IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.]

    Arguments:
        as_a {[list]} -- [description]
        as_b {[list]} -- [description]

    Returns:
        [float] -- [Grau de similaridade dos textos]
    """

    soma_das_similaridade = 0

    for i in range(0, 6):
        soma_das_similaridade += (abs(as_a[i] - as_b[i]))

    return soma_das_similaridade / 6


def calcula_assinatura(texto):
    """[IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.]

    Arguments:
        texto {[list]} -- [lista recebida de um texto]

    Returns:
        [list] -- [devolve a assinatura que o usuario é ou não infectado pelo COH-PIAH]
    """
    ''''''
    sentenças = separa_sentencas(texto)
    frases = list()
    palavras = list()
    meias_palavras = 0
    meias_sentenças = 0
    comp_sentenças = 0
    rel_type_token = 0
    hapax = 0
    soma_caractere_das_sentenças = 0
    soma_das_palavras = 0
    soma_os_caracteres_das_frases = 0
    tamanho_meio_frase = 0

    for sentença in sentenças:
        soma_caractere_das_sentenças += len(sentença)
        l_frases = separa_frases(sentença)

        for fra in l_frases:
            frases.append(fra)
    for frase in frases:
        soma_os_caracteres_das_frases += len(frase)
        lista_palavra = separa_palavras(frase)

        for palavra in lista_palavra:
            palavras.append(palavra)

    for palavra in palavras:
        soma_das_palavras += len(palavra)

    meias_palavras = soma_das_palavras / len(palavras)
    rel_type_token = n_palavras_diferentes(palavras) / len(palavras)
    hapax = n_palavras_unicas(palavras) / len(palavras)
    meias_sentenças = soma_caractere_das_sentenças / len(sentenças)
    comp_sentenças = len(frases) / len(sentenças)

    tamanho_meio_frase = soma_os_caracteres_das_frases / len(frases)

    return [meias_palavras, rel_type_token, hapax,meias_sentenças,comp_sentenças, tamanho_meio_frase]


def avalia_textos(textos, ass_cp):
    """[IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.]

    Arguments:
        textos {[list]} -- [description]
        ass_cp {[list]} -- [description]

    Returns:
        [int] -- [description]
    """
    ''''''
    inf = []

    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        inf.append(compara_assinatura(ass_texto, ass_cp))

    menor = inf[0]
    c = 1

    for i in range(1, len(inf)):
        if (menor < inf[i]):
            c = i
    return c


# Programa Principal main

assinatura = le_assinatura()
textos = le_textos()
avaliar = avalia_textos(textos, assinatura)

print(f'O autor do texto {avaliar} está infectado com COH-PIAH')
