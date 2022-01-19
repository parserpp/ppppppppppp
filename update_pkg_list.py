#!/usr/bin/env python
# -*- encoding: utf-8 -*-


"""
获取数据,包名
"""
import csv
import os
import sys

import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# from fake_useragent import UserAgent
# ua = UserAgent(verify_ssl=False)

HEADER = {
        # 'User-Agent': ua.random,
          'Accept': '*/*',
          'Connection': 'keep-alive',
          'Accept-Language': 'zh-CN,zh;q=0.8'}

import github_api

base_wandoujia = "https://www.wandoujia.com/apps/{0}"
base_yingyongbao = "https://webcdn.m.qq.com/webapp/homepage/index.html#/appDetail?apkName={0}"

pkg_file = "pkg.csv"
result_file = "pkg_result.csv"

pkg_model = {}
success_pkg_model = {}


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


# 支持开头和持续步长（切片）
def readFile(_sbegin: int = 0, _steps: int = 0):
    with open(pkg_file, 'r', encoding='utf-8') as f:

        reader = csv.reader(f)
        if (_steps > 0):
            dur = _steps + _sbegin
            print("readFile read [" + str(_steps) + ", " + str(dur) + " ]")
            for index, row in enumerate(reader):
                if index >= _sbegin and index < dur:
                    pkg = row[1]
                    m = Model(row[0], row[1])
                    pkg_model[pkg] = m
        else:
            print("readFile read all")
            for row in reader:
                pkg = row[1]
                m = Model(row[0], row[1])
                pkg_model[pkg] = m
                # print("add ", pkg, " success. d: ", len(pkg_model))


# 豌豆荚包含该app
def isFountInWandoujia(pkg, url):
    try:
        resp = requests.get(url
                            , headers=HEADER
                            , timeout=3
                            , verify=False
                            )
        if "豌豆们没有找到这个页面" in resp.text:
            print("pkg: {0} not fount!".format(pkg))
            return False
        else:
            print(pkg + "----success")
            return True
    except Exception as e:
        print(e)
        return False


def work(_token=os.getenv('GITHUB_TOKEN', ""), _sbegin: int = 0, _step: int = 0):
    readFile(_sbegin, _step)

    print("内存结构: ", len(pkg_model))
    # ## 去除没有内存没有值. eg: com.sz.cleanmaster
    # for pkg in pkg_model.keys():
    #     if isFountInWandoujia(pkg, base_wandoujia.format(pkg)):
    #         success_pkg_model[pkg] = pkg_model[pkg]
    # print("检测完成，成功个数: ", len(success_pkg_model))
    # ## 其他地方另存结果
    # for pkg in success_pkg_model.keys():
    #     try:
    #         model = success_pkg_model[pkg]
    #         appname = model.app_name
    #         with open(result_file, "w") as csvfile:
    #             writer = csv.writer(csvfile)
    #             writer.writerow([appname, pkg])
    #     except Exception as e:
    #         print("[" + pkg + "] happen Exception")
    # github_api.create_file(_owner="parserpp"
    #                        , _repo="data"
    #                        , _path="/pkgs/" + str(_sbegin) + "_" + str(_step) + ".csv"
    #                        , _token=_token
    #                        , _filename=result_file
    #                        , _commit_msg="ppppp"
    #                        , _name="who are U"
    #                        )


"""
argv：
   token: github token
   s1: start_index 开始下标
   s2: step 步长。持续数量
"""
if __name__ == '__main__':
    # work("xxxx", 0, 1000)
    # print(sys.argv)
    if len(sys.argv) > 1:
        print("收到多个参数： " + str(sys.argv))
        token = sys.argv[1]
        begin_index = int(sys.argv[2])
        step_len = int(sys.argv[3])
        work(token, begin_index, step_len)
    else:
        print("入参不对,即将开启所有的工作模式")
        # work()
