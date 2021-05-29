# -*- coding: utf-8 -*-
# @Project: pythonProject
# @Author: HoRizon
# @Time: 2021/5/27 10:44

import re
from bs4 import BeautifulSoup
f = open('data.txt', 'r', encoding='utf-8')
html = f.read()
#print(html)
bs = BeautifulSoup(html, "html.parser")

find_name = re.compile(r'<span class="title">(.*)</span>')
find_href = re.compile(r'<a href="(.*?)">')
find_imgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
find_judge = re.compile(r'<span>(\d*)人评价</span>')
find_intro = re.compile(r'<span class="inq">(.*)</span>')
find_bg1 = re.compile(r'<p class="">\s*(.*?)<br/>', re.S)
find_bg2 = re.compile(r'<p class="">.*<br/>\s*(.*?)</p>', re.S)

for i in bs.find_all('div', class_='item'):
    i = str(i)
    # print(i)
    name = find_name.search(i).group(1)
    href = find_href.search(i).group(1)
    imgSrc = find_imgSrc.search(i).group(1)
    rating = find_rating.search(i).group(1)
    judge = find_judge.search(i).group(1)
    intro = find_intro.search(i).group(1)
    bg = find_bg1.search(i).group(1) + " " + find_bg2.search(i).group(1)
    print(name)
    print(href)
    print(imgSrc)
    print(rating)
    print(judge)
    print(intro)
    print(bg)

