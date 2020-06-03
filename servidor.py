import socket
from _thread import *
import random
jugadores = []
ServerSocket = socket.socket()
host = '127.0.0.1'

port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Esperando conexiones...')
ServerSocket.listen(5)

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

def threaded_client(connection,jugadores):
    connection.send(str.encode('Bievenido al servidor de Dice Roll\n'))
    while True:
        data = connection.recv(1024)
        print("{} responde: {}".format(connection.getpeername(),data.decode()))
        #reply = 'rta server: ' + data.decode('utf-8') + str(address[0]) + ":" + str(address[1])
        if not data:
            break
        for i in jugadores:
            conn_instance = i[0]
            index_player = i[1]
            if index_player == 1:
                player1_addr = conn_instance.getpeername()
                conn_instance.sendto(bytes("Jugador 1 - {}:{}\n".format(player1_addr[0],player1_addr[1]), "utf-8"), player1_addr)
            elif index_player == 2:
                player2_addr = conn_instance.getpeername()
                conn_instance.sendto(bytes("Jugador 2 - {}:{}\n".format(player2_addr[0],player2_addr[1]), "utf-8"), player2_addr)

    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Conexión con: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,jugadores))
    ThreadCount += 1
    jugadores.append((Client, ThreadCount))
    print('Cantidad de usuarios on: ' + str(ThreadCount))
ServerSocket.close()

