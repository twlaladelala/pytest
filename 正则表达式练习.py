"""


字符集  ----> -----> [a-za-Z0-9]{6,20} ---->\w{6,20}

\w    匹配字符串
\d    匹配数字

Python使用政策表达式的两种方式




"""


import  re
username = input('请输入用户名：')
# if re.match(r'^\w{6,20}$', username) is None: print('用户名不合法')
#  ^  表示从字符串头开始 ，，   $表示匹配到字符串结尾
if re.fullmatch(r'\w{6,20}', username) is None: print('用户名不合法')

#匹配QQ号
qq = input('请输入QQ号：')
matcher = re.fullmatch(r'[1-9]\d{9}', qq)

