import os

import requests

import shutil
from myutils import download_picture
from myutils import send_email


def main():
    if not os.path.exists('images/since'):
        os.mkdir('images/since')
    resp = requests.get('https://image.so.com/zjl?ch=wallpaper&sn=10')

    picture_list = resp.json()['list']
    for picture_dist in picture_list:
        picture_url = picture_dist['qhimg_url']

        print(picture_url)
        download_picture('images/since/', picture_url)
    shutil.make_archive('images/car', 'zip', 'images/since')  # 压缩 images/since下的所有文件
    send_email(
        form_user='18318055277@163.com',
        to_user='ha1586795195@qq.com',
        subject='资源分享',
        content='附件中有下载的内容，请注意查收！',
        filenames=['images/car.zip']
    )


if __name__ == '__main__':
    main()
