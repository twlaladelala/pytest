import time

import pymongo

mydict = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]


def save_mongoo(database='1',table='2',data=[{"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},]):
    global x
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[database]
    dblist = myclient.list_database_names()
    # dblist = myclient.database_names()
    if database in dblist:
        print("数据库已存在,写入数据库成功")
    else:
        print('数据库不存在，创建新的数据库')
    collist = mydb.list_collection_names()
    # collist = mydb.collection_names()
    if table in collist:  # 判断 sites 集合是否存在
        print("表已存在！")
        x = mydb[table].insert_many(data)
        print('数据添加成功')
    else:
        print('表不存在，创建新的表')
    x = mydb[table].insert_many(data)
    print('数据写入成功')


if __name__=='__main__':
    save_mongoo()
