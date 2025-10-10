def trocar_entrada():
	from monitorcontrol import get_monitors 	#pip install monitorcontrol

	with get_monitors()[0] as monitor: #Seleciona o monitor principal passando pra variavel "monitor"

		#VALORES ABAIXO É REFERENCIA AO MEU MONITOR ALIENWARE AW2725DM
		#NÚMERO 15 = DISPLAYPORT (PC)
		#NÚMERO 17 = HDMI 1
		#NÚMERO 18 = HDMI 2 (PS5)

		ENTRADA_ATUAL = monitor.get_input_source() #Pega a entrada atual do monitor passando pra variavel ENTRADA_ATUAL

		if ENTRADA_ATUAL == 15: #Checa se a entrada atual é o DISPLAYPORT
			monitor.set_input_source(18) #Altera para o HDMI 2

		if ENTRADA_ATUAL == 18: #Checa se a entrada atual é o HDMI 2
			monitor.set_input_source(15) #Altera para o DISPLAYPORT


def main():
	trocar_entrada()


if __name__ == '__main__':
	main()

