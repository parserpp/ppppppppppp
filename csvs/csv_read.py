#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import csv

try:
    # 取别名，并且自动关闭文件
    with open('../pkg.csv', 'r') as db01:
        # 返回一个生成器对象，reader是可迭代的
        # reader = csv.reader(db01)
        # for row in reader:
        #   print(row)
        reader = csv.reader(db01)
        for index, rows in enumerate(reader):
            if index > 7 and index < 20:
                print(str(index)+"--->"+str(rows))

# 捕捉异常本身，打印异常信息
except csv.Error as e:
    print("Error at line %s :%s", reader.line_num, e)
