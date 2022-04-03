#三方库  xlrd /xlwt / xlutils
import  xlrd
import  xlwt
import  xlutils
wb = xlrd.open_workbook('table/阿里巴巴2020年股票数据.xls')
#获取所有工作表的名字
# print(wb.sheet_names())


# sheet1 = wb.sheet_names('表格1')   #通过工作表名获取
sheet = wb.sheet_by_index(0) #通过工作表的下标ID获取工作表

#获取工作表的行数，列数
# print(sheet.nrows,sheet.ncols)

#获取单元格数据 第一行的第一列
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        value1 = sheet.cell(i,j).value
        if i >0 :
            print(f"{value1:.2f}", end='\t')
        else:
            print(value1, end=' \t')
    print()
        # print(sheet.row(i)[j].value , end=' ')
