import json
import logging
import base64
from folder import Folder

'''
PROTOCOL FORMAT

String terbagi menjadi 2 bagian, dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter

FITUR

a. Meletakkan File
   Fungsi   : Untuk menambahkan file ke dalam direkori 'folder' 
   Request  : Upload 
   Parameter: NamaFile *spasi* isiFile
   Response : Jika berhasil, maka akan mengeluarkan tulisan 'namaFile Has been uploaded!'
              Jika gagal, maka akan mengeluarkan tulisan 'ERROR' 

b. Mengambil File
   Fungsi   : Untuk mengunduh file dari dalam direktori 'folder'
   Request  : Download
   Parameter: NamaFile
   Response : Jika berhasil, maka akan mengeluarkan tulisan 'namaFile has been downloaded!'
              Jika gagal, maka akan mengeluarkan tulisan 'ERROR'             

c. Melihat List File 
   Fungsi   : Untuk melihat daftar file yang terdapat di dalam direktori 'folder'
   Request  : List
   Parameter: -
   Response : Menampilkan nama file yang terdapat di dalam direktori 'folder'
   
Jika command tidak dikenali akan merespon dengan ERRCMD
'''

f = Folder()

class Folder_machine:
    def process(self, string_to_process):
        s = string_to_process
        cstrings = s.split(" ")
        try:
            command = cstrings[0].strip()
            if command == "upload":
                logging.warning("upload")
                source = cstrings[1].strip()
                dest = cstrings[2].strip()
                f.upload_file(source, dest.encode())
                return "File uploaded"
            elif command == "download":
                logging.warning("download")
                source = cstrings[1].strip()
                res = f.download_file(source)
                return res[0]
            elif command == "list":
                logging.warning("list")
                res = f.list_file()
                return json.dumps(res)
            else:
                return "ERROR CMD"
        except:
            return "ERROR"


if __name__ == '__main__':
    fm = Folder_machine()
    run = fm.process("list")
    print(run)