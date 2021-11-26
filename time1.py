import respostas
import constant

def cobraSeMordeu(cobra):
    # IMPLEMENTAR FUNCAO QUE VERIFICA SE A COBRA SE MORDEU

    # se a coordenada da cabeca repetiu, quer dizer que a cobra ta batendo nela mesma

    # SE <valor> esta em <LISTA>:
       # faz alguma coisa se for verdade

    # cobra[0] = cabeca
    # cobra[1:] = corpo

    if cobra[0] in cobra[1:]:
    	return True
    else:
    	return False

    #return respostas.cobraSeMordeu(cobra)
    


def validaDirecao(janela, direcao):


	# pega a tecla que o usuario digitou
	nova_direcao = janela.getch()


	# pra cada direcao, verificar a naoova direcao, e se for a direcao contraria a da cobra, nao faz nada

	if (direcao == constant.DIREITA) or (direcao == constant.ESQUERDA):
		# lista com todas as direcoes possiveis nesse momento
		lista_possiveis = [constant.CIMA, constant.BAIXO, constant.ESC]

		if nova_direcao in lista_possiveis: # se a nova direcao esta dentro da lista de possiveis direcoes
			return nova_direcao # retorna a nova direcao
		else: # se nao
			return direcao # retorna a direcao que ja estava


	if (direcao == constant.CIMA) or (direcao == constant.BAIXO):
		lista_possiveis = [constant.DIREITA, constant.ESQUERDA, constant.ESC]

		if nova_direcao in lista_possiveis:
			return nova_direcao
		else:
			return direcao