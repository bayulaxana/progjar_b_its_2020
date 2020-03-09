import logging
import requests
import os
import threading

def download_gambar(url=None):
    if url is None:
        return False
    ff = requests.get(url)
    types = dict()
    types['image/png']='png'
    types['image/jpg']='jpg'
    types['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if content_type in list(types.keys()):
        fileName = os.path.basename(url)
        extension = types[content_type]
        logging.warning(f"writing {fileName}.{extension}")
        fp = open(f"{fileName}.{extension}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__ == '__main__':

    image_list = [
        "https://cdn.programiz.com/sites/tutorial2program/files/bst-search-upward-recursion.jpg",
        "https://cdn.programiz.com/sites/tutorial2program/files/bst-vs-not-bst.jpg",
        "https://cdn.programiz.com/sites/tutorial2program/files/linked-list-concept.jpg"
    ]

    thread_list = []
    for i in range(len(image_list)):
        t = threading.Thread( target=download_gambar, args=(image_list[i],) )
        thread_list.append(t)

    for each_thread in thread_list:
        each_thread.start()
