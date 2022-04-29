#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re

import requests
from bs4 import BeautifulSoup


# 1.发送请求：
def get_html(url):
    res = requests.get(url)
    return res

# 2.解析数据
def parse_data(data):
    soup = BeautifulSoup(data, 'lxml')
    # 获取所有的li标签，li中包含所有想要的数据
    li_list = soup.find_all(name='li')
    for li in li_list:
        # app详情url
        app_detail = li.find(name='a').attrs.get('href')
        print('详情url:', app_detail)

        # app图标url
        app_img_url = li.find(name='img').attrs.get('data-original')
        print('图标url:', app_img_url)

        # app名称
        app_name = li.find(name='img').attrs.get('alt')
        print('名称:', app_name)

        # 下载人数
        app_download_num = li.find(name='span', attrs={'class': 'install-count'}).text
        print('下载人数:', app_download_num)

        # 大小
        try:
            # 有可能匹配规则是错的或者没有大小，然后获取不到text文本
            app_size = li.find(name='span', attrs={'title': re.compile('MB')}).text
        except Exception as e:
            # 放弃匹配规则不一样的数据，默认为空字符串
            app_size = ''
        print('大小:', app_size)

        # 简介
        app_comment = li.find(name='div', attrs={'class': 'comment'}).text
        print('简介:', app_comment)
        print('*' * 100)

        yield app_name, app_detail, app_img_url, app_download_num, app_size, app_comment

        # app_data = f"""
        #     '名称:', {app_name},
        #     '详情url:', {app_detail},
        #     '图标url:', {app_img_url},
        #     '下载人数:', {app_download_num},
        #     '大小:', {app_size},
        #     '简介:', {app_comment}
        # """
        # save(app_data)


# # 3.保存数据到数据库中
# def save(generator_data, mysql_obj):

#     for data in generator_data:
#         print(data)
#         sql = 'insert into wandoujia(app_name, app_detail, app_img_url, app_download_num, app_size, app_comment)' \
#               ' values(%s, %s, %s, %s, %s, %s) '
#         print(sql)
#         mysql_obj.execute(sql, data)

if __name__ == '__main__':
    # 1.获取所有app的接口url
    # for i in range(1,42):
    #     url = f'https://www.wandoujia.com/wdjweb/api/top/more?resourceType=0&page={i}&ctoken=mrci2hDXHNxavE42fJ85v3JE'

    #     # 获取响应数据
    #     res = get_html(url)

    #     # 将json数据转成字典
    #     res_dict = res.json()
    #     # 获取字典中data的值中的content的值
    #     data = res_dict.get('data').get('content')
    #     generator_data = parse_data(data)

    #     # 保存数据到数据库中
    #     print("generator_data ", generator_data)

    url = f'https://www.wandoujia.com/wdjweb/api/top/more?resourceType=0&page=1&ctoken=mrci2hDXHNxavE42fJ85v3JE'
    # 获取响应数据
    res = get_html(url)
    # 将json数据转成字典
    res_dict = res.json
    # 获取字典中data的值中的content的值
    data = res_dict.get('data').get('content')
    generator_data = parse_data(data)

    # 保存数据到数据库中
    print("generator_data ", generator_data)
