import socket
import threading

SERVER_ADDRESS = ('127.0.0.1', 12345)
BUFFER_SIZE = 1024

def handle_client(client_socket, client_address):
    try:
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        
        # Receive data from the client
        data = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        print(f"Received data from {client_address[0]}:{client_address[1]}: {data}")

        # Modify the data
        response = f"Modified: {data.upper()}"

        # Send the modified data back to the client
        client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(5)
    print("Server listening on", SERVER_ADDRESS)

    while True:
        client_socket, client_address = server_socket.accept()
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
