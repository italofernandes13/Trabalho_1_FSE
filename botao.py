botao_pedestre_1_pressionado = 0
botao_pedestre_2_pressionado = 0

############## BOTAO_PEDESTRE_1 ##############

def verifica_botao_pedestre_1(acionou):
    global botao_pedestre_1_pressionado
    if acionou == 1:
        botao_pedestre_1_pressionado = 1
    elif acionou == 0:
        botao_pedestre_1_pressionado = 0
    return botao_pedestre_1_pressionado

def botao_pedestre_1_acionado(GPIO_pin):
    # print ("Você pressionou o YY - botão pedestre 1 - YY do pino %d e agora ele sera desativado" % GPIO_pin)
    verifica_botao_pedestre_1(1)


############## BOTAO_PEDESTRE_2 ##############

def verifica_botao_pedestre_2(acionou):
    global botao_pedestre_2_pressionado
    if acionou == 1:
        botao_pedestre_2_pressionado = 1
    elif acionou == 0:
        botao_pedestre_2_pressionado = 0
    return botao_pedestre_2_pressionado

def botao_pedestre_2_acionado(GPIO_pin):
    # print ("Você pressionou o XX - botão pedestre 2 - XX do pino %d e agora ele sera desativado" % GPIO_pin)
    verifica_botao_pedestre_2(1)