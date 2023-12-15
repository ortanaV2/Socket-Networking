import socket
import threading
import json

with open(r"./config.json", "r") as config_f:
    CONFIG = json.load(config_f)

def handle_client(client_socket, client_address):
    while True:
        data = client_socket.recv(1024)
        if not data: break
        decoded_message = data.decode('utf-8')
        print(f"{client_address} >>: {decoded_message}")

        try:
            response = CONFIG[str(decoded_message)]
        except KeyError:
            response = 404
        except Exception:
            response = 500
        print(f"Response: {response}")
        
        client_socket.send(str(response).encode('utf-8'))
    client_socket.close()

def start_server(port):
    host = '0.0.0.0'
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening --> {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted --> {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    port1 = 10883
    port2 = 10884
    server_thread1 = threading.Thread(target=start_server, args=(port1,))
    server_thread2 = threading.Thread(target=start_server, args=(port2,))

    server_thread1.start()
    server_thread2.start()
    server_thread1.join()
    server_thread2.join()
