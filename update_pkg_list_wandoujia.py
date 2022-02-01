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

import github_api

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# from fake_useragent import UserAgent
# ua = UserAgent(verify_ssl=False)

HEADER = {
    # 'User-Agent': ua.random,
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

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


# 定义一个进度条
def process_bar(num, total):
    rate = float(num) / total
    ratenum = int(100 * rate)
    r = '\r[{}{}]{}%'.format('*' * ratenum, ' ' * (100 - ratenum), ratenum)
    sys.stdout.write(r)
    sys.stdout.flush()


# 支持开头和持续步长（切片）
def readFile(_sbegin: int = 0, _steps: int = 0):
    with open(pkg_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        if _steps > 0:
            dur = _steps + _sbegin
            # print("readFile read [" + str(_sbegin) + "---" + str(dur) + " ]")
            for index, row in enumerate(reader):
                if (index >= _sbegin) and (index < dur):
                    # print("[" + str(_sbegin) + "---" + str(dur) + "] index: " + str(index))
                    process_bar(index - _sbegin, _steps)
                    pkg = row[1]
                    m = Model(row[0], row[1])
                    pkg_model[pkg] = m
        else:
            # print("readFile read all")
            for row in reader:
                pkg = row[1]
                m = Model(row[0], row[1])
                pkg_model[pkg] = m
                # print("add ", pkg, " success. d: ", len(pkg_model))
        print("\r\n")


# 豌豆荚包含该app
def isFountInWandoujia(pkg, url):
    try:
        resp = requests.get(url, headers=HEADER, timeout=3, verify=False)

        if resp.status_code == 200:
            if "该应用已下架" in resp.text:
                print("pkg: {0} 抱歉  not fount!".format(pkg))
                return False
            elif "没有找到这个页面" in resp.text:
                print("pkg: {0} 相似应用下载  not fount!".format(pkg))
                return False
            elif "app-offline-down" in resp.text:
                print(
                    "pkg: {0} 图片(安装豌豆荚,下载相似应用)下载链接容器  not fount!".format(pkg))
                return False
            elif "image.uc.cn/s/uae/g/0n/wenshan/1.png" in resp.text:
                print("pkg: {0} 图片链接  not fount!".format(pkg))
                return False
            elif "download-wp" in resp.text:
                print(pkg + "---包含download-wp----200----")
                return True
            else:
                # print(pkg + "-----200---其他情况-----" + resp.text)
                print(pkg + "-----[%s]200---其他情况-----\n %s" % ( pkg, resp.text))
                return False
        else:
            return False
    except Exception as e:
        print(e)
        return False
    return False


def work(
        _token=os.getenv('GITHUB_TOKEN', ""), _sbegin: int = 0,
        _step: int = 0):
    readFile(_sbegin, _step)

    print("[%d-%d] 读取文件完毕,内存数量:%d " % (_sbegin,
                                       (_sbegin + _step), len(pkg_model)))
    ## 去除没有内存没有值. eg: com.sz.cleanmaster
    for pkg in pkg_model.keys():
        if isFountInWandoujia(pkg, base_wandoujia.format(pkg)):
            success_pkg_model[pkg] = pkg_model[pkg]
    print("[%d-%d] 检测完成，成功个数: %d" % (_sbegin, (_sbegin + _step), len(success_pkg_model)))
    if len(success_pkg_model) > 0:
        # 查找关联应用

        # 写文件需要追加
        with open(result_file, "w+") as csvfile:
            ## 其他地方另存结果
            for pkg in success_pkg_model.keys():
                try:
                    model = success_pkg_model[pkg]
                    appname = model.app_name
                    print(appname + "-------" + pkg)
                    writer = csv.writer(csvfile)
                    writer.writerow([appname, pkg])
                except Exception as e:
                    print("[" + pkg + "] happen Exception")

        # github_api.create_file(_owner="parserpp",
        #                        _repo="data",
        #                        _path="/pkgs/" + str(_sbegin) + "_" +
        #                        str(_step) + ".csv",
        #                        _token=_token,
        #                        _filename=result_file,
        #                        _commit_msg="ppppp",
        #                        _name="who are U")
    else:
        print("木有成功的啊")


def realwork(argv):
    if len(argv) > 1:
        print("收到多个参数： " + str(sys.argv))
        token = sys.argv[1]
        begin_index = int(sys.argv[2])
        step_len = int(sys.argv[3])
        work(token, begin_index, step_len)
    else:
        print("入参不对,即将开启所有的工作模式")
        # work()


"""
argv：
   token: github token
   s1: start_index 开始下标
   s2: step 步长。持续数量
"""
if __name__ == '__main__':
    realwork(sys.argv)

    # work("", 0, 10)
    # work("", 1000, 1000)
    # work("", 2000, 1000)
    # work("", 3000, 1000)
    # work("", 4000, 1000)
    # work("", 5000, 1000)
