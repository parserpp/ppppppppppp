#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# import requests
# from bs4 import BeautifulSoup
#
# # url = 'http://www.pbc.gov.cn/huobijinyinju/147948/147964/index.html'
# url = 'https://webcdn.m.qq.com/webapp/homepage/index.html#/'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
#            }
# res = requests.get(url,headers=headers)
# res.encoding = 'utf-8'
# soup = BeautifulSoup(res.text,'html.parser')
# print(soup)


"""
加载另一个
"""
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from lxml import etree
#
# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
# chrome_options.add_argument('--disable-gpu') # 禁止加载图片
# driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行
#
# url = 'http://www.pbc.gov.cn/huobijinyinju/147948/147964/index.html'
#
# driver.get(url)
# html = etree.HTML(driver.page_source)
# print(html)
#
# extract_announcements_list = html.xpath('//*[@id="22786"]/div[2]/div[1]/table/tbody/tr[2]/td/table')
# print(extract_announcements_list)
# for i in extract_announcements_list:
#     announcement_date = i.xpath('./tbody/tr/td[2]/span/text()')
#     announcement_title = i.xpath('./tbody/tr/td[2]/font/a/@title')
#     announcement_link = i.xpath('./tbody/tr/td[2]/font/a/@href')
#     real_link = 'http://www.pbc.gov.cn' + announcement_link[0]
#     print(announcement_title,announcement_date,real_link)



"""
加载百度地址
"""
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')
