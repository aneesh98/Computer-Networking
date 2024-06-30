from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Enter the file whose contents you want: ")
clientSocket.send(sentence.encode())
content = clientSocket.recv(1024)
print("Received from server: ", content.decode())
sentence = input("Enter the file whose contents you want: ")
clientSocket.send(sentence.encode())
content = clientSocket.recv(1024)
print("Received from server: ", content.decode())
clientSocket.close()