import socket
from token import NEWLINE

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 8820))

while True:
    msg = str(input("enter message\n"))
    my_socket.send(msg.encode())
    data = my_socket.recv(1024).decode()
    print("The server sent " + data + "\n")
    if data == "BYE":
        print("exiting...")
        break

my_socket.close()