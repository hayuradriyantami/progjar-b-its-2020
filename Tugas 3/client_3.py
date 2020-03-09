import logging
import requests
import os
import threading

def download_gambar(url=None, nama=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':

    threads = []

    t = threading.Thread(target=download_gambar, args=('https://globalgrasshopper.com/wp-content/uploads/2017/03/Mount-Bromo.jpg',))
    threads.append(t)

    t = threading.Thread(target=download_gambar, args=('https://media.holidayme.com/wp-content/uploads/2019/05/22152925/holidayme_FeatureImage_PlacestToVisitInIndonesia_Bali_Shutterstock_1382245616.jpg',))
    threads.append(t)

    t = threading.Thread(target=download_gambar, args=('https://media.holidayme.com/wp-content/uploads/2019/06/18124952/holidayme_PlacestToVisitInIndonesia_Jakarta_Shutterstock_1075918016.jpg',))
    threads.append(t)

    for thr in threads:
        logging.warning(f"{thr} started")
        thr.start()
