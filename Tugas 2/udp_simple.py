import socket

TARGET_IP = "192.168.0.112"
TARGET_PORT = 5006

string = "Progjar"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(string.encode()),(TARGET_IP,TARGET_PORT))
