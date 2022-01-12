#!/usr/bin/env python
# -*- encoding: utf-8 -*-


"""
获取数据,包名
"""
import csv
import requests

base_wandoujia = "https://www.wandoujia.com/apps/{0}"
base_yingyongbao = "https://webcdn.m.qq.com/webapp/homepage/index.html#/appDetail?apkName={0}"


pkg_file="pkg.csv"
result_file="pkg_result.csv"

pkg_model = {}


class Model(object):
    url_wandoujia = ""
    url_yingyonbao = ""
    url_huawei = ""
    is_contains_wandoujia = False
    is_contains_yingyonbao = False
    is_contains_huawei = False

    # 初始化中给对象属性赋值
    def __init__(self, __app_name, __package_name):
        self.app_name = __app_name
        self.package_name = __package_name



def readFile():
    with open(pkg_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            pkg = row[1]
            m = Model(row[0], row[1])
            pkg_model[pkg] = m
            # print("add ", pkg, " success. d: ", len(pkg_model))


'''
豌豆荚包含该app,判断后，减少内存的结构。
'''


def requestWandoujia(pkg, url):
    get
    resp = requests.get(url)
    notFount = resp.text.__contains__("豌豆们没有找到这个页面")
    if notFount:
        pkg_model.pop(pkg)


if __name__ == '__main__':
    getpkgFile()
    readFile()
    print("内存结构: ", len(pkg_model))
    # 去除没有内存没有值. eg: com.sz.cleanmaster
    for pkg in pkg_model.keys():
        requestWandoujia(pkg, base_wandoujia.format(pkg))


# def parser_line(line):
#     # requests.request(url.format())
#     temp1 = line.strip()
#     temp2 = temp1.split(',')
#     print(temp2)
#     pass
#
# """
#  应用宝检查需要：开启javascript
# https://webcdn.m.qq.com/webapp/homepage/index.html#/appDetail?apkName=com.UCMobile
#
# """
# from bs4 import BeautifulSoup
# def requestYingyongbao(url):
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
#         }
#     resp = requests.get(url, headers=headers)
#     resp.encoding = 'utf-8'
#     # print(resp.content)
#     # print(resp.text)
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     print(soup)
#
#     pass
