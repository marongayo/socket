import socket

SERVER_ADDRESS = ('192.168.0.111', 12345)
BUFFER_SIZE = 1024

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    client_ip = get_client_ip()
    
    # Send the client's IP address to the server
    client_socket.send(client_ip.encode('utf-8'))

    response = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    print("Received response from server:", response)

    client_socket.close()

def get_client_ip():
    return socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    start_client()
