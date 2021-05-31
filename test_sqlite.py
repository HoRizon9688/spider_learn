# -*- coding: utf-8 -*-
# @Project: pythonProject
# @Author: HoRizon
# @Time: 2021/5/29 20:29

import sqlite3

# 首先创建database对象链接数据库，然后创建一个游标对象来实现对数据表的操作，操作完毕后需要将游标和数据库关闭
database = sqlite3.connect('movie250.db')
cursor = database.cursor()
sql = '''select rating, count(rating) from movie250 group by rating'''
data = cursor.execute(sql)
datalist = []  # 使用一个datalist保存查询到的值，防止关闭游标后数据丢失
print(data.fetchall())  # 游标执行sql语句后返回的是一个列表，列表中的每一项为一个元组，里面存有查询到的每一条记录
# for i in data:
#     datalist.append(data)
#     print(i)
cursor.close()
database.close()
