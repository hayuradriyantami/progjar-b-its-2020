import shelve
import uuid
import socket
import os
import base64

class Folder:
    def __init__(self):
        if not os.path.exists('folder'):
            os.makedirs('folder')

    def upload_file(self, name=None, file=None):
        upload = file
        f = open('folder/' + name, 'wb')
        f.write(base64.decodebytes(upload))
        return True

    def download_file(self, name=None):
        array = []
        f = open('folder/'+ name,'rb')
        read_file = f.read()
        print(read_file)
        f.close()

        result = base64.encodebytes(read_file)
        print(result)
        array.append(result.decode())
        return array

    def list_file(self):
        list = os.listdir('folder')
        array = []
        for file_name in list:
            array.append(file_name)
        return array

if __name__=='__main__':
    test = Folder()
    print(f.list_test())
