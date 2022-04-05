import uuid

from lxml import etree

from utils import header
import requests
from 向数据库写入数据 import save_mongoo

url = "https://www.gushiwen.cn/"


def itempipeline(item):
    # 保存数据
    save_mongoo('prom','prom',dict(item))
    print(item)

def parse(html):    #xpath 表达式 获取元素位置
    root = etree.HTML(html)  # 获取html的根元素
    divs = root.xpath('//div[@class="left"]/div[@class="sons"]')
    item = {}
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item["name"] = div.xpath('.//p[1]//text()')
        item["author"] = ''.join(div.xpath('.//p[2]/a/text()'))
        item["content"] = '<br>'.join(div.xpath('.//div[@class="contson"]/text()'))
    # print(item)
    # save_mongoo('prom','prom',item)
    itempipeline(item)


def get(url):
    resp = requests.get(url,
                        headers={'User-Agent': header.get_ua()})
    if resp.status_code == 200:
        parse(resp.text)
    else:
        raise Exception('请求失败！')


if __name__ == '__main__':
    get(url)
