import xlwt
import main
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('test', cell_overwrite_ok=True)
test = main.get_housing()
sheet.write(0, 0, '地区')
sheet.write(0, 1, '小区')
sheet.write(0, 2, '户型')
sheet.write(0, 3, '房价')
sheet.write(0, 4, '单价')
# print(test)
for i in range(len(test)):
    sheet.write(i+1, 0, test[i][0])
    sheet.write(i+1, 1, test[i][1])
    sheet.write(i+1, 2, test[i][2])
    sheet.write(i+1, 3, test[i][3])
    sheet.write(i+1, 4, '万')
book.save(r'test1.xls')
print("ok")







