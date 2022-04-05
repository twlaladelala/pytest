from pprint import pprint

stocks = {'Google': 100.1153,
          'BaiDu': 100.151,
          'TengXun': 500.1843,
          'SYMC': 23.1115,
          'JD': 100.1514,
          }
#生成式 成成新字典， 按照条件筛选
new_stocks = {key: value for key,value  in stocks.items() if value > 100}
# print (new_stocks)


#翻转字典的 key 和value
dict1 = dict(zip(stocks.values(), stocks.keys()))   #组成一个二元列表
print(dict1)
print(type(dict1))

print((max(dict1)))
print((min(dict1)))


print(max(zip(stocks.values(),stocks.keys())))
