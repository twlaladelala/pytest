import random

import xlwt
wb = xlwt.Workbook()
#添加工作表
sheet = wb.add_sheet('期末成绩')

header_style = xlwt.XFStyle()   #创建样式对象
#修改单元格颜色
header_pattern = xlwt.Pattern()
header_pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# header_pattern.pattern_back_colour =  xlwt.Style.colour_map['coral']
header_pattern.pattern_fore_colour = xlwt.Style.colour_map['aqua']


header_style.pattern = header_pattern
#修改字体
header_font = xlwt.Font()
header_font.height = 20 * 20
header_style.font = header_font
header_font.bold = True


header_aligument = xlwt.Alignment()
#对齐
header_aligument.vert = xlwt.Alignment.VERT_CENTER
header_aligument.horz = xlwt.Alignment.HORZ_CENTER
header_style.alignment = header_aligument


#写入表头
sheet.write(0,0,'姓名',header_style)     #第四个参数指定样式
sheet.write(0,1,'语文',header_style)
sheet.write(0,2,'数学',header_style)
sheet.write(0,3,'英语',header_style)

a = ["田伟","田伟1","田伟2","田伟3","田伟4"]
for i in range(1,len(a)+1):
    sheet.write(i,0,a[i-1])
    for k in range(1,4):
        sheet.write(i,k,random.randint(50,100))

wb.save('table/某年级某班成绩表.xls')

print(len(a))