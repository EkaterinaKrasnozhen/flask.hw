# Задание №9
# � Написать программу, которая скачивает изображения с заданных URL-адресов и
# сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
# файле, название которого соответствует названию изображения в URL-адресе.
# � Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
# image1.jpg
# � Программа должна использовать многопоточный, многопроцессорный и
# асинхронный подходы.
# � Программа должна иметь возможность задавать список URL-адресов через
# аргументы командной строки.
# � Программа должна выводить в консоль информацию о времени скачивания
# каждого изображения и общем времени выполнения программы.

import requests
import threading
import time
from sys import argv

urls = ['https://w.forfun.com/fetch/3e/3e6d5f96bb0a293b7eb3866e91f2fd32.jpeg',
'https://w.forfun.com/fetch/ca/ca3c70c3111dde977a73ebf659a9ccc2.jpeg',
'https://mobimg.b-cdn.net/v3/fetch/32/32270e41db5c3c8763937d843a9d1fc8.jpeg',
'https://i.pinimg.com/originals/21/25/ee/2125ee74769913bb6793f249d4a8cded.jpg',
'https://i.pinimg.com/originals/8a/a7/83/8aa7831e22f8d5c74aecfe0c0e6953e3.jpg',
'https://klike.net/uploads/posts/2023-01/1674543731_3-86.jpg',
]


def download(url):
    filename = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")


threads = []
start_time = time.time()
    

if __name__ == '__main__':
    urls = argv[1:]
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()