#!/usr/bin/env python3
import socket

HOST = '127.0.0.1' # IP del server
PORT = 5000      # port 

# instancia socket - protocolos internet / TCP 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# asocia el socket server con un host y puerto 
s.bind((HOST, PORT))

# empieza a escuchar 
s.listen()

# queda bloqueado hasta que recibe conexión - 
# devuelve un socket (cliente) para comunicarse
# y la dirección y puerto del cliente (en IPv6 tiene dos elementos más) 
conn, addr = s.accept()


print('Conectado con ', addr)
while True:
    # bloquea hasta recibir datos - máx 1024 bytes x vez
    data = conn.recv(1024)
    print(data)
    if not data: # si recibe b’’ cliente cortó conexión
        break

    # devuelve todos los bytes en data
    conn.sendall(data)

conn.close()
s.close()
