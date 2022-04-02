# a = {1:'lalala',2:'alallaa',3:'lalaldwadwa'}
# # for i in a[::-1]:
# #     print(i)
# x = dict(map(reversed, a.items()))
# print(x)           #字典 key，value翻转

# l = [1,2,3,4,5]
# for n in l :
#     l = ','.join(str(n))
#     print(l)
# # sl = ','.join(str(n) for n in l)      #列表按照元素分割
# l = []
# for i in range(1,3):
#     input('请输入第 %i，个数字：'% i)
#     l.append(i)
# l.sort()
# print(l)           # sort 排序数组

# if __name__ == '__main__':
#     a = []
#     sum = 0
#     for i in range(3):
#         a.append([])
#         for j in range(3):
#             a[i].append(float(input('输入数字')))
#     for i in range(3):
#         sum += a[i][i]
# print(sum)        #矩阵对角线之和

# x = [[12, 7, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# y = [[5, 8, 1],
#      [6, 7, 3],
#      [4, 5, 9]]
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] =x[i][j] + y[i][j]
# for k in result:
#     print(k)           #矩阵之和
if __name__ == '__main__':
    class student:
        x = 0
        c = 0


    def f(stu):
        stu.x = 20
        stu.c = 'c'


    a = student()
    a.x = 3
    a.c = 'a'
    f(a)
    print(a.x, a.c)
