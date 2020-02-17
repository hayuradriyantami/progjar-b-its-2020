import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    # Send data
    file = open("rumput.jpg",'rb')
    read = file.read()
    print (f"sending {read}")
    sock.sendall(read)

finally:
    print ('closing socket')
    sock.close()
