import socket
import time
import sys
from multa import qtd_infracao_avanco, qtd_infracao_velocidade, qtd_media_via, qtd_carro_min
from main import main
from estado import noturno_liga, noturno_desliga, emergencia_liga, emergencia_desliga
import threading

HEADER = 128
PORT = 10211
SERVER = sys.argv[-1]
# SERVER = "192.168.1.129"            ## 43
# SERVER = "192.168.1.146"            ## 44
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket()
client.connect(ADDR)

def recive():    
    while True:
        
        msg = (client.recv(2048).decode(FORMAT))
        print(f"msg: {msg}")
        if msg == '0':
            noturno_liga()
        elif msg == '1':
            noturno_desliga()

        elif msg == '2' and (sys.argv[1] == '1' or sys.argv[1] == '2'):
            emergencia_liga()
        elif msg == '3' and (sys.argv[1] == '1' or sys.argv[1] == '2'):
            emergencia_desliga()

        elif msg == '4' and (sys.argv[1] == '3' or sys.argv[1] == '4'):
            emergencia_liga()
        elif msg == '5' and (sys.argv[1] == '3' or sys.argv[1] == '4'):
            emergencia_desliga()


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def informacoes():
    cruzamento = 0
    
    if sys.argv[1] == '1' or sys.argv[1] == '3':
        cruzamento = 1
        # print('entrou 1 ou 3', ADDR)
    elif sys.argv[1] == '2' or sys.argv[1] == '4':
        cruzamento = 2
        # print('entrou 2 ou 4', ADDR)

    msg = True
    tempo = time.perf_counter()
    main(cruzamento)
    while msg:
        if sys.argv[1] == '1':
            send("limpa")
        send("=============")
        send(f"CRUZAMENTO {sys.argv[1]}")
        send(f"Fluxo de trânsito nas via principal: {qtd_carro_min(tempo)}Carros/min")
        send(f"Fluxo de trânsito nas via principal: {qtd_media_via()}km/h")
        send(f"Número de infrações por avanço de sinal: {qtd_infracao_avanco()}")
        send(f"Número de infrações por velocidade acima da permitida: {qtd_infracao_velocidade()}")
        send("=============")
        time.sleep(3)

    

thread_send = threading.Thread(target=informacoes, args=())
thread_send.start()
thread_recv = threading.Thread(target=recive, args=())
thread_recv.start()
