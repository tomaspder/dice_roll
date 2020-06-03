import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print("Juego de dados aleatorios. Quien obtenga un dado mayor gana la ronda. El mejor de 10 rondas es el ganador final.")
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    keypressed = input('Presione enter para tirar un dado: ')
    ClientSocket.send(str.encode(keypressed))
    Response = ClientSocket.recv(1024)
    print(Response.decode())
ClientSocket.close()
