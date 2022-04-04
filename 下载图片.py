import os

import requests

import shutil
from  myutils import  download_picture



def main():
    if not os.path.exists('images/since'):
        os.mkdir('images/since')
    resp = requests.get('https://image.so.com/zjl?ch=wallpaper&sn=10')

    picture_list = resp.json()['list']
    for pictur_dist in picture_list:
        picture_url = pictur_dist['qhimg_url']

        print(picture_url)
        download_picture('images/since/', picture_url)
    shutil.make_archive('images/car','zip', 'images/since')  #压缩 images/since下的所有文件


if __name__ == '__main__':
    main()
