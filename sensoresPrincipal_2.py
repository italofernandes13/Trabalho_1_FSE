import time
from multa import velocidade_multa

tempo_sensor_velocidade_2_A = 0
tempo_sensor_velocidade_2_B = 0

sensor_velocidade_2_A_pressionado = 0
sensor_velocidade_2_B_pressionado = 0

############## TEMPO_SENSOR_VELOCIDADE_2 ##############

def calcula_velocidade_2(a, b):
    global tempo_sensor_velocidade_2_A
    global tempo_sensor_velocidade_2_B
    if a > 0 and b == 0:
        tempo_sensor_velocidade_2_A = a
        velocidade = 3.6/(tempo_sensor_velocidade_2_A - tempo_sensor_velocidade_2_B)
        # print("passou a ", velocidade, "km/h")
        velocidade_multa(velocidade)
        tempo_sensor_velocidade_2_A = 0
        tempo_sensor_velocidade_2_B = 0
    elif a == 0 and b > 0:
        tempo_sensor_velocidade_2_B = b


############## SENSOR_VELOCIDADE_2_A ##############

def verifica_sensor_velocidade_2_A(acionou):
    global sensor_velocidade_2_A_pressionado
    if acionou == 1:
        sensor_velocidade_2_A_pressionado = 1
    elif acionou == 9:
        aux = sensor_velocidade_2_A_pressionado
        sensor_velocidade_2_A_pressionado = 0
        return aux
    return sensor_velocidade_2_A_pressionado

def sensor_velocidade_2_A_acionado(GPIO_pin):
    tempo = time.perf_counter()
    
    calcula_velocidade_2(tempo, 0)
    verifica_sensor_velocidade_2_A(1)
    # print("Você ativou o YY - sensor velocidade 2 A - YY do pino %d" % GPIO_pin)
    verifica_sensor_velocidade_2_A(0)

############## SENSOR_VELOCIDADE_2_B ##############

def verifica_sensor_velocidade_2_B(acionou):
    global sensor_velocidade_2_B_pressionado
    if acionou == 1:
        sensor_velocidade_2_B_pressionado = 1
    # elif acionou == 0:
    #     sensor_velocidade_2_B_pressionado = 0
    return sensor_velocidade_2_B_pressionado

def sensor_velocidade_2_B_acionado(GPIO_pin):
    tempo = time.perf_counter()
    
    calcula_velocidade_2(0, tempo)
    verifica_sensor_velocidade_2_B(1)
    # print("Você ativou o YY - sensor velocidade 2 B - YY do pino %d" % GPIO_pin)



# ############## SENSOR_VELOCIDADE_2_A ##############

# def verifica_sensor_velocidade_2_A(acionou):
#     global sensor_velocidade_2_A_pressionado
#     if acionou == 1:
#         sensor_velocidade_2_A_pressionado = 0
#     # elif acionou == 0:
#     #     sensor_velocidade_2_A_pressionado = 0
#     return sensor_velocidade_2_A_pressionado

# def sensor_velocidade_2_A_acionado(GPIO_pin):
#     tempo = time.perf_counter()
    
#     aux = verifica_sensor_velocidade_2_A(9)

#     if aux == 0:
#         calcula_velocidade_2(tempo, 0)

#         # print ("Você ativou o YY - sensor velocidade 2 A - YY do pino %d" % GPIO_pin)
#         verifica_sensor_velocidade_2_A(1)
#     # elif aux[1] == 1:
#     #     # print ("Você desativou o YY - sensor velocidade 2 A - YY do pino %d" % GPIO_pin)
#     #     verifica_sensor_velocidade_2_A(0)

# ############## SENSOR_VELOCIDADE_2_B ##############

# def verifica_sensor_velocidade_2_B(acionou):
#     global sensor_velocidade_2_B_pressionado
#     if acionou == 1:
#         sensor_velocidade_2_B_pressionado = 0
#     # elif acionou == 0:
#     #     sensor_velocidade_2_B_pressionado = 0
#     return sensor_velocidade_2_B_pressionado

# def sensor_velocidade_2_B_acionado(GPIO_pin):
#     tempo = time.perf_counter()
    
#     aux = verifica_sensor_velocidade_2_B(9)

#     if aux == 0:
#         calcula_velocidade_2(0, tempo)

#         # print ("Você ativou o YY - sensor velocidade 2 B - YY do pino %d" % GPIO_pin)
#         verifica_sensor_velocidade_2_B(1)
#     # elif aux == 1:
#     #     # print ("Você desativou o YY - sensor velocidade 2 B - YY do pino %d" % GPIO_pin)
#     #     verifica_sensor_velocidade_2_B(0)
