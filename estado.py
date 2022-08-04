import RPi.GPIO as GPIO
from time import sleep
from botao import verifica_botao_pedestre_1, verifica_botao_pedestre_2
from sensoresAuxiliar import verifica_sensor_passagem_1, verifica_sensor_passagem_2
from multa import semafaro_fechado
from estadoLED import estado_1_comp, estado_2_comp, estado_3_comp, estado_4_comp, estado_5_comp, estado_noturno_1_comp, estado_noturno_2_comp
from sensoresPrincipal_1 import verifica_sensor_velocidade_1_A
from sensoresPrincipal_2 import verifica_sensor_velocidade_2_A

modo_noturno = False
modo_emergencia = False
# sensor_passagem_1_pressionado
# sensor_passagem_2_pressionado
# sensor_principal_1_pressionado
# sensor_principal_2_pressionado

sensores = [0, 0, 0, 0]
multa = [0, 0, 0, 0]

def sensores_0():
        global sensores
        global multa
        sensores = [0, 0]
        multa = [0, 0]


def sensores_inicio():
        global sensores
        sensores[0] = verifica_sensor_passagem_1(9)
        sensores[1] = verifica_sensor_passagem_2(9)

def sensores_fim():
        global multa
        multa[0] = sensores[0]
        multa[1] = sensores[1]

def noturno_liga():
        global modo_noturno
        modo_noturno = True
def noturno_desliga():
        global modo_noturno
        modo_noturno = False

def emergencia_liga():
        global modo_emergencia
        modo_emergencia = True
def emergencia_desliga():
        global modo_emergencia
        modo_emergencia = False

def estado_1(x, semaforo_principal, semaforo_auxiliar):
        global modo_noturno
        global modo_emergencia
        global sensores
        global multa
        count = 0
        verifica_sensor_velocidade_1_A(9)
        verifica_sensor_velocidade_2_A(9)

        # print("Todos vermelho ", x)
        while count < 10:
                
                if modo_emergencia:
                        estado_emergencia(x, semaforo_principal, semaforo_auxiliar)
                        break
                elif modo_noturno:
                        estado_noturno_1(x, semaforo_principal, semaforo_auxiliar)
                        break

                if verifica_sensor_velocidade_1_A(9) == 1:
                        # print('multado')
                        semafaro_fechado()
                if verifica_sensor_velocidade_2_A(9) == 1:
                        # print('multado')
                        semafaro_fechado()

                sensores_inicio()
                for i in range (2):
                        if (multa[i] == 1 and sensores[i] == 0):
                                # print('multado')
                                semafaro_fechado()

                estado_1_comp(semaforo_principal, semaforo_auxiliar)
                sleep(0.1)
                count += 1
                sensores_fim()

def estado_2(x, semaforo_principal, semaforo_auxiliar):
        global modo_noturno
        global modo_emergencia
        global sensores
        global multa
        count = 0
        botao_pedestre_2_pressionado = verifica_botao_pedestre_2(0) 

        # print("Principal verde ", x)
        while (count < 100 and not(count >= 50 and (botao_pedestre_2_pressionado == 1 or sensores[0] == 1 or sensores[1] == 1))):
                
                if modo_emergencia:
                        estado_emergencia(x, semaforo_principal, semaforo_auxiliar)
                        break
                elif modo_noturno:
                        estado_noturno_1(x, semaforo_principal, semaforo_auxiliar)
                        break
                
                sensores_inicio()
                for i in range (2):
                        if (multa[i] == 1 and sensores[i] == 0):
                                # print('multado')
                                semafaro_fechado()

                estado_2_comp(semaforo_principal, semaforo_auxiliar)
                sleep(0.2)
                count += 1
                sensores_fim()
                # print(count , botao_pedestre_2_pressionado, sensor_passagem_1_pressionado, sensor_passagem_2_pressionado)

def estado_3(x, semaforo_principal, semaforo_auxiliar):
        global modo_noturno
        global modo_emergencia
        global sensores
        global multa
        count = 0

        # print("Principal amarelo ", x)
        while count < 30:
                
                if modo_emergencia:
                        estado_emergencia(x, semaforo_principal, semaforo_auxiliar)
                        break
                elif modo_noturno:
                        estado_noturno_1(x, semaforo_principal, semaforo_auxiliar)
                        break
                
                sensores_inicio()
                for i in range (2):
                        if (multa[i] == 1 and sensores[i] == 0):
                                # print('multado')
                                semafaro_fechado()

                estado_3_comp(semaforo_principal, semaforo_auxiliar)
                sleep(0.1)
                count += 1
                sensores_fim()

def estado_4(x, semaforo_principal, semaforo_auxiliar):
        global modo_noturno
        global modo_emergencia
        count = 0
        botao_pedestre_1_pressionado = verifica_botao_pedestre_1(0)
        verifica_sensor_velocidade_1_A(9)
        verifica_sensor_velocidade_2_A(9)

        # print("Auxiliar verde ", x)
        while (count < 50 and not (count >= 25 and botao_pedestre_1_pressionado == 1)):
                
                if modo_emergencia:
                        estado_emergencia(x, semaforo_principal, semaforo_auxiliar)
                        break
                elif modo_noturno:
                        estado_noturno_1(x, semaforo_principal, semaforo_auxiliar)
                        break

                if verifica_sensor_velocidade_1_A(9) == 1:
                        # print('multado')
                        semafaro_fechado()
                if verifica_sensor_velocidade_2_A(9) == 1:
                        # print('multado')
                        semafaro_fechado()

                botao_pedestre_1_pressionado = verifica_botao_pedestre_1(9)

                estado_4_comp(semaforo_principal, semaforo_auxiliar)
                sleep(0.2)
                count += 1
                # print(count , botao_pedestre_1_pressionado)

def estado_5(x, semaforo_principal, semaforo_auxiliar):
        global modo_noturno
        global modo_emergencia
        global sensores
        global multa
        count = 0
        verifica_sensor_velocidade_1_A(9)
        verifica_sensor_velocidade_2_A(9)
        
        # print("Auxiliar amarelo ", x)
        while count < 30:
                
                if modo_emergencia:
                        estado_emergencia(x, semaforo_principal, semaforo_auxiliar)
                        break
                elif modo_noturno:
                        estado_noturno_1(x, semaforo_principal, semaforo_auxiliar)
                        break

                if verifica_sensor_velocidade_1_A(9) == 1:
                        # print('multado')
                        semafaro_fechado()
                if verifica_sensor_velocidade_2_A(9) == 1:
                        # print('multado')
                        semafaro_fechado()

                sensores_inicio()
                for i in range (2):
                        if (multa[i] == 1 and sensores[i] == 0):
                                # print('multado')
                                semafaro_fechado()

                estado_5_comp(semaforo_principal, semaforo_auxiliar)
                sleep(0.1)
                count += 1
                sensores_fim()

def estado_noturno_1(x, semaforo_principal, semaforo_auxiliar):
        global modo_noturno
        global modo_emergencia
        count = 0
        # print("Todos amarelo")
        while count<10:
                if not modo_noturno:
                        count = 0
                        estado_1(x, semaforo_principal, semaforo_auxiliar)
                        break

                estado_noturno_1_comp(semaforo_principal, semaforo_auxiliar)
                sleep(0.1)
                count += 1
        if count == 10:
                estado_noturno_2(x, semaforo_principal, semaforo_auxiliar)

def estado_noturno_2(x, semaforo_principal, semaforo_auxiliar):
        global modo_noturno
        global modo_emergencia
        count = 0
        # print("Todos apagados")
        while count<10:
                if not modo_noturno:
                        count = 0
                        estado_1(x, semaforo_principal, semaforo_auxiliar)
                        break

                estado_noturno_2_comp(semaforo_principal, semaforo_auxiliar)
                sleep(0.1)
                count += 1
        if count == 10:
                estado_noturno_1(x, semaforo_principal, semaforo_auxiliar)

def estado_emergencia(x, semaforo_principal, semaforo_auxiliar):
        estado_2_comp(semaforo_principal, semaforo_auxiliar)
        while True:
                if not modo_emergencia:
                        estado_1(x, semaforo_principal, semaforo_auxiliar)
                        break