import socket
import sys
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
port = 1803
server_address = ("localhost", port)
print("Connecting to localhost with port:", port,"....")

sock.connect(server_address)
message = ("upload test.txt")
file_name = "".join(message.split()[1])
print("Uploading file test.txt....")

f = open(file_name, "rb")
length = len(file_name) + 1
file_content = base64.encodebytes(f.read())
f.close()

f = open("base64encode","wb")
f.write(file_content)
f.close

f = open("base64encode","rb")
messages = message.encode() + (b" ") + f.read(1024)

while (messages):
    sock.send(messages)
    messages = f.read(1024)
    data = sock.recv(1024)

print(file_name + " has been uploaded!")
sock.close()