# -*- coding: utf-8 -*-
# @Project: pythonProject
# @Author: HoRizon
# @Time: 2021/5/29 20:29

import sqlite3

database = sqlite3.connect('test.db')
cursor = database.cursor()
sql = '''
        create table company
        (id int primary key not null,
        name char(10) not null,
        age int not null,
        address char(50),
        salary real);
'''
cursor.execute(sql)
database.commit()
database.close()
