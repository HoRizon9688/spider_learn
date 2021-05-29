# -*- coding: utf-8 -*-
# @Project: pythonProject
# @Author: HoRizon
# @Time: 2021/5/28 14:26


import re
from bs4 import BeautifulSoup
f = open('data.txt', 'r', encoding='utf-8')
html = f.read()
# print(html)
bs = BeautifulSoup(html, "html.parser")

find_name = re.compile(r'<span class="title">(.*)</span>')
find_href = re.compile(r'<a href="(.*?)">')
find_imgSrc = re.compile(r'<img.*src="(.*?)"')
find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
find_judge = re.compile(r'<span>(\d*)人评价</span>')
find_intro = re.compile(r'<span class="inq">(.*)</span>')
find_bg = re.compile(r'<p class="">(.*?)</p>', re.S)

for i in bs.find_all('div', class_='item'):
    i = str(i)
    name = re.findall(find_name, i)
    href = re.findall(find_href, i)
    imgSrc = re.findall(find_imgSrc, i)
    rating = re.findall(find_rating, i)
    judge = re.findall(find_judge, i)
    intro = re.findall(find_intro, i)
    bg = re.findall(find_bg, i)
    print(name[0])
    print(href[0])
    print(imgSrc)
    print(rating[0])
    print(judge[0])
    print(intro[0])
    # print(bg[0])
    break
