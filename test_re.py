# -*- coding: utf-8 -*-
# @Project: pythonProject
# @Author: HoRizon
# @Time: 2021/5/29 11:47

import re
pattern1 = re.compile(r'<p class="">\s*(.*)\s*\.\.\.<br/>', re.S)
pattern2 = re.compile(r'<p class="">.*<br/>\s*(.*)</p>', re.S)
text = '''<p class="">
                            导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                            1994 / 美国 / 犯罪 剧情
                        </p>'''
# result = pattern.search(text).group(1) + pattern.search(text).group(2)  <p class="">\s*(.*)\s*\.\.\.<br/>|
result = pattern1.search(text).group(1) + pattern2.search(text).group(1)
print(result)
# <p class="">.*<br/>\s*(.*)</p>
