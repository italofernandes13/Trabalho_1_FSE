import RPi.GPIO as GPIO


def estado_1_comp(semaforo_principal, semaforo_auxiliar):
    GPIO.output(semaforo_principal, GPIO.LOW)
    GPIO.output(semaforo_auxiliar, GPIO.LOW)
    GPIO.output(semaforo_principal[2], GPIO.HIGH)
    GPIO.output(semaforo_auxiliar[2], GPIO.HIGH)


def estado_2_comp(semaforo_principal, semaforo_auxiliar):
    GPIO.output(semaforo_principal, GPIO.LOW)
    GPIO.output(semaforo_auxiliar, GPIO.LOW)
    GPIO.output(semaforo_principal[0], GPIO.HIGH)
    GPIO.output(semaforo_auxiliar[2], GPIO.HIGH)


def estado_3_comp(semaforo_principal, semaforo_auxiliar):
    GPIO.output(semaforo_principal, GPIO.LOW)
    GPIO.output(semaforo_auxiliar, GPIO.LOW)
    GPIO.output(semaforo_principal[1], GPIO.HIGH)
    GPIO.output(semaforo_auxiliar[2], GPIO.HIGH)


def estado_4_comp(semaforo_principal, semaforo_auxiliar):
    GPIO.output(semaforo_principal, GPIO.LOW)
    GPIO.output(semaforo_auxiliar, GPIO.LOW)
    GPIO.output(semaforo_principal[2], GPIO.HIGH)
    GPIO.output(semaforo_auxiliar[0], GPIO.HIGH)


def estado_5_comp(semaforo_principal, semaforo_auxiliar):
    GPIO.output(semaforo_principal, GPIO.LOW)
    GPIO.output(semaforo_auxiliar, GPIO.LOW)
    GPIO.output(semaforo_principal[2], GPIO.HIGH)
    GPIO.output(semaforo_auxiliar[1], GPIO.HIGH)

    
def estado_noturno_1_comp(semaforo_principal, semaforo_auxiliar):
    GPIO.output(semaforo_principal, GPIO.LOW)
    GPIO.output(semaforo_auxiliar, GPIO.LOW)
    GPIO.output(semaforo_principal[1], GPIO.HIGH)
    GPIO.output(semaforo_auxiliar[1], GPIO.HIGH)
    

def estado_noturno_2_comp(semaforo_principal, semaforo_auxiliar):
    GPIO.output(semaforo_principal, GPIO.LOW)
    GPIO.output(semaforo_auxiliar, GPIO.LOW)