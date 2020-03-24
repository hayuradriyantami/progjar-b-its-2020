import socket
import sys
from time import sleep
import base64
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
port = 1803
server_address = ("localhost", port)
print("Connecting to localhost with port:", port, "....")
sock.connect(server_address)

message = (b"list")
sock.send(message)
print("Request sent")

data = sock.recv(2048)
print("List file: \n"+data.decode())
sock.close()