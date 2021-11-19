import respostas
from time1 import cobraSeMordeu, validaDirecao
from time2 import proximoPasso, bateuNasBordas
from time3 import novaFruta, daProximoPasso
import curses
import constant
from random import randint



def main():

    janela = respostas.novaJanela()

    # Definicoes iniciais (onde tudo comeca)
    pontos = 0
    cobra = constant.COBRA
    direcao = constant.DIREITA  # sempre comeca andando para direita

    fruta = novaFruta(janela, cobra)

    while direcao != constant.ESC:  # continua o jogo enquanto o usuario nao
                                    # apertar ESC

        ##########ATUALIZA JANELA##########

        # se necessario atualiza pontuacao e velocidade da cobra
        respostas.atualizaJanela(janela, cobra, pontos)

        ##########VALIDA A DIRECAO##########

        direcao = validaDirecao(janela, direcao)

        ##########CALCULA O PROXIMO PASSO##########

        y = proximoPasso(direcao, cobra[0][0], constant.BAIXO, constant.CIMA)
        x = proximoPasso(direcao, cobra[0][1],
                         constant.DIREITA, constant.ESQUERDA)

        # Nova cabeca da cobra é a posicao calculada
        cobra.insert(0, (y, x))

        ##########VERIFICA SE NAO BATEMOS##########

        # Testar se nao batemos na borda da janela
        if bateuNasBordas(x, y):
            break

        # Testar se nao mordemos a propria cobra
        if cobraSeMordeu(cobra):
            break

        ##########DA O PROXIMO PASSO##########

        # IMPLEMENTAR O PROXIMO PASSO
        # SE O PROXIMO PASSO É VALIDO, QUAIS SAO NOSSAS POSSIBILIDADES ?
        cobra, fruta, pontos = daProximoPasso(janela,cobra,fruta, pontos)


    ##########ACABOU O JOGO##########

    # Fecha a janela
    curses.endwin()

    # Imprime pontos no terminal
    print(f"Pontuação final: {pontos}")
    print("Obrigado por jogar")


if __name__ == "__main__":
    main()
