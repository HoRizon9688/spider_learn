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


if __name__ == "__main__":
    a = get_html("https://movie.douban.com/top250?start=0")
    # print(a)
    f = open("data.txt", 'w', encoding='utf-8')
    f.write(a)
    f.close()

