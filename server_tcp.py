import socket
import  time
from datetime import datetime
import random


server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820 ))
server_socket.listen()
print("Server is up and running")
(client_socket, client_address) = server_socket.accept()
print("Client connected")

while True:
    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)
    if data == "QUIT":
        data = "BYE"
        client_socket.send(data.encode())
        break
    elif data == "TIME":
       data = str(datetime.now())
    elif data == "RANDOM":
        data = str(random.randint(1, 10))
    else:
        data = data.upper() + "!!!"
    client_socket.send(data.encode())




client_socket.close()
server_socket.close()