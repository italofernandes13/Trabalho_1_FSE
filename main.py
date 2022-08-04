import RPi.GPIO as GPIO
import time
from threading import Thread
from estado import estado_1, estado_2, estado_3, estado_4, estado_5
from botao import botao_pedestre_2_acionado, botao_pedestre_1_acionado
from sensoresAuxiliar import sensor_passagem_1_acionado, sensor_passagem_2_acionado
from sensoresPrincipal_1 import sensor_velocidade_1_A_acionado, sensor_velocidade_1_B_acionado
from sensoresPrincipal_2 import sensor_velocidade_2_A_acionado, sensor_velocidade_2_B_acionado
from multa import qtd_infracao_avanco, qtd_infracao_velocidade, qtd_media_via, qtd_carro_min

""" Global """
botao_pedestre_1 = [8, 10]
botao_pedestre_2 = [7, 9]

semaforo_principal = [[20, 16, 12],[0, 5, 6]]
semaforo_auxiliar = [[1, 26, 21],[2, 3, 11]]

sensor_passagem_1 = [14, 4]
sensor_passagem_2 = [15, 17]

sensor_velocidade_1_A = [18, 27]
sensor_velocidade_1_B = [23, 22]

sensor_velocidade_2_A = [24, 19] #[24, 13]
sensor_velocidade_2_B = [25, 13] #[25, 19]


def configurando_cruzamento(y):
    """ Configurando GPIO """
    # Configurando o modo do GPIO como BCM
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 

    # leds
    GPIO.setup(semaforo_principal[y-1], GPIO.OUT)
    GPIO.setup(semaforo_auxiliar[y-1], GPIO.OUT)

    # botoes
    GPIO.setup(botao_pedestre_1[y-1], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(botao_pedestre_2[y-1], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    GPIO.add_event_detect(botao_pedestre_1[y-1], GPIO.RISING, callback=botao_pedestre_1_acionado, bouncetime = 300)
    GPIO.add_event_detect(botao_pedestre_2[y-1], GPIO.RISING, callback=botao_pedestre_2_acionado, bouncetime = 300)

    # sensores auxiliares
    GPIO.setup(sensor_passagem_1[y-1], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(sensor_passagem_2[y-1], GPIO.IN, pull_up_down = GPIO.PUD_UP)

    GPIO.add_event_detect(sensor_passagem_1[y-1], GPIO.BOTH, callback=sensor_passagem_1_acionado, bouncetime = 300)
    GPIO.add_event_detect(sensor_passagem_2[y-1], GPIO.BOTH, callback=sensor_passagem_2_acionado, bouncetime = 300)

    # sensores principais A
    GPIO.setup(sensor_velocidade_1_A[y-1], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(sensor_velocidade_1_B[y-1], GPIO.IN, pull_up_down = GPIO.PUD_UP)

    GPIO.add_event_detect(sensor_velocidade_1_A[y-1], GPIO.BOTH, callback=sensor_velocidade_1_A_acionado, bouncetime = 300)
    GPIO.add_event_detect(sensor_velocidade_1_B[y-1], GPIO.BOTH, callback=sensor_velocidade_1_B_acionado, bouncetime = 300)

    # sensores principais B
    GPIO.setup(sensor_velocidade_2_A[y-1], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(sensor_velocidade_2_B[y-1], GPIO.IN, pull_up_down = GPIO.PUD_UP)

    GPIO.add_event_detect(sensor_velocidade_2_A[y-1], GPIO.BOTH, callback=sensor_velocidade_2_A_acionado, bouncetime = 300)
    GPIO.add_event_detect(sensor_velocidade_2_B[y-1], GPIO.BOTH, callback=sensor_velocidade_2_B_acionado, bouncetime = 300)
 
 
def rotina(x): 
    tempo = time.perf_counter()
    # print(f"tempo inical {tempo}")
    configurando_cruzamento(x)
    while True:
        # print("==========")
        # print(f"Fluxo de trânsito nas via principal: {qtd_carro_min(tempo)}Carros/min")
        # print(f"Fluxo de trânsito nas via principal: {qtd_media_via()}km/h")
        # print(f"Número de infrações por avanço de sinal: {qtd_infracao_avanco()}")
        # print(f"Número de infrações por velocidade acima da permitida: {qtd_infracao_velocidade()}")
        # print("==========")
        ##### todos vermelho #####
        estado_1(x-1, semaforo_principal[x-1], semaforo_auxiliar[x-1])
        ##### principal verde #####
        estado_2(x-1, semaforo_principal[x-1], semaforo_auxiliar[x-1])
        ##### principal amarelo #####
        estado_3(x-1, semaforo_principal[x-1], semaforo_auxiliar[x-1])
        ##### todos vermelho #####
        estado_1(x-1, semaforo_principal[x-1], semaforo_auxiliar[x-1])        
        ##### auxiliar verde #####
        estado_4(x-1, semaforo_principal[x-1], semaforo_auxiliar[x-1])
        ##### auxiliar amarelo #####
        estado_5(x-1, semaforo_principal[x-1], semaforo_auxiliar[x-1])

# rotina(1)
# cruzamento_1 = Thread(target=rotina,args=[1])

def main(x):
    cruzamento_1 = Thread(target=rotina,args=[x])
    cruzamento_1.start()