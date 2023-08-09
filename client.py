import socket

SERVER_ADDRESS = ('192.168.0.111', 12345)
BUFFER_SIZE = 1024

def start_client(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    # Send the message to the server
    client_socket.send(message.encode('utf-8'))

    # Receive and print the response from the server
    response = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    print("Received response from server:", response)

    client_socket.close()

if __name__ == "__main__":
    message = input("Enter a message to send to the server: ")
    start_client(message)
