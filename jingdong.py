"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2019/1/13 16:30
@Author  : jiajia
@File    : jingdong.py
"""

import re

from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
mobile_emulation = {"deviceName": "iPhone 6"}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 30)


url = "https://m.jd.com/"
browser.get(url)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]/div[5]/div/div[1]'))).click()
js = "var q=document.documentElement.scrollTop=100"
browser.execute_script(js)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="floorContent"]/div[7]/div/div/div[1]/a[2]'))).click()
number = 0
while True:
    try:
        js = "window.scrollTo(0,document.body.scrollHeight)"
        browser.execute_script(js)
        html = browser.find_element_by_xpath("//*").get_attribute("outerHTML")
        shuliang = re.findall('立即抢购', html)
    except:
        browser.refresh()
        continue
    print(len(shuliang))
    if len(shuliang) == number and len(shuliang) > 0:
        break
    else:
        number = len(shuliang)

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







