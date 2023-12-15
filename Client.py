"""Example-Code for a client connecting and comunicating with the server"""

import socket

host = '192.123.4.567' #Servers IP-Address
port = 10883

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print(f"Connected to server --> {host}:{port}")

while True:
    message = input("Server request: ")
    if message == "$kill": break
    client_socket.send(message.encode('utf-8'))

    data = client_socket.recv(1024)    
    if not data:
        print("Status: 500")
        break
    else:
        print(f"Response: {data.decode('utf-8')}")
client_socket.close()
