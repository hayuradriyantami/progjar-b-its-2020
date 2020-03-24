import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
port = 1803
server_address = ("localhost", port)
print("Connecting to localhost with port:", port, "....")
sock.connect(server_address)

file_name = "lake.jpg"
message = (b"downloadfile "+file_name.encode())
print("Downloading " + file_name, "....")

f = open(file_name,'wb')
file = (b" ")
sock.send(message)
data = sock.recv(1024)

while True:
    file = file + data
    if sys.getsizeof(data) != 1057:
        break
    else:
        data = sock.recv(1024)

file = base64.decodebytes(file)
f.write(file)
f.close()

print(file_name + " has been downloaded!")
sock.close()