from random import randint, random
import respostas
import constant

# retorna nova posicao x,y da nova fruta
def novaFruta(janela, cobra):
    # IMPLEMENTAR FUNCAO QUE CRIA NOVA FRUTA E IMPRIME NA TELA
    fruta = ()

    while fruta == ():
        # criar uma posicao aleatoria
        x = randint(1, constant.ALTURA_JANELA-2)
        y = randint(1, constant.LARGURA_JANELA-2)

        fruta = (x, y)

        # verificar se a fruta nao esta em cima da cobra
        if fruta in cobra:
            fruta = ()

    janela.addch(fruta[0], fruta[1], constant.APPLE)

    return fruta


# retorna cobra atualizada, posicao da nova fruta
# se necessario e pontos atualizados
# atualiza posicao da cobra e fruta na tela se necessario
def daProximoPasso(janela, cobra, fruta, pontos):

    # IMPLEMENTAR FUNCAO QUE DA PROXIMO PASSO
    if cobra[0] == fruta:
        # adicionar na tela mais um pedaco da cobra (cabeca)
        janela.addch(cobra[0][0], cobra[0][1], constant.SNAKE)

        # adicionar outra fruta
        fruta = novaFruta(janela, cobra)

        # adicionar um ponto
        pontos = pontos + 1
    else:
        # adiciona na tela mais um pedaco da cobra (cabeca)
        janela.addch(cobra[0][0], cobra[0][1], constant.SNAKE)

        # tira ultimo elemento da lista
        rabo = cobra.pop()

        # remove da tela o rabo da cobra
        janela.addch(rabo[0], rabo[1], " ")

    return cobra, fruta, pontos