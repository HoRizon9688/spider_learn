# -*- coding: utf-8 -*-
# @Project: pythonProject
# @Author: HoRizon
# @Time: 2021/5/29 17:52

import xlwt
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
for i in range(1, 10):
    for j in range(1, i + 1):
        # print("{}*{}={}".format(i, j, i*j), end=" ")
        worksheet.write(i-1, j-1, "{}*{}={}".format(i, j, i*j))
workbook.save('test.xls')

