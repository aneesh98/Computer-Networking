from socket import *
import threading

def handle_client(connection_socket):
    try:
        connection_socket.settimeout(30)  # Set a timeout for inactivity
        while True:
            try:
                file_name = connection_socket.recv(1024).decode()
                if not file_name:
                    break
                with open(file_name, 'r') as f:
                    contents = f.read()
                connection_socket.send(contents.encode())
            except timeout:
                print("[LOCAL-SERVER]: Connection timed out.")
                break
    except Exception as e:
        print(f"[LOCAL-SERVER]: Error handling client: {e}")
    finally:
        connection_socket.close()
        print("[LOCAL-SERVER]: Connection closed.")

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)  # Listen for up to 5 connections

print(f"[LOCAL-SERVER]: BOUND PORT {serverPort}. Server ready to receive")

while True:
    connection_socket, addr = serverSocket.accept()
    print(f"[LOCAL-SERVER]: Connection Accepted with Address: {addr[0]} and port: {str(addr[1])}")
    client_thread = threading.Thread(target=handle_client, args=(connection_socket,))
    client_thread.start()
