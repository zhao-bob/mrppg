from xlwt import *

book = Workbook()                        # 创建新的Excel文件
sheet1 = book.add_sheet('First')         # 添加新的worksheet
al = Alignment()
al.horz = Alignment.HORZ_CENTER          # 对齐方式
al.vert = Alignment.VERT_CENTER
borders = Borders()
borders.bottom = Borders.THICK           # 边框样式
style = XFStyle()
style.alignment = al
Style.borders = borders
row = sheet1.row(0)                      # 获取第0行
row.write(0, 'test', style=style)        # 写入字符串
row = sheet1.row(1)
for i in range(5):
    row.write(i, i, style=style)         # 写入数字
row.write(5, '=SUM(A2:E2)', style=style) # 写入公式
book.save(r'test.xls')                # 保存文件

import xlrd

book = xlrd.open_workbook(r'test.xls')
sheet1 = book.sheet_by_name('First')
row = sheet1.row(0)
print(row[0].value)
print(sheet1.row(1)[2].value)
