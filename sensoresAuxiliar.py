sensor_passagem_1_pressionado = 0
sensor_passagem_2_pressionado = 0

############### SENSOR_PASSAGEM_1 ##############

def verifica_sensor_passagem_1(acionou):
    global sensor_passagem_1_pressionado
    if acionou == 1:
        sensor_passagem_1_pressionado = 1
    elif acionou == 0:
        sensor_passagem_1_pressionado = 0
    return sensor_passagem_1_pressionado
 
def sensor_passagem_1_acionado(GPIO_pin):

    aux = verifica_sensor_passagem_1(9)

    if aux == 0:
        # print ("Você ativou o YY - sensor passagem 1 - YY do pino %d" % GPIO_pin)
        verifica_sensor_passagem_1(1)
    elif aux == 1:
        # print ("Você desativou o YY - sensor passagem 1 - YY do pino %d" % GPIO_pin)
        verifica_sensor_passagem_1(0)

############## SENSOR_PASSAGEM_2 ##############

def verifica_sensor_passagem_2(acionou):
    global sensor_passagem_2_pressionado
    if acionou == 1:
        sensor_passagem_2_pressionado = 1
    elif acionou == 0:
        sensor_passagem_2_pressionado = 0
    return sensor_passagem_2_pressionado

def sensor_passagem_2_acionado(GPIO_pin):

    aux = verifica_sensor_passagem_2(9)

    if aux == 0:
        # print ("Você ativou o YY - sensor passagem 2 - YY do pino %d" % GPIO_pin)
        verifica_sensor_passagem_2(1)
    elif aux == 1:
        # print ("Você desativou o YY - sensor passagem 2 - YY do pino %d" % GPIO_pin)
        verifica_sensor_passagem_2(0)
