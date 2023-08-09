import socket

def get_ip_address():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))  # Connect to a known external server
        local_ip = sock.getsockname()[0]  # Get the local IP address
        sock.close()
        return local_ip
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    ip_address = get_ip_address()
    if ip_address:
        print("Your computer's IP address:", ip_address)
    else:
        print("Unable to retrieve IP address.")
