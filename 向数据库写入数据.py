import time

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["lalala1"]
dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "lalala1" in dblist:
  print("数据库已存在,写入数据库成功")
else: print('数据库不存在，创建新的数据库')

collist = mydb.list_collection_names()
# collist = mydb.collection_names()
if "sites" in collist:   # 判断 sites 集合是否存在
  print("表已存在！")
else: print('表不存在，创建新的表')

mydict = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]

# x = mydb['sites'].insert_many(mydict)
start_time = time.time()
for x in mydb['sites'].find():
    print (x)
    end_time = time.time()



