from socket import *
import socket
import threading
import logging
import time
import sys
from folder_machine import Folder_machine

fm = Folder_machine()
port = 1803
class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        file = (b'')
        array = []
        while True:
            while True:
                data = self.connection.recv(1024)
                file = file + data
                array.append(data)
                byte = int(sys.getsizeof(data))

                if byte != 1057:
                    print(byte)
                    break
                else:
                    print(byte)
                    self.connection.sendall(b'')
            data = file
            if data:
                d = data.decode()
                result = fm.process(d)
                result = result
                self.connection.sendall(result.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('localhost', port))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    print("Server running....")
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()

