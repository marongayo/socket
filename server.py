import socket
import threading

SERVER_ADDRESS = ('192.168.0.111', 12345)
BUFFER_SIZE = 1024

def handle_client(client_socket, client_address):
    try:
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        
        data = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        print(f"Received data from {client_address[0]}:{client_address[1]}: {data}")
        condition_result = check_condition(data)
        
        response = str(condition_result)
        client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def check_condition(data):
    # Implement your condition checking logic here
    # For example, check if data contains a specific value
    return True if "specific_value" in data else False

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
