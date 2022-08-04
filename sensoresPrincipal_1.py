import time
from multa import velocidade_multa

tempo_sensor_velocidade_1_A = 0
tempo_sensor_velocidade_1_B = 0

sensor_velocidade_1_A_pressionado = 0
sensor_velocidade_1_B_pressionado = 0

############## TEMPO_SENSOR_VELOCIDADE_1 ##############

def calcula_velocidade_1(a, b):
    global tempo_sensor_velocidade_1_A
    global tempo_sensor_velocidade_1_B
    if a > 0 and b == 0:
        tempo_sensor_velocidade_1_A = a
        velocidade = 3.6/(tempo_sensor_velocidade_1_A - tempo_sensor_velocidade_1_B)
        # print("passou a ", velocidade, "km/h")
        velocidade_multa(velocidade)
        tempo_sensor_velocidade_1_A = 0
        tempo_sensor_velocidade_1_B = 0
    elif a == 0 and b > 0:
        tempo_sensor_velocidade_1_B = b



############## SENSOR_VELOCIDADE_1_A ##############

def verifica_sensor_velocidade_1_A(acionou):
    global sensor_velocidade_1_A_pressionado
    if acionou == 1:
        sensor_velocidade_1_A_pressionado = 1
    elif acionou == 9:
        aux = sensor_velocidade_1_A_pressionado
        sensor_velocidade_1_A_pressionado = 0
        # print(aux)
        return aux
    return sensor_velocidade_1_A_pressionado

def sensor_velocidade_1_A_acionado(GPIO_pin):
    tempo = time.perf_counter()

    calcula_velocidade_1(tempo, 0)
    verifica_sensor_velocidade_1_A(1)
    # print("Você ativou o YY - sensor velocidade 1 A - YY do pino %d" % GPIO_pin)

############## SENSOR_VELOCIDADE_1_B ##############

def verifica_sensor_velocidade_1_B(acionou):
    global sensor_velocidade_1_B_pressionado
    if acionou == 1:
        sensor_velocidade_1_B_pressionado = 1
    # elif acionou == 0:
    #     sensor_velocidade_1_B_pressionado = 0
    return sensor_velocidade_1_B_pressionado

def sensor_velocidade_1_B_acionado(GPIO_pin):
    tempo = time.perf_counter()

    calcula_velocidade_1(0, tempo)
    verifica_sensor_velocidade_1_B(1)
    # print("Você ativou o YY - sensor velocidade 2 B - YY do pino %d" % GPIO_pin)

