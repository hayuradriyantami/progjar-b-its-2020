import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
nama = input("Masukkan nama file : ")
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    # Send data
    message = nama
    print(f"sending {message}")
    sock.sendall(message.encode())
    while True:
        data = sock.recv(2048)
        file = open("copy" + message, 'a+b')
        if not data:
            file.close()
            break
        file.write(data)
finally:
    print("closing")
    sock.close()
