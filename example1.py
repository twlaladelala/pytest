import xlrd
import xlwt

wb1 = xlrd.open_workbook('table/工作簿1.xls', encoding_override='utf-8')
sheet1 = wb1.sheet_by_index(0)
data = []
for row in range(1, sheet1.nrows):
    record = []
    for col in range(sheet1.ncols):
        record.append(sheet1.cell(row, col).value)
    data.append(record)
# print(data)

wb2 = xlwt.Workbook()
sheet2 = wb2.add_sheet('带颜色标记的体温数据')
sheet2.write(0, 0., '编号')
sheet2.write(0, 1., '体温')
sheet2.write(0, 2., '状态')


def get_style_by_temp(temp):
    global style
    style = xlwt.XFStyle()
    font = xlwt.Font
    if temp < 37.5:
        font.colour_index = 3
    elif temp < 38.5:
        font.colour_index = 5
    else:
        font.colour_index = 2
    return style


def get_status_by_temp(temp):
    if temp < 37.5:
        status_info = '正常'
    elif temp < 38.5:
        status_info = '发热'
    else:
        status_info = '高热'
    return status_info


count = 0
for row_index, record in enumerate(data):
    no, temp = record
    if temp > 37.2:
        count += 1
    sheet2.write(row_index + 1, 0, no)
    # get_style_by_temp(temp)
    sheet2.write(row_index + 1, 1, temp, get_style_by_temp(temp))
    sheet2.write(row_index + 1, 2, get_status_by_temp(temp))
sheet2.write(45, 0, '异常人数')
sheet2.write(45, 1, f'{count}人')
sheet2.write(46, 0, '总人数')
sheet2.write(46, 1, f'{len(data)}人')
print(data)

wb2.save('table/工作簿1.xls')
