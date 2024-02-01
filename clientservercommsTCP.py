import socket
from time import sleep

def run_client():
    client_socket = sockect.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9987))
    client_socket.send('hello'.encode())
    data = client_socket.recv(1024)
    print(data.decode())
    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 9985))
    server_socket.listen(10)

    while True:
        connection, address = server_socket.accept()
        try:
            data = connection.recv(1024).decode()
            if len(data) > 0:
                print("Received: " + data)
        except ConnectionResetError:
            print("Client closed the connection.")
        finally:
            connection.close()
            break  # Assuming only one connection is handled

   server_socket.close()

if __name__ == "__main__":
    run_client()
    sleep(0.05)  # Added for demonstration; adjust as needed
    run_server()
