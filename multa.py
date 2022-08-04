import time
import os

count_qtd_carro = 0
count_vel_acima = 0
media_velocidade = 0
count_avanco_sinal = 0

def velocidade_multa(vel):
    global count_qtd_carro
    global count_vel_acima
    global media_velocidade
    # print(f"Carro no Cruzamento {x+1} passou a {vel}km/h")
    if vel > 60:
        # print(f"Carro no Cruzamento {x+1} foi multado por passar a {vel}km/h")
        count_vel_acima += 1
        # os.system('omxplayer -o both example.mp3 &')
    count_qtd_carro += 1
    media_velocidade = (media_velocidade*(count_qtd_carro-1) + vel)/count_qtd_carro
    # print(f"qtd de carro {count_qtd_carro} velocidade media {media_velocidade} qtd carro acima {count_vel_acima}")

def semafaro_fechado():
    global count_avanco_sinal
    # print(f"Avancou o sinal fechado no Cruzamento {x+1}")
    # os.system('omxplayer -o both example.mp3 &')
    count_avanco_sinal += 1
    # print(f"avanco sinal {count_avanco_sinal}")



def qtd_carro_min(tempo_inicial):
    global count_qtd_carro
    tempo_final = time.perf_counter()
    # print(f"tempo final {tempo_final}")
    return count_qtd_carro*60/(tempo_final-tempo_inicial)

def qtd_infracao_avanco():
    global count_avanco_sinal
    return count_avanco_sinal

def qtd_infracao_velocidade():
    global count_vel_acima
    return count_vel_acima

def qtd_infracao_velocidade():
    global count_vel_acima
    return count_vel_acima

def qtd_media_via():
    global media_velocidade
    return media_velocidade