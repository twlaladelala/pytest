import re

# content = "马化腾是一个杀逼刹雕FUCK you"
# pattern = re.compile(r'[傻杀煞刹][逼笔币毕屌叼雕]|马化腾|fuck|shit',flags=re.IGNORECASE)
# # replace_content = re.sub(r'[傻杀煞刹][逼笔币毕屌叼雕]|马化腾|fuck|shit', '*', content)
# replace_content = pattern.sub('*',content)   #sub  替换
# print(replace_content)



#正则表达式拆分字符串
poem = '床前明月光，疑是地上霜，举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。]', poem)  #maxsplit= 2   表示拆分两次，剩余不拆分
print(sentences_list)
sentences_list = [sentence for sentence in sentences_list if sentence] #
print(sentences_list)
for sentence in sentences_list:
    print (sentence)