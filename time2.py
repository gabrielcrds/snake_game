import respostas
import constant

def proximoPasso(direcao, posicao, aumenta, diminui):

    # IMPLEMENTAR FUNCAO QUE CALCULA O PROXIMO PASSO DA COBRA
    if direcao == aumenta:
        return posicao + 1
    elif direcao == diminui:
        return posicao - 1

    return respostas.proximoPasso(direcao,posicao,aumenta,diminui)


def bateuNasBordas(x, y):

    # IMPLEMENTAR FUNCAO QUE VERIFICA SE BATEMOS NAS BORDAS
    if x == 0 or x == constant.LARGURA_JANELA-1:
        return True
    if y == 0 or y == constant.ALTURA_JANELA-1:
        return True
    return False

    return respostas.bateuNasBordas(x,y)
