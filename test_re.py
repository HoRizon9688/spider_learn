# -*- coding: utf-8 -*-
# @Project: pythonProject
# @Author: HoRizon
# @Time: 2021/5/29 11:47

import re


# 两种匹配方式均可获得结果，一种使用两个正则表达式区分别匹配<br/>前面和后面的数据，然后再拼接起来
# 第二种匹配方式为使用.*进行全部匹配，然后使用.strip()方法去掉空格，然后再用正则表达式匹配空格再删去
# pattern1 = re.compile(r'<p class="">\s*(.*)<br/>', re.S)
# pattern2 = re.compile(r'<p class="">.*<br/>\s*(.*)</p>', re.S)
pattern = re.compile(r'<p class="">(.*)</p>', re.S)

text = '''<p class="">
                            导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...<br/>
                            1994 / 美国 / 犯罪 剧情
                        </p>'''

# result = pattern1.search(text).group(1) + pattern2.search(text).group(1)
result = pattern.search(text).group(1).strip()
result = re.sub(r'<br/>\s*', '', result)
print(result)
