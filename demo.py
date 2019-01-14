"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2019/1/13 17:23
@Author  : jiajia
@File    : demo.py
"""
import re
from pyquery import PyQuery as pq
with open('asd.html', 'r', encoding='utf-8')as f:
    html = f.read()
text = pq(html)
for item in text('.seckill_items_meta').items():
    xixi = dict()
    jiage = item(".seckill_items_prices").text().split('\n')
    jjfd = 1 - float(jiage[0].strip('¥'))/float(jiage[1].strip('¥'))
    jjfd = "%d" % (jjfd * 100) + "%"
    shengyu = item(".seckill_items_reserve").text()
    shengyu = re.findall('[0-9]*', shengyu)
    for i in shengyu:
        if i:
            shengyu = int(i)
            break
    else:
        shengyu = 0
    sehngyu = "{}%".format(100 - shengyu)
    xixi['商品名'] = item(".seckill_items_fn").text()
    xixi['现价'] = jiage[0]
    xixi['原价'] = jiage[1]
    xixi['降价幅度'] = jjfd
    xixi['剩余数量'] = sehngyu
    print(xixi)
    print('#####')

