import socket
import chatlib  # To use chatlib functions or consts, use chatlib

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678

# HELPER SOCKET METHODS
"""
    Builds a new message using chatlib, wanted code and message. 
    Prints debug info, then sends it to the given socket.
    Paramaters: conn (socket object), code (str), data (str)
    Returns: Nothing
"""
def build_and_send_message(conn, code, data):
    msg = chatlib.build_message(code, data)
    conn.send(msg.encode())


	
"""
    Recieves a new message from given socket,
    then parses the message using chatlib.
    Paramaters: conn (socket object)
    Returns: cmd (str) and data (str) of the received message. 
    If error occured, will return None, None
"""
def recv_message_and_parse(conn):
    data = conn.recv(1024).decode()
    parsed_data = chatlib.parse_message(data)
    if parsed_data[0] == 'ERROR':
        print(parsed_data[1])
    return parsed_data


def connect():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((SERVER_IP, SERVER_PORT))
    return my_socket


def error_and_exit(error_msg):
    print (error_msg)
    exit()


def login(conn):
    while True:
        username = input("Please enter username: \n")
        password = input("please enter password: \n")
        if username == "QUIT" and password == "QUIT":
            print("LOGIN FAILED \n")
            return
        msg = chatlib.join_data((username,password))
        build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"], msg)
        if recv_message_and_parse(conn)[0] != "ERROR":
            print("LOGIN SUCCESS")
            return
        print("LOGIN FAIL: PLEASE INSERT INFO AGAIN \n")

def logout(conn):
    build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["logout_msg"],"")

def main():
    conn = connect()
    login(conn)
    logout(conn)
    conn.close()

if __name__ == '__main__':
    main()
