import socket 
import threading

HEADER = 128
PORT = 10211
SERVER = "192.168.1.129"            ## 43
# SERVER = "192.168.1.146"            ## 44
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
cruzamentos = []
count_cruzamentos = 0

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket()
server.bind(ADDR)

def noturno(n):
    global cruzamentos
    global count_cruzamentos
    for i in range(count_cruzamentos):
        cruzamentos[i].sendall(f"{n}".encode(FORMAT))

def emergencia_1(n):
    global cruzamentos
    global count_cruzamentos
    for i in range(count_cruzamentos):
        cruzamentos[i].sendall(f"{n}".encode(FORMAT))
        if i == 1:
            break

def emergencia_2(n):
    global cruzamentos
    global count_cruzamentos
    for i in range(count_cruzamentos):
        if i == 0 or i == 1:
            pass
        else:
            cruzamentos[i].sendall(f"{n}".encode(FORMAT))

def send_handle_client(conn, addr):
    while True:
        entrada = input()
        if entrada == '0' or entrada == '1':
            noturno(entrada)
        elif entrada == '2' or entrada == '3':
            emergencia_1(entrada)
        elif entrada == '4' or entrada == '5':
            emergencia_2(entrada)


def handle_client(conn, addr):
    # print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"{msg}")
            # print(f"[{addr}] {msg}")
            # conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen(5)
    # print(f"[LISTENING] Server is listening on {SERVER} port: {PORT}")
    global cruzamentos
    global count_cruzamentos
    while True:
        conn, addr = server.accept()
        count_cruzamentos += 1
        cruzamentos.append(conn)
        thread_send = threading.Thread(target=handle_client, args=(conn, addr))
        thread_send.start()
        thread_recv = threading.Thread(target=send_handle_client, args=(conn, addr))
        thread_recv.start()
        # print(f"[ACTIVE CONNECTIONS] {threading.activeCount - 1}")


# print("[STARTING] server is starting...")
print('Digite 0 para ligar modo noturno\nDigite 1 para desligar modo noturno\nDigite 2 para ligar modo emergencia cruzamento 1 e 2\nDigite 3 para desligar modo emergencia cruzamento 1 e 2\nDigite 4 para ligar modo emergencia cruzamento 3 e 4\nDigite 5 para desligar modo emergencia cruzamento 3 e 4: ')
        
start()