#!/usr/bin/env python
# -*- encoding: utf-8 -*-


"""
获取数据,包名
"""
import csv

import requests

base_wandoujia = "https://www.wandoujia.com/apps/{0}"
base_yingyongbao = "https://webcdn.m.qq.com/webapp/homepage/index.html#/appDetail?apkName={0}"

pkg_file = "pkg.csv"
result_file = "pkg_result.csv"

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
    resp = requests.get(url)
    notFount = resp.text.__contains__("豌豆们没有找到这个页面")
    if notFount:
        print("pkg: {0} not fount!".format(pkg))
        pkg_model.pop(pkg)


def work(_token):
    readFile()
    print("内存结构: ", len(pkg_model))
    ## 去除没有内存没有值. eg: com.sz.cleanmaster
    for pkg in pkg_model.keys():
        print(pkg+"---"+base_wandoujia.format(pkg))
        requestWandoujia(pkg, base_wandoujia.format(pkg))
    ## 其他地方另存结果
    for pkg in pkg_model.keys():
        model = pkg_model[pkg]
        appname = model.app_name
        with open(result_file, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([appname, pkg])


if __name__ == '__main__':
    work("")
    # if len(sys.argv) > 1:
    #     work(sys.argv[1])
    # else:
    #     print("入参不对,即将停止")

#
#
# pkg_url = "https://raw.githubusercontent.com/parserpp/data/main/appList.csv?token={0}"
#
# """
# 文件太大无法下载
# curl -i -H "Authorization: token ${token}" \
#     https://api.github.com/repos/parserpp/data/contents/appList.csv
#
# Error msg
# This API returns blobs up to 1 MB in size. The requested blob is too large to fetch via the API,
#  but you can use the Git Data API to request blobs up to 100 MB in size
# """
# def getpkgFile(_token):
#     resp = requests.get(pkg_url.format(_token))
#     resp.encoding = 'utf-8'
#     print(resp.text)
#     pass
#
#
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
