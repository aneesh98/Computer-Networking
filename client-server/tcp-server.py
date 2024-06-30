from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(2)
print(f"[LOCAL-SERVER]: BOUND PORT {serverPort}. Server ready to receive")
while True:
    connection_socket, addr = serverSocket.accept()
    print(f"[LOCAL-SERVER]: Connection Accepted with Address: {addr[0]} and port: {str(addr[1])}")
    file_name = connection_socket.recv(1024).decode()
    with open(file_name, 'r') as f:
        contents = f.read()
    connection_socket.send(contents.encode())
