# -*- coding: utf-8 -*-
# @Project: pythonProject
# @Author: HoRizon
# @Time: 2021/5/27 10:44

from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.parse
import urllib.error
import xlwt
import sqlite3

# baseurl = "https://movie.douban.com/top250?start="
find_name = re.compile(r'<span class="title">(.*)</span>')
find_href = re.compile(r'<a href="(.*?)">')
find_imgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
find_judge = re.compile(r'<span>(\d*)人评价</span>')
find_intro = re.compile(r'<span class="inq">(.*)</span>')
find_bg1 = re.compile(r'<p class="">\s*(.*?)<br/>', re.S)
find_bg2 = re.compile(r'<p class="">.*<br/>\s*(.*?)</p>', re.S)


def get_data(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = get_html(url)
        bs = BeautifulSoup(html, "html.parser")
        for item in bs.find_all('div', class_='item'):
            data = []
            item = str(item)
            name = find_name.search(item).group(1)
            # print(name)
            data.append(name)
            href = find_href.search(item).group(1)
            # print(href)
            data.append(href)
            imgSrc = find_imgSrc.search(item).group(1)
            # print(imgSrc)
            data.append(imgSrc)
            rating = find_rating.search(item).group(1)
            # print(rating)
            data.append(rating)
            judge = find_judge.search(item).group(1)
            # print(judge)
            data.append(judge)
            if find_intro.search(item):  # 部分电影没有简评，直接调用group方法会报错
                intro = find_intro.search(item).group(1).replace("。", "")
                # print(intro)
                data.append(intro)
            else:
                data.append(" ")
            bg = find_bg1.search(item).group(1) + " " + find_bg2.search(item).group(1)
            # print(bg)
            data.append(bg)
            datalist.append(data)
    return datalist


# 获取单个页面html源码
def get_html(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
    request = urllib.request.Request(url=url, headers=headers, method='GET')
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8").replace("&nbsp;", " ")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def save_data(datalist):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    column = ("电影名", "豆瓣链接", "封面链接", "评分", "评价人数", "简评", "相关信息")
    for i in range(7):
        worksheet.write(0, i, column[i])
    for i in range(len(datalist)):
        for j in range(len(datalist[i])):
            worksheet.write(i+1, j, datalist[i][j])
    workbook.save('douban.xls')


if __name__ == "__main__":
    datalist = get_data("https://movie.douban.com/top250?start=")
    # 保存到douban.xls表格中
    save_data(datalist)
    # print(a)
    # 将爬取的信息保存到本地data.txt中
    # f = open("data.txt", 'w', encoding='utf-8')
    # f.write(a)
    # f.close()
