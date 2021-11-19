import curses
import constant

from random import randint

def novaJanela():
    # configura nova janela
    curses.initscr()

    # cria nova janela
    # lembrar que eixo vertical e horizontal sao invertidos y, x
    window = curses.newwin(constant.ALTURA_JANELA,
                           constant.LARGURA_JANELA, 0, 0)

    # configura janela para funcionar somente com setas do teclado
    window.keypad(1)

    # Ouvir apenas janela - para nao ficar escrevendo no terminal
    curses.noecho()

    # inicia cursor
    curses.curs_set(0)

    # janela sem borda
    window.border(0)

    # janela nao espera por acao do usuario
    # se nao houver acao retorna -1
    window.nodelay(1)

    return window


def atualizaJanela(janela, cobra, pontos):
    # Mostra pontuacao na tela
    janela.addstr(0, 2, "Pontos " + str(pontos) + " ")

    # Toda vez que aumenta a cobra, aumenta a velocidade
    janela.timeout(150-len(cobra) // 5 + len(cobra) // 10 %
                   120)


def novaFruta(janela, cobra):

    fruta = ()

    # enquanto nao criarmos uma fruta que nao esteja na mesma
    # posicao da cobra, ficamos tentando
    while fruta == ():

        # criar fruta em posicao aleatoria
        # tira valores das bordas para evitar problema
        fruta = (randint(1, constant.ALTURA_JANELA-2),
                 randint(1, constant.LARGURA_JANELA-2))

        if fruta in cobra:
            fruta = ()

    janela.addch(fruta[0], fruta[1], constant.APPLE)

    return fruta


def validaDirecao(janela, direcao):
    # salva ultima direcao
    direcao_anterior = direcao

    # le do teclado nova direcao
    nova_direcao = janela.getch()

    # se usuario mudou a direcao
    # usuario apertou alguma tecla
    if (nova_direcao != -1):
        direcao = nova_direcao
    else:
        direcao = direcao_anterior

    # se o usuario nao apertou uma seta ou a tecla ESC
    # usamos a direcao anterior
    if direcao not in [constant.DIREITA, constant.ESQUERDA, constant.BAIXO,
                       constant.CIMA, constant.ESC]:
        direcao = direcao_anterior

    return direcao


def proximoPasso(direcao, posicao, aumenta, diminui):

    if direcao == aumenta:
        posicao += 1

    if direcao == diminui:
        posicao -= 1

    return posicao


def bateuNasBordas(x, y):

    if (y == 0) or (y == constant.ALTURA_JANELA - 1):
        return True  # bateu na parede em cima ou embaixo - acabou o jogo
    if (x == 0) or (x == constant.LARGURA_JANELA - 1):
        return True  # bateu na parede na esquerda ou direita -acabou o jogo

    return False


def cobraSeMordeu(cobra):

    # se a nova posicao da cobra já existe na lista
    # é porque ela se mordeu
    if cobra[0] in cobra[1:]:
        return True

    return False



def daProximoPasso(janela,cobra,fruta, pontos):
    # Se achou a fruta,, come a fruta
    if cobra[0] == fruta:
        pontos += 1

        # se comeu a fruta, precisamos de uma nova fruta
        fruta = novaFruta(janela, cobra)

    # se nao achou a fruta, só anda
    else:
        # remove o rabo da lista
        rabo = cobra.pop()

        # remove o rabo da tela
        janela.addch(rabo[0], rabo[1], " ")

    # Adiciona nova cabeça na tela
    janela.addch(cobra[0][0], cobra[0][1], constant.SNAKE)

    return cobra, fruta, pontos